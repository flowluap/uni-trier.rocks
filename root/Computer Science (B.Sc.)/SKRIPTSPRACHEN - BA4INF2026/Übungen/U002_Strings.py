"""Übung 001 | Sitzung 001 + 002"""
# I use a lot of exit(), the script stops once it reaches one that isn't part of a comment
# You can replace all "exit()" with "exit()" by pressing CTRL + R and use "Replace all"
# Please don't use "# exit()"
# The idea of this file is to give you some examples we can test and discuss in real time, so that you understand them
# and can use them and experiment with them at home.


"""Comments"""
# This is a single line comment that is ignored by the interpreter and doesn't allocate memory

"""This is
a
multiline
comment"""
# Strictly speaking this is WRONG. Stuff inside triple quotation marks is not ignored by the interpreter and does
# allocate memory until the garbage collection frees the memory again. This happens when the code is executed and the
# string isn't assigned to a variable.
# However, this is the way to document within code. When this multiline is placed immediately after a function or
# class definition or on top of a module, garbage collection will ignore it. Such a case is called docstring(s).


"""Python syntax and semantics by indentation"""
print("Python syntax and semantics by indentation")
# Sometimes it helps to think of indentation as "blocks".
# Block1
#   Block2
#       Block3
#   Block2 continuation
# Block1 continuation


# Initializing variable i -> we start at 0; initializing j -> we count to 10
i = 0
j = 10
print("Counting from", i + 1, "to 10")
# Alternative print, please note the extra whitespaces for formatting:
print("Counting from " + str(i + 1) + " to 10")

# Start of while
# We begin our while-loop. While our variable i is less than 10 we do:
while i < j:
    # ...add 1 to the starting number.
    i += 1
    # ..."say" the number we are at. See above where we initialized our variable -> we start at that number (0), add
    # 1 and THEN announce our number. This means we are announcing a 1, not a 0.
    print("Counting: ", i)
    # Once we reach number 5 we announce that we are half way done counting
    if i == 5:
        # This print belongs to the if-statement right above, this is how indentation in Python shows what part belongs
        # to what other part. You can visually see the hierarchy.
        print("Half way done counting")
    # Once we reach 10 we announce that we are done counting and exit our while-loop.
    # Notice: The elif-statement is part of the if-statement. This is where indentation might get confusing for
    # beginners. That is because some statements, like if, do have optional clauses, here elif, which are part of the
    # if-statement are are hence of the same hierarchy or block.
    elif i == 10:
        # This print belongs to the elif-statement.
        print("Done counting")
# End of While

# This print below is not part of the while-loop since it's not inside / nested in the block/hierarchy
# This print is used to print 3 empty lines to improve the readability of the print output
# Notice: We need to declare it a \n (newline, more later). If we leave the print with an empty string (print(""))
# it will print 3 empty strings, which are the same as 1 empty string, which results in a single empty line.
print("------------------------\n"*2)
# exit() stops the execution of the script, I use it here to end the script each time I want to explain something. It
# can also be used for quick troubleshooting.
# One can just use the single line comment (#) and go to the next part of the demonstration

#exit()


# The same while-loop as above without the comments for better visualization of the blocks:
# For this example we include the while-loop in a function
def count_to_ten(i):
    print("Starting with i =", i)
    while i < j:
        i += 1
        print("Counting: ", i)
        if i == 5:
            print("Half way done counting")
        elif i == 10:
            print("Done counting")
# Note: We call the function with parameter "0" to start counting from 0. We could use any other integer to start
# counting from there.
count_to_ten(0)
print("")
#exit()


# Question: What would happen if we used the following function calls at this point in the script:
print("Different calls")
print("Different calls: i")
count_to_ten(i)
# Answer:
#
#
#
# It depends on what our i is. We are overwriting our i constantly with a different integer. If we start with
# count_to_ten(0) and then call count_to_ten(i) the second call starts with i = 10 because count_to_ten(0) counted
# up to i = 10
print("")
#exit()

