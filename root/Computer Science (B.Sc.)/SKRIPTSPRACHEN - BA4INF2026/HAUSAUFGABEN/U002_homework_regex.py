"""Regular Expressions"""
import re

# RegEx Exercise 1
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
print(re.sub("\s+"," ",re.sub(",|;|-|_"," ",text3)))


# RegEx Exercise 4
text4 = 'abcdddefg'
# a:
#print(re.findall("[d\1+]{3,}",text4)) seems way more elegant
print(re.findall("[d^d$d]{3,}",text4))

#b
#Need for search to be able to group syntax like (^a)|([d^d$d]{3,})|($g)|(^.*[a-z].*$) wont work...
match = re.findall("^a|[d^d$d]{3,}|g$",text4)
print(match)


# RegEx Exercise 5 - difficult
text5_1 = "abcdefgabcdefg"
text5_2 = "a1112221111cdefgabcdef12221111221g"
text5_3 = "abccccdefgabcdefgggg"

print(re.search("(^a.*?c)(.*)(def.*g)",text5_2).group(2))
"""
Step 1: Check what the strings have in common:
    They have a delimiting start - and ending group.
    a*c - string we want - def*g
Step 2 Regex: Working with groups we want a*c and def*g to be a group so that the string in the middle 
    can be isolated. so the string in the center also needs to be a seperate group --> (.*)
    We know both strings begin with a and the something till we reach a "c" --> ^a.*?c group it --> (^a.*?c) 
    
    Last step is to isolate the last group. Steps like for the beginning string: 
    it starts with def*g --> def.*g grouping --> (def.*g) 
    
    You could somehow for sure work with $ in the end but it kinda works like this.
     
"""
print(re.search("(^a.*?c)(.*)(ef.*g)",text5_3).group(2))


# RegEx Exercise 6
text6 = """<meta property='og:title' content="&quot;Star Trek: Voyager&quot; Scorpion (TV Episode 1997)" />"""
# Solution:
print(re.sub('^.*?="&quot;|" />|&quot;',"",text6))


# RegEx Exercise 7
courses = """001 CL    Computational Linguistics
002 INF  Informatics
003 DH        Digital Humanities
004    TSDC Tim's Super    Duper Class
005HTWP HowTo  \tWrite:   Python"""

course_pattern = re.compile(r'([0-9]+)\s*([A-Z]{2,5})\s+([A-Za-z].*)', re.MULTILINE)
print(re.findall(course_pattern, courses))

# RegEx Exercise 8
tweet = """Thank you very much! RT @this_is_not_an_account: I'm learning to use Python and regexes to clean up strings
http://t.co/lbghj0pzOd cc: @cldh_trier #python #regex Have a nice day"""

# Solution
def cleanup(st):
    urls = r'(http|https)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?' #notbyme
    hashtags = r'\#[a-zA-Z]+\b'
    mention = r'@([A-Za-z0-9-_]+)'
    rt_cc = r'cc:|CC:|cC:|Cc:|RT|rt|rT|Rt' #not sure if we need all those but anyways
    sp_chars = r':|!'
    all_regex = re.compile("(%s|%s|%s|%s|%s)" % (urls,hashtags,mention,rt_cc,sp_chars)) #id that the kind of re.escape???

    return re.sub("\s+", " ",re.sub(all_regex,"",st))

print(cleanup(tweet))

# RegEx Exercise 9
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
# Solution:
#is there a neater way to remove empty string from the array?
#probably using another re moethod?
html = re.compile('\s*<.*?>\s*')
print(list(filter(None,re.split(html,html_site))))
