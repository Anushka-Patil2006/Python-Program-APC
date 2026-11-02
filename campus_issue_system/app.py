import os, sqlite3, uuid
from datetime import datetime
from flask import Flask, request, redirect, session, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder=".")
app.secret_key = "change-this-secret"
os.makedirs("static/uploads", exist_ok=True)

ADMIN_USER, ADMIN_PASS = "admin", "admin123"
CATEGORIES = ["Electricity", "Water", "Cleanliness", "Classroom", "Hostel", "Other"]


# ---------- Database ----------
def db():
    con = sqlite3.connect("campus.db")
    con.row_factory = sqlite3.Row
    return con


def init_db():
    con = db()
    con.executescript("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE, password TEXT);
    CREATE TABLE IF NOT EXISTS complaints(
        id TEXT PRIMARY KEY, student_id INTEGER, title TEXT, category TEXT, location TEXT,
        description TEXT, photo TEXT, priority TEXT DEFAULT 'Not set',
        status TEXT DEFAULT 'Submitted', resolution TEXT DEFAULT '', created_at TEXT);
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT, complaint_id TEXT, status TEXT, time TEXT);
    """)
    con.commit()
    con.close()


def now():
    return datetime.now().strftime("%d %b %Y, %H:%M")


# ---------- Home ----------
@app.route("/")
def home():
    return render_template("index.html", page="home")


# ---------- Student: register / login ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            con = db()
            con.execute("INSERT INTO students(name,email,password) VALUES(?,?,?)",
                        (request.form["name"], request.form["email"],
                         generate_password_hash(request.form["password"])))
            con.commit()
            flash("Account created. Log in to report an issue.")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("This email is already registered. Try logging in.")
    return render_template("index.html", page="register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        s = db().execute("SELECT * FROM students WHERE email=?", (request.form["email"],)).fetchone()
        if s and check_password_hash(s["password"], request.form["password"]):
            session["student_id"] = s["id"]
            return redirect("/my")
        flash("Email or password is wrong. Check both and try again.")
    return render_template("index.html", page="login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------- Student: report / view / track ----------
@app.route("/report", methods=["GET", "POST"])
def report():
    if "student_id" not in session:
        return redirect("/login")
    if request.method == "POST":
        f = request.form
        if not f["title"].strip() or not f["description"].strip():
            flash("Add a title and a description before submitting.")
            return redirect("/report")
        cid = "CMP" + uuid.uuid4().hex[:6].upper()
        photo = ""
        file = request.files.get("photo")
        if file and file.filename:
            photo = cid + "_" + os.path.basename(file.filename)
            file.save("static/uploads/" + photo)
        con = db()
        con.execute("INSERT INTO complaints(id,student_id,title,category,location,description,photo,created_at)"
                    " VALUES(?,?,?,?,?,?,?,?)",
                    (cid, session["student_id"], f["title"], f["category"], f["location"],
                     f["description"], photo, now()))
        con.execute("INSERT INTO history(complaint_id,status,time) VALUES(?,?,?)", (cid, "Submitted", now()))
        con.commit()
        flash("Complaint submitted. Your complaint ID is " + cid + ". Keep it to track progress.")
        return redirect("/my")
    return render_template("index.html", page="report", cats=CATEGORIES)


@app.route("/my")
def my():
    if "student_id" not in session:
        return redirect("/login")
    rows = db().execute("SELECT * FROM complaints WHERE student_id=? ORDER BY rowid DESC",
                        (session["student_id"],)).fetchall()
    return render_template("index.html", page="my", rows=rows)


@app.route("/track")
def track():
    if "student_id" not in session:
        return redirect("/login")
    cid = request.args.get("cid", "").strip().upper()
    c, hist = None, []
    if cid:
        c = db().execute("SELECT * FROM complaints WHERE id=? AND student_id=?",
                         (cid, session["student_id"])).fetchone()
        hist = db().execute("SELECT * FROM history WHERE complaint_id=? ORDER BY id", (cid,)).fetchall()
        if not c:
            flash("No complaint found with that ID in your account.")
    return render_template("index.html", page="track", c=c, hist=hist, cid=cid)


# ---------- Admin ----------
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form["user"] == ADMIN_USER and request.form["password"] == ADMIN_PASS:
            session["admin"] = True
            return redirect("/admin")
        flash("Admin username or password is wrong.")
    return render_template("index.html", page="admin_login")


@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect("/admin_login")
    cat, pri = request.args.get("category", ""), request.args.get("priority", "")
    q = "SELECT complaints.*, students.name AS student FROM complaints JOIN students ON students.id=student_id WHERE 1=1"
    args = []
    if cat:
        q += " AND category=?"; args.append(cat)
    if pri:
        q += " AND priority=?"; args.append(pri)
    con = db()
    rows = con.execute(q + " ORDER BY complaints.rowid DESC", args).fetchall()
    counts = {r["status"]: r["n"] for r in con.execute("SELECT status, COUNT(*) AS n FROM complaints GROUP BY status")}
    return render_template("index.html", page="admin", cats=CATEGORIES, rows=rows, cat=cat, pri=pri, counts=counts)


@app.route("/admin/<cid>", methods=["GET", "POST"])
def admin_update(cid):
    if not session.get("admin"):
        return redirect("/admin_login")
    con = db()
    if request.method == "POST":
        f = request.form
        old = con.execute("SELECT status FROM complaints WHERE id=?", (cid,)).fetchone()
        con.execute("UPDATE complaints SET priority=?, status=?, resolution=? WHERE id=?",
                    (f["priority"], f["status"], f["resolution"], cid))
        if old and old["status"] != f["status"]:
            con.execute("INSERT INTO history(complaint_id,status,time) VALUES(?,?,?)", (cid, f["status"], now()))
        con.commit()
        flash("Complaint " + cid + " updated.")
        return redirect("/admin")
    c = con.execute("SELECT * FROM complaints WHERE id=?", (cid,)).fetchone()
    return render_template("index.html", page="admin_update", c=c)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
