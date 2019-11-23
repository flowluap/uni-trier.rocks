"""Strings"""

name = 'Sarah'
vovels = ("a", "e", "i", "o", "u", "y") # including y

# Solution:

# a
print(name[4])
# b
print(name[len(name)-2]) 
# c
if (name[len(name)-1]=="h" and name[len(name)-2] in vovels):
    print("{0}: {1}".format(name,name[len(name)-2:]))
else:
    print(name)



"""Regular Expressions"""
import re


# Retrieve all the words starting with 'b' or 'B' from the following text.
text1 = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the 
bitter butter better."""
# Solution:
print(re.findall("[Bb]\w+", text1))

# RegEx Exercise 2
text2 = """Urbi@orbi.com
colin34@google.com
bArbArA87@amazon.com"""
# Solution
desired_output = []

for mail in text2.split("\n"):
    desired_output.append(tuple(re.split("[@|.]",mail)))
print(desired_output)

# RegEx Exercise 3
# Solution
text3 = """A, very   very; irregular_sentence, that only   occurs in       examples for students -or final tests"""
print(" ".join(re.findall("\S+",re.sub(",|;|-|_"," ",text3))))

# RegEx Exercise 4
# Note: The use of '^' and '$' is mandatory for both a) and b) (otherwise you would just be looking for 'ddd' and
# that's a bit too simple)
# a) Write a regex that returns all consecutive 'd' as a list => ['ddd']
# b) Write a regex that returns 'a' or 'ddd' (and only 3 'd' in a row) or 'g' or 'abcdefg' depending on the use
# of .group(0) to .group(3).

text4 = 'abcdddefg'


# Solution:



# RegEx Exercise 5 - difficult
print("{:-^200s}".format("RegEx Exercise 5"))
# a) Given the following 3 strings write a single (!) regex that returns
# ['defgabcd'] for text5_1 and text5_2 and
# ['cccdefgabcd'] for text5_3
# Hint: print("\143\141\160\164\165\162\145\40\147\162\157\165\160\40\141\156\144\40\154\157\157\153\55\141\150\145\141\144\163\40\50\47\77\47\51"
# b) Explain the steps how your regex works for text5_1

text5_1 = "abcdefgabcdefg"
text5_2 = "a1112221111cdefgabcdef12221111221g"
text5_3 = "abccccdefgabcdefgggg"


# Solution



# RegEx Exercise 6
print("{:-^200s}".format("RegEx Exercise 6"))
# Extract the show, title and air date.
# desired output = "'Star Trek- Voyager' Scorpion (TV Episode 1997)"
# Hint: You need to clean up the string, e.g. by replacing characters like "&quot;"
# Hint: "\120\162\145\163\145\156\164\141\164\151\157\156\40\160\141\147\145\40\62\65\40\55\40\147\162\157\165\160\50\51"
# The hint can be read if you print it like print("the octal string from above")

text6 = """<meta property='og:title' content="&quot;Star Trek: Voyager&quot; Scorpion (TV Episode 1997)" />"""

# Solution:



# RegEx Exercise 7
print("{:-^200s}".format("RegEx Exercise 7"))
# The following regex returns [('001', 'CL', 'Computational'), ('002', 'INF', 'Informatics'), ('003', 'DH', 'Digital')]
# Please write a regex that doesn't cut off the course names and also includes the entire courses 004 and 005
# Do not change the string in courses, the \t should be part of the resulting list item
# re.MULTILINE might come in handy.

courses = """001 CL    Computational Linguistics
002 INF  Informatics
003 DH        Digital Humanities
004    TSDC Tim's Super    Duper Class
005HTWP HowTo  \tWrite:   Python"""

course_pattern = re.compile(r'([0-9]+)\s+([A-Z]{2,3})\s+([A-Za-z]{4,})')
print(re.findall(course_pattern, courses))
# => [('001', 'CL', 'Computational'), ('002', 'INF', 'Informatics'), ('003', 'DH', 'Digital')]


# Solution:





# RegEx Exercise 8 (this one is meant as an exercise to understand the online python docs)
print("{:-^200s}".format("RegEx Exercise 8"))
# Clean up the following tweet, we only want the actual message. re.sub() is a good way to do this.
# Remove all hashtags, URLs, RTs, CCs and mentions.
# Remove punctuations -> hint: read re.escape (https://docs.python.org/3/library/re.html#re.escape) and string
# formatting %s, they do contain the solution
# Hint: re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
# Example: "Hello %s, my name is %s" % ('Bob', 'Tim') # => "Hello Bob, my name is Tim".
# http://www.diveintopython.net/native_data_types/formatting_strings.html
# Also interesting. https://realpython.com/python-f-strings/
# If you can't clean up the string with regular expressions use a different solution of your choice

# desired output = "Thank you very much Im learning to use Python and regexes to clean up strings Have a nice day"


tweet = """Thank you very much! RT @this_is_not_an_account: I'm learning to use Python and regexes to clean up strings 
http://t.co/lbghj0pzOd cc: @cldh_trier #python #regex Have a nice day"""


# Hint: Write a function/method that uses multiple regexes, if you don't know how to write a function simply print
# your regex output
# This function has to return something
# Call the function with print()
# Hint: Punctuation is contained in the string module and can be access via string.punctuation. You may use this
# instead of escaping punctuation characters by hand

# Solution





# RegEx Exercise 9
print("{:-^200s}".format("RegEx Exercise 9"))
# Extract all text portions between the tags from the following HTML page:
# https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# Hint: Uses requests module. If it's not installed you have to do that first.
# Optional: read the documentation on the requests module
# Since HTML is not absolutely standardized sometimes tags can be <body>...</body> or < body>...< /body>
# Write a regex that would work with both inputs
html_site = """
<HTML>
<HEAD>
    <TITLE>My Website</TITLE>
</HEAD>

<BODY>
    <HR>
    <a href="http://someurl.com">Some Link</a>
    <H1>This is a Header</H1>
    <H2>This is a Medium Header</H2>
    <P>This is a paragraph</P>
    <P>This is a another paragraph</P>
    <B>This is a new sentence without a paragraph break</B>
    <MARQUEE direction="down" width="250" height="200" behavior="alternate" style="border:solid">
        <MARQUEE behavior="alternate">
            This is some nonsense from the 90s and early 2000s, I'm glad it doesn't work in most browsers these days.
        </MARQUEE>
    </MARQUEE>

</BODY>
</HTML>
"""

desired_output = ["My Website", "Some Link", "This is a Header", "This is a Medium Header",
                  "This is a new paragraph", "This is a another paragraph",
                  "This is a new sentence without a paragraph break",
                  "This is some nonsense from the 90s and early 2000s, I'm glad it doesn't work in most browsers these days."]


# Solution:
#print(re.sub("[\n]"," ",html_site))
print(re.split("<[^>]*>", re.sub(" +"," ",re.sub("[\n]","",html_site))))

