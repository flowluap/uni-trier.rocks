#!/usr/bin/python

"""
Learning Regular Expressions

Resources:
https://docs.python.org/3.7/howto/regex.html
https://pythonprogramming.net/regular-expressions-regex-tutorial-python-3/ (Later on this tutorial will explain how to
parse a website)

Others:
https://www.python-course.eu/python3_re.php
https://www.tutorialspoint.com/python/python_reg_expressions.htm (Python 2)
https://www.learnpython.org/en/Regular_Expressions
"""



"""
Identifiers:
\d -> One decimal digit, same as [0-9]
\D -> One non-digit, same as [^0-9]
\w -> One word character including digits, same as [a-zA-Z0-9_]
\W -> One non-word character, same as [^a-zA-Z0-9_]
\s -> One whitespace, same as [ \t\n\r\f\v]
\S -> One non-whitespace, same as [^ \t\n\r\f\v]
\b -> Word boundary = space around whole words
\n -> Newline
\t -> Tab
. -> Any one character except new line
\. -> Period, '.' without backslash means any character


Metacharacters:
Metacharacters can't be used like other characters in regexes since they fulfill special functions, they are:
. ^ $ * + ? { } [ ] \ | ( )


Modifiers:
^ -> Matches at start of string
$ -> Matches at end of string
+ -> Match one or more repetitions/characters
* -> Match zero or more repetitions/characters
? -> Match zero or one repetitions/characters
ab|cd -> Matches ab or cd
[ab-d] -> Range, or "variance" = one character of: a, b, c, d
[^ab-d] -> One character except: a, b, c, d
() -> Items within parenthesis are retrieved/matched (groups)
(a(bc)) -> Items within the sub-parenthesis are retrieved
| = Matches either/or. Example x|y = will match either x or y


Brackets:
[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z


Repetitions:
[ab]{2} -> Exactly 2 continuous occurrences of a or b
[ab]{2,5} -> 2 to 5 continuous occurrences of a or b
[ab]{2,} -> 2 or more continuous occurrences of a or b
+ -> One or more
* -> Zero or more
? -> 0 or 1


Patterns:
Basic example: '\s+'
-> '\s' matches any whitespace character, '+' requires the pattern to match at least one or more spaces.


Compiling a regular expression so that you can use it by calling a variable:
regex = re.compile('\s+')
"""


# importing module for regular expressions
import re


"""
Common Regular Expressions
"""

# For each of these regex' - what does it do/print?
# Any character except for a new line
text = "Pythonkurs und Übung."
exit()
print(re.findall('.', text))  # .   Any one character except for a new line
print(re.findall('...', text))

# A period
exit()
print(re.findall('\.', text))  # matches a period
print(re.findall('[^\.]', text))  # matches anything but a period

# Any digit
exit()
text = '01, Jan 2015'
print(re.findall('\d+', text))  # \d  Any digit. The + mandates at least 1 digit.

# Anything but a digit
exit()
text = '01, Jan 2015'
print(re.findall('\D+', text))  # \D  Anything but a digit

# Any character, including digits
exit()
text = '01, Jan 2015'
print(re.findall('\w+', text))  # \w  Any character
exit()

# Anything but a character
exit()
text = '01, Jan 2015'
print(re.findall('\W+', text))  # \W  Anything but a character

# Collection of characters
exit()
text = '01, Jan 2015'
print(re.findall('[a-zA-Z]+', text))  # [] Matches any character inside

# Match something upto 'n' times
exit()
text = '01, Jan 2015'
print(re.findall('\d{4}', text))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', text))

# Match 1 or more occurrences
# This doesn't work, why? Suggestions?
exit()
print(re.findall(r'Hallo+', 'Ach, halloooo'))  # Match for 1 or more occurrences
# Solution:
#
#
#
# It's case sensitive, the follwing one does work
exit()
print(re.findall(r'hallo+', 'Ach, halloooo'))