print("Different calls: -i")
count_to_ten(-i)
# If we then call count_to_ten(-i) we start at i = -10 and count from there. Of course our proclamation that i = 5 is
# the half way mark is now incorrect.
print("")
#exit()

print("Different calls: -1")
count_to_ten(-1)
# If we then call count_to_ten(-1) we start at i = -1 because we set i to -1 in the function call.
print("")

print("------------------------\n"*2)
#exit()



"""Multiline commands"""
print("Multiline commands")

# Please avoid doing this. Yes you can do it, but it's not nice to read.
a = 1; b = 2; print(a+b); print("These multiple commands in a single line aren't easy to read, are they?")
print("")

# The '\' is redundant between brackets, even if we use a multiline command
print(1 * 1 +
       2
       + 2)

# '\' is mandatory since we aren't using brackets, but spreading the command over multiple lines of code
erg = 1 * 1 +\
    2\
    + 2
print(erg)

# Multiple calls can be done within the same command, for readability I would suggest to turn it into a multiline
# command.
# The commands are carried out as "first in first out", meaning the first command within the brackets
# -> .replace("e", "a")
# Otherwise the print statement would print "Hallo Walt"
print("Hello World!"
      .replace("e", "a")
      .replace("or", "e")
      .replace("d", "t")
      )

print("------------------------\n"*2)
#exit()



"""Type Conversion / Type Casting"""
print("Type Conversion / Type Casting")

# Setting variables
my_int = 2
my_flo = 2.2
print("my_int =", my_int, "| my_flow =", my_flo)

# printing data type of set variables
print("data type of my_int:", type(my_int))
# => data type of my_int: <class 'int'>

print("data type of my_flo:", type(my_flo))
# => data type of my_flo: <class 'float'>

# adding int and float, printing data type of result
my_add = my_int + my_flo
print("data type of my_add:", type(my_add))
# => data type of my_add: <class 'float'>

# multiplying int and float, printing data type of result
my_mul= my_int * my_flo
print("data type of my_mul:", type(my_mul))
# => data type of my_mul: <class 'float'>

my_str = str(my_int)
print("data type of my_str:", type(my_str))
# => data type of my_str: <class 'str'>

# You can NOT add strings and integers
#my_inv = my_int + my_str
#print("data type of my_inv:", type(my_inv))
# => TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("------------------------\n"*2)
#exit()



"""Escape Sequences / Characters"""
print("Escape Sequences / Characters")
# Escape sequences are necessary since certain characters have a special meaning, e.g. the double quote opens and closes
# a string. But what about a string that contains a double quote that's not supposed to close the string (""")?
# We "escape" such a character that might be interpreted as an operator with a backslash, signaling that it is
# supposed to be interpreted as a string.

# Double quote (")
print("\"")
print("")

# Single quote (')
print('\'')
print('"')
print("")

# Backslash (\)
print("\\")
print("")
#exit()

# Backslash and newline ignored
print("line1 \
line2 \
line3")
print("")

# ASCII Bell (BEL) - if printed in a command prompt or shell: will ring an audible command tone. Does not work with the
# PyCharm command prompt
print("BEL (audible signal)")
print("\a")
print("")
# Use the command line or shell to run up to this point to hear the bell
#exit()

# ASCII Formfeed (FF)
# Advance downward to the next "page". It was commonly used as page separators, but now is also used as section
# separators
print("Formfeed")
print("Hello \f World!")
print("")

# ASCII Backspace (BS)
print("Backspace")
print("Hello \b World!")
print("")

# ASCII Carriage Return (CR)
# Return to the beginning of the current line without advancing downward
print("Carriage Return")
print("Hello \r World!")
print("")
#exit()

# ASCII Linefeed (LF)
# Linefeed means to advance downward to the next line
# Used as "newline", it terminates lines (commonly confused with separating lines)
# Important:
# The most common difference (and probably the only one worth worrying about) is lines end with CRLF on Windows,
# NL on Unix-likes. Note the shift in meaning from LF to NL, for the exact same character, gives the differences
# between Windows and Unix.
print("Linefeed aka newline")
print("Hello \n World!")
print("")

