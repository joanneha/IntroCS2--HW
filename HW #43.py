# Team Paradoxical -- Joanne Ha, Clio Chen
# IntroCS2 pd. 08
# HW #43: ASCIIing About Your Visage
# 2015-04-29

# Part A
# 1. common(L1, L2) takes 2 lists as input and returns a new list containing values common to both.

def common(L1, L2):
    retL = []
    for i in L1:
        if i in L2:
            retL += [i]
    return retL

# Diagnostics
x = [1,5,4,3,2]
h = [4,5,10,15]
print common(x,h) #...[4,5]


# 2. alphabetize(names) takes a string of names, assumed to be in Last-First
# pairings, separated by commas, and returns an alphabetized list of
# names with line breaks in string form. Summarize algorithm in block comment

'''
ALGO:

    1. Turn input string into list called "listed". 
    2. Create a new list in which each element is the first AND last name of a person.
    For example, listed would contain something like "Joanne,Ha". In this newlist, I want
    "Joanne Ha" as a single entity.
        - This can be achieved by using a while loop and using a ctr that adds 2 each time
    3. Return the string version of the newlist.
'''

def alphabetize(names):
    listed = names.split(",")
    newlist = []
    ctr = 0
    while ctr < len(listed)-1:
        i = listed[ctr]
        appending = i + " " + listed[ctr+1] + "\n"
        newlist.append(appending)
        ctr += 2
    return "".join(sorted(newlist))

# Diagnostics
print alphabetize("Wayne,Bruce,Kent,Clark,Parker,Peter") #...Kent Clark\nParker Peter\nWayne Bruce
print alphabetize("Tara,Banks,Beyonce,Knowles,Alan,Turing,Amelia,Earhart") #...Alan Turing\nAmelia Earhart\Beyonce Knowles\nTara Banks