# Match any number of occurrences (0 or more times)
exit()
print(re.findall(r'Pi*lani', 'Pilani'))
exit()

# Match exactly zero or one occurrence
exit()
print(re.findall(r'colou?r', 'color'))
exit()

# Match word boundaries
# Remember, word boundaries are marked with '\b'
# Example: You want to match the word in toy store, but not in Lew Tolstoy, which is a famous author
# Your turn, try to write a regex for this.
# Solution:
#
#
#
print(re.findall(r'\btoy\b.{6}', 'You want to match the word in toy store, but not in Lew Tolstoy, which is a famous author'))
# match toy with boundary on both sides, the ".{6}" is only used to show that we really matched "toy store"
exit()



"""
Slighty harder examples
"""
# Note: the spaces between the words are not of equal length
courses = """001 CL    Computational Linguistics
002 INF  Informatics
003 DH        Digital Humanities
004 TSDC Tim's Super Duper Class"""


# What is the difference between the next 2 print statements?
# What are the outputs?

simple_regex = re.compile('\s+')
print(simple_regex.split(courses))
print(re.split('\s+', courses))

# When to use which alternative:
# If you intend to use a particular pattern multiple times, then you are better off compiling a regular expression
# rather than using re.split over and over again.
exit()



"""
Different regex methods:
re.findall() -> The findall method extracts all occurrences of the given pattern from the text and returns them in a list.

re.search() vs. re.match() -> regex.search() searches for the pattern in a given text, but unlike findall() 
regex.search() returns a particular match object that contains the starting and ending positions of the first occurrence 
of the pattern.

regex.match() also returns a match object. But the difference is, it requires the pattern to be present at the beginning 
of the text itself.

re.sub() -> Replaces text
"""


"""Examples"""
print("{:-^200s}".format("Examples"))
"""
001 CL    Computational Linguistics
002 INF  Informatics
003 DH        Digital Humanities
004 TSDC Tim's Super Duper Class
"""
print(courses)
# What does the following regex do?
exit()
regex_num = re.compile('\d+')
print(regex_num.findall(courses))
#
#
# It compiles a regular expression, regex_num, which matches at least one decimal digit.
# What happens if we replace the '+' with '*'?
exit()
regex_num2 = re.compile('\d*')
print(regex_num2.findall(courses))
# Why is the output the way it is?
#
#
# The '*' matches 0 or many occurrences, since we try to match a digit with a letter we get an empty (0 matches) result
# which the '*' still keeps as an empty string
exit()



# Your turn:
# Syntax: re.sub(Pattern to find, Replacement for found pattern, String your are manipulating)
courses3 = """001 CL \t   Computational Linguistics
002 INF \t Informatics
003 DH    \t    Digital Humanities"""

print("courses3")
print(courses3)
print('----')

# This looks horrid, please replace all the unnecessary spaces with only one whitespace.
# You may use the information PyCharm gives (or other sources) when typing in your code to complete the task

# Solution:
#
#
#
regex = re.compile('[ \t\r\f]+')
print(regex.sub(' ', courses3))
# Why can't you use '\s+'?
# or
print(re.sub('[ \t\r\f]+', ' ', courses3))
print("")
exit()


# The output still looks confusing, to keep the newlines we use a negative lookahead (?!\n)
# It checks for an upcoming newline character and excludes it from the pattern.
# A wonderful example from the docs:
# (?!...) Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov)
# will match 'Isaac ' only if it’s not followed by 'Asimov'.

regex = re.compile(r'Isaac (?!Asimov)')
print(regex.findall("Isaac Asimov is one of the greatest sci-fi authors."))
print(regex.findall("The Binding of Isaac is a great game."))

print("Lookahead")
courses3 = """001 CL \t   Computational Linguistics
002 INF \t Informatics
003 DH    \t    Digital Humanities"""

# As long as the next character is not a newline it matches all whitespaces, which are then replaced with re.sub()
regex = re.compile('((?!\n)\s+)')