# ASCII Vertical Tab (VT)
print("Vertical Tab")
print("Hello \v World!")
print("")

# ASCII Horizontal Tab (TAB)
print("Horizontal Tab")
print("Hello \t World!")
print("")

# Octal value characters
# Note: This is how I will give you certain hints for your homework.
print("Octal value characters")
print("\110\145\154\154\157\40\127\157\162\154\144\41")
print("")

# Hex value characters
print("Hex value characters")
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
print("")

print("------------------------\n"*2)
#exit()



"""Raw text"""
print("Raw text")

# Text aligns at the word "care" to make the differences easily visible
# raw string, adding 2 double quotes would bne interpreted as closing the string and opening another
print(r"This is raw text, it doesn't care about special characters like \, \" or \\ ' or a \t tab or even quotation marks ''' ")
# normal string, adding 2 double quotes would bne interpreted as closing the string and opening another
print("This isn\'t raw text, it does care about special characters like \, \" or \\ ' or a \t tab or even quotation marks ''' ")
# multiline string (even if it is in fact just one line), adding 2 double quotes inside the string would interpreted
# as being part of the string
print("""This isn\'t raw text, it does care about special characters like \, \" or \\ ' or a \t tab or even quotation marks ''' """)

#exit()


# TODO HOMEWORK
# Try to understand why the following - all of them, even the ones that are line comments
print(r"") # ok, empty string
#print(r""") # not ok, odd number of quotation marks (1) inside
#print(r"""") # not ok, interpreted as turning the ) and the following characters into a string, despite an even number
# (2)
print(r"2""2") # ok, even number inside (2), basically (string open)2(string close)(string open)2(string close) => "22"
print("Hallo" "Welt") # same structure as above, different example
print(r"2""")
#print(r""""") # not ok, odd number of quotation marks (3) inside
#exit()

# Note: 3 quotation marks in a row are interpreted as a string with multiple lines, even if it only contains one line
# In multi-line string mode the interpreter halts the translation of the statement until it finds the closing triplet
# of the quotation mark. This enables us to include other quotation marks as long as they repeat less than 3 times.
print(r"""2""") # ok, even number inside (4)
#print(r""""""") # not ok, odd number of quotation marks (5) inside
print(r"""2""2""") # ok, even number inside (6)
print(r"2""2""2""") # ok, even number inside (6)
print(r"2""2""2""2") # ok, even number inside (6)
print(r"""""2""") # ok, even number inside (6)
# If you get strings with even more quotation marks, shoot the one responsible -_-
#exit()

# Possible solutions: Use the quotation mark that is not inside the string
print("Possible solution: Use the other quotation mark")
print(r'"')
print(r'""')
print(r'"""')
print(r'""""')
print(r'"""""')
# Possible solutions: Use escapes and not a raw string
print("Possible solution: Use escapes and not a raw string")
print("\"")
print("\"\"")
print("\"\"\"")
print("------------------------\n"*2)
#exit()



"""String Formatting with %"""
# Syntax: %[flags][width][.precision]type
print("String Formatting with %")

# Substitution
# %s = string
name = "Bob"
print("Hello %s" % name)
# => "Hello Bob"

course = "Python"
hours = 2
# %d = integer
print("Students have to attend the %s-course for %d hours/week." % (course, hours))
# => "Students have to attend the Python-course for 2 hours/week."
#exit()

# Substitution works for more than just strings - everything that has a string representation can be used for %s
a = 1 + 1
# [] = (empty) list
my_list = [course, 1, "hallo", a]
print("My list: %s" % my_list)
# => "My list: ['Python', 1, 'hallo', 2]"
#exit()

# Excercise: string formatting and flags
# Syntax: %[flags][width][.precision]type
# The float should be represented as an integer, with 3 preceding "0", use a flag
# %i = rounded integer
print("Excercise: string formatting and flags")
data = ("Rick", "Sanchez", 137, -70.2)
desired_output = "Hello Rick Sanchez, you are in universe C-137. You have last visited this universe -00070 days ago."
# Solution:
#
#
#
format_string = "Hello %s %s, you are in universe C-%d. You have last visited this universe %06i days ago."
print(format_string % data)
# => "Hello Rick Sanchez, you are in universe C-137. You have last visited this universe -00070 days ago."
#exit()

