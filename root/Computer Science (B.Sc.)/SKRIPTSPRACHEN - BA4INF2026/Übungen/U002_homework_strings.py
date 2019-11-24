#!/usr/bin/env python3

"""
Excercises

! Comment your code

NLTK
    1) (Try to) Create a corpus (of files in english!) of your own choosing. A single file is enough,
    use more if you want.
    2) How many token are in your corpus?
    3) How many types are in your corpus?
    4) At home: Experiment more with your corpus and the NLTK to get used to it. You may use the examples from
    presentation 02, you may consult the NLTK book/homepage and use their examples.
"""

author = "John Wyndham"

# name + year of publication
novel = ["The", "Day", "of", "the", "Triffids"]
date = 1951

quote01 = """I don't think it had ever occurred to me that man's supremacy is not primarily due to his brain, as most 
of the books would have one think. It is due to the brain's capacity to make use of the information conveyed to it 
by a narrow band of visible light rays. His CIVILIZATION, all that he had achieved or might achieve, hung upon his 
ability to perceive that range of vibrations from red to violet. Without that, he was lost."""

quote02 = """I don’t think we can blame anyone too much for the triffids. The extracts they give were very valuable in 
the circumstances. Nobody can ever see what a major discovery is going to lead to whether it is a new kind of engine 
or a triffid and we coped with them all right in normal conditions. We benefited quite a lot from them, as long 
as the conditions were to their disadvantage."""

# ############################ SOLUTIONS ############################

#1
print(len(author))

#2
print(author[0], author[:1], author[-len(author)])

#3
print(author[len(author)-1], author[len(author)-1:])

#4
print(author[2:len(author)-3])

#5
novel_name = ' '.join(novel)
print(novel_name)

for quote in (quote01, quote02):
    if 'civilization' in quote or 'CIVILIZATION' in quote :
        print('Bill Masen contemplates the civilization of man in quote{0}'.format("01" if quote == quote01 else "02"))
    else:
        print("Bill Masen doesn't contemplate the civilization of man in quote{0}".format("01" if quote == quote01 else "02"))
#6a
strange_string = "Publication: " +author+" - "+novel_name+" (published "+str(date)+")"
print(strange_string)
#6b
print("Publication: %s - %s (published %d)"%(author,novel_name,date))
print("Publication: {0} - {1} (published {2})".format(author,novel_name,date))

#6c whatever???
strange_string2 = "Publication: "
strange_string2 += author
strange_string2 += " - "
strange_string2 += novel_name
strange_string2 += " (published "
strange_string2 += str(date)
strange_string2 += ")"
print(strange_string2)

#7
print(quote01.split("."))
# str.split complements str.join. If you join the list w/o the empty string the last dot in the sentence would be missing.