# What is the output?
exit()
print(regex.sub(' ', courses3))
exit()



"""
Regex Groups:
Regular expression groups are a very useful feature that lets you extract the desired match objects as individual items.

Suppose I want to extract the course number, code and the name as separate items. Without groups, I would have to write 
something like this:
"""

text = """002 INF  Informatics
001 CL    Computational Linguistics
000000003 DHU        Digital Humanities"""
#'''
# 1. What is the output?
exit()
print(re.findall('[0-9]+', text))


# 2. What is the output?
exit()
print(re.findall('[A-Z]{2,3}', text))

# 3. What is the output?
exit()
print(re.findall('[A-Za-z]{4,}', text))
# will look for upper and lower case alphabets a-z, assuming all course names will have at least 4 or more characters.

# 4. What is the output?
exit()
print(re.findall('[A-Za-z]{4,}\s*[A-Za-z]{4,}', text))
# Solution:
#
#
# will look for upper and lower case alphabets a-z, assuming all course names will have at least 4 or more characters AND
# include possible whitespaces, then will look again for upper and lower case alphabets a-z with at least 4 characters.

"""Excercise"""
print("Excercise")
"""
002 INF  Informatics
001 CL    Computational Linguistics
000000003 DHU        Digital Humanities
"""
# Instead of using 3 separate regexes, we can use a single one.
# Please try to write this regex. Hint: This regex will be used by re.findall() to find all occurences of the given pattern
# => [('002', 'INF', 'Informatics'), ('001', 'CL', 'Computational'), ('000000003', 'DHU', 'Digital')]
# Solution:
#
#
#
course_pattern = '([0-9]+)\s*([A-Z]{2,3})\s*([A-Za-z]{4,})'
print(re.findall(course_pattern, text))
exit()
#'''


"""
Greedy matching
Greedy matching is a regex' default behaviour, it tries to extract as much as possible until it conforms to a pattern 
even when a smaller part would have been syntactically sufficient. Think of it as "take it all".

Lazy matching 
Lazy matching is "take as little as possible". This can be effected by adding a '?' at the end of the pattern.
"""
#'''
# Greedy
# Instead of matching till the first occurrence of ‘>’ the regex matches the entire string
text = "<body>Regex Greedy Matching Example < /body>"
print(re.findall('<.*>', text))
exit()


# Lazy
# Note how many items are in the lists
# The regex matches the smallest possible match(es)
print(re.findall('<.*?>', text))
exit()


# What would you do if only the first match should be retrieved?
# Solution:
#
#
#
print(re.search('<.*?>', text).group())
exit()



"""
Grouping in a bit more detail
A group is created with round brackets (), the regular expression inside it determines what the group matches
"""
#'''
tel = '0176/123456789'
match = re.search(r'([\d\.-]+)'
                  r'(/)'
                  r'([\d\.-]+)'
                  , tel)
if tel:
    print("Match object:", match)
    print("Whole match:", match.group())
    print("Area code (group 1):", match.group(1))
    print("Delimiter (group 2):", match.group(2))
    print("Phone number (group 3):",  match.group(3))
exit()


# What do the following statements do?
courses2 = """CL    Computational Linguistics
002 INF  Informatics 003"""

regex_num3 = re.compile('\d+')
s = regex_num3.search(courses2)
exit()
# What are the 2 print outputs (roughly speaking)?
print('Starting Position: ', s.start())
print('End Position: ', s.end())
# This is a list slice with start and end positions as stated above
# What is the output?
exit()
print(courses2[s.start():s.end()])
exit()

# Using the group() method on the match object. See presentation page 25 and consult additional resources. group()
# is important.
# search() (our s defined above) returns a match object, group() extracts this object. search() only finds its
# first match ("002"), hence group() returns "002".
print(s.group())
exit()

# What is the output?
m = regex_num.match(courses2)
print(m)
exit()