# Syntax: %[flags][width][.precision]type
# Flag: 0; width: 10/1/100; precision: 3 (=3 numbers after decimal); type: float; value
print("")
print("%10.3f more text"% (356.08977))
print("%-10.3f more text"% (356.08977))
print("%0100.3f more text"% (356.08977))
# Do you understand what's happening here?
print("------------------------\n"*2)
#exit()



"""String Formatting with format()"""
print("String Formatting with format()")
# Syntax: {}.format(value)

format_string2 = "Hello {} {}, you are in universe C-{}. You have last visited this universe {} days ago."
print(format_string2.format("Rick", "Sanchez", 137, -70.2))
# => "Hello Rick Sanchez, you are in universe C-137. You have last visited this universe -70.2 days ago."

# Changing the float to a rounded whole number
format_string2 = "Hello {:s} {:s}, you are in universe C-{:d}. You have last visited this universe {:.0f} days ago."
print(format_string2.format("Rick", "Sanchez", 137, -70.2))
#exit()

# Changing the order
format_string2 = "Hello {1:s} {0:s}, you are in universe C-{3:.0f}. You have last visited this universe {2:d} days ago."
print(format_string2.format("Rick", "Sanchez", 137, -70.2))
print("")
#exit()


# Spacing with formatting
print("Spacing with formatting")
# {:width} sets the minimum width a string will occupy. If the string is longer than the minimum it won't change the
# output.
print("{0:10}, is the computer-aided analysis of {1:20}, therefore you need to learn to program."
      .format("Computational Linguistics", "language"))

# Spacing with numeric types
print("This is universe C-{0:10}."
      .format(137))
#exit()

# Spacing with multiple types
# Note: This example makes the different treatment of strings and numbers more clear. Strings get the additional
# spaces on their right side, numbers on their left
print("This {0:40} is attended by {1:20} students."
      .format("Python course", 3))

# Spacing alignment
# There's more in the docs for even more formatting options
# <: left-align text in the field
# >: right-align text in the field
# ^: center text in the field
print("This {0:^40} is attended by {1:<20}!"
      .format("Python course", 3))

# Spacing alignment with filler (*), odd-numbered
print("{:*^20s}".format("Python course"))
print("------------------------\n"*2)
#exit()



"""String manipulation  - split() and join()"""
# You should now understand this print statement
print("{:-^200s}".format("String manipulation  - split() and join()"))

sj_str1 = r"This is an example string, it's only purpose is to illustrate split() and join() in Python. Well, right " \
         "now it's a bit too simple... Let's add some more characters like \n or \" ' maybe even some @ and {} to make " \
         "it a bit \"\"\" more: \n difficult \'\' for us ''"
sj_str2 = """This is an example string, it's only purpose is to illustrate split() and join() in Python. Well, right 
now it's a bit too simple... Let's add some more characters like \n or \" ' maybe even some @ and {} to make 
it a bit \"\"\" more: \n difficult \'\' for us ''"""
sj_str3 = r"""This is an example string, it's only purpose is to illustrate split() and join() in Python. Well, right 
now it's a bit too simple... Let's add some more characters like \n or \" ' maybe even some @ and {} to make 
it a bit \"\"\" more: \n difficult \'\' for us ''"""


# TODO HOMEWORK
# Please take note of how the strings in the output are quoted and try to understand the reasons for it
# Experiment a bit with quoting and splitting. I can't stress this enough, get some text and reconstruct why certain
# elements are in the resulting split-list.
# Try to understand the differences between sj_str1 to sj_str3 and their corresponding output from the following prints

print("Split")
# split() turns a string into a list with string elements. If no parameter is given split separates at every whitespace

# Split by whitespace. This includes the characters space, tab, linefeed/newline, return, formfeed, and vertical tab.
print(sj_str1.split())

