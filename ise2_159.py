#1st problem.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

sentence = "This is a simple program to remove stopwords from the sentence"

stop_words = set(stopwords.words('english'))

words = word_tokenize(sentence)

result = [word for word in words if word.lower() not in stop_words]

print("Original sentence:", sentence)
print("After removing stopwords:", " ".join(result))


#2nd Problem

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#2. Count the frequency of each char
s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))

#3. Reverse a word 
s = input("Enter a word: ")

print("Reversed word:", s[::-1])

#4. anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagrams")
else:
    print("Not anagrams")

#5. Find a substring in a string 
s = input("Enter a string: ")
sub = input("Enter substring to find: ")

if sub in s:
    print("Substring found")
else:
    print("Substring not found")


#3rd problem


group1 = ["Reading", "Gaming", "Cooking", "Reading", "Music"]
group2 = ["Gaming", "Music", "Dancing", "Swimming", "Gaming"]

set1 = set(group1)
set2 = set(group2)

print("Group 1 hobbies:", sorted(set1))
print("Group 2 hobbies:", sorted(set2))

print("All hobbies:", sorted(set1 | set2))

print("Common hobbies:", sorted(set1 & set2))

print("Only Group 1:", sorted(set1 - set2))

print("Only Group 2:", sorted(set2 - set1))