# Split by parameter
print(sj_str1.split("\n"))
# Note: The lists might look different, especially after the "more characters like" part. Remember that Python does
# change the quotation mark and escapes automatically if needed for unambiguous strings. There is no additional \ before
# the (' maybe even some). It's just an escape added automatically.
#exit()

# Split and max split
# We split the first 5 times, getting 6 parts
# Note: In this example the (it's) is converted to (it\'s) because later on we have an escaped double quote etc.,
# which leads to some output problems.
print(sj_str1.split(" ", 5))

# Split into variables
print("Splitting strings directly into variables")
# Note: You have to assign a number of variables equal to the number of parts you get from split()
words_str = 'House,Mouse,Louse,Desoxyribonucleinacid'
a,b,c,d = words_str.split(",")
print("a =", a, "b =", b, "c =", c, "d =", d)
#exit()

# Join
print("Join")
# You can imagine join() as the opposite of split(), it creates a string from different elements
star_trek_series = ("Star Trek - The Original Series", "Star Trek - The Next Generation", "Star Trek - Deep Space 9",
                    "Star Trek - Voyager", "Star Trek - Enterprise", "Star Trek - Discovery")
star_trek_air_time_table = "\n  ".join(star_trek_series)
print("Series in order of air date:\n", star_trek_air_time_table)

print("------------------------\n"*2)
#exit()



"""Regular Expressions (RegEx)"""
print("{:-^200s}".format("Regular Expressions (RegEx)"))
# See different file
print("------------------------\n"*2)
#exit()



"""NLTK"""
print("{:-^200s}".format("NLTK - create your own corpus of english(!) files"))

# Creating a new corpus with NLTK
# Note: PlaintextCorpusReader only works with files in ENGLISH
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from pathlib import Path

# Setting paths
working_dir = Path.cwd()
print(working_dir)
star_trek_corpus_dir = working_dir / 'star_trek_corpus'
print("sta_trek_corpus_dir =", star_trek_corpus_dir)

# NLTKs PlaintextCorpusReader can't handle Path-objects, hence we convert it to a string
# PlaintextCorpusReader creates a corpus from given files

star_trek_corpus = PlaintextCorpusReader(str(star_trek_corpus_dir), '.*', encoding='latin1')
print(star_trek_corpus)

# List of all file names in the new corpus
print(star_trek_corpus.fileids())

# List of all words from all files
star_trek_words = star_trek_corpus.words()
print(star_trek_words)

# Now you can do the NLTK stuff
"""commenting this out, because it take quite a while to compute"""
"""
star_trek_corpus_len = len(star_trek_words)
print(star_trek_corpus_len)
star_trek_corpus_set = len(set(star_trek_words))
print(star_trek_corpus_set)
"""

# TODO ADVANCED HOMEWORK (optional)
# Removing digits and punctuation for a better FreqDist, because files contain subtitle timestamps
# Removing unwanted characters and digits is advanced stuff. If anyone wants to try it, be my guest.
# I think this will be covered in the course. If not and you want to do it send me an email.


# This converts all characters to lowercase so that "Phaser" and "phaser" are identical
# If you don't want that use: fdist1 = FreqDist(star_trek_words)
fdist1 = FreqDist([s.lower() for s in star_trek_words])
print(fdist1.most_common(50))
fdist1.plot(50, cumulative=True)

print("------------------------\n"*2)
exit()



"""Advanced stuff"""
"""String cleanup"""
print("{:-^200s}".format("Advanced stuff"))
print("{:-^200s}".format("String cleanup - practical tip, you don't have to understand the code yet"))
# Sometimes strings will include control characters (Steuerzeichen), which ruin the output, like:
messy_str = "\bS\x00t\n\rr\fi\xc3n\x05g"
print("String with control characters:")
print(messy_str)
cleaned = lambda s: "".join(i for i in s if 31 < ord(i) < 127)
print("Clean string:")
print(cleaned(messy_str))
print("------------------------\n"*2)
exit()