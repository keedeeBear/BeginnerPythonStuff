'''hangman'''
import random
choices = ['hangman', 'welcoming', 'popeye', 'spinach', 'doorway', 'sweater', 'brilliant', 'lollipop', 'willow']
alfabet = "abcdefghijklmnopqrstuvwxyz"
v1 = []
word = random.randint(0, len(choices) - 1)
v2 = choices[word]
print "Hello. This is Hangman. You'll have a random word chosen for you, and you'll need to guess it."
print "You can input a letter by typing it like this: a (lowercase)"
print "Best of luck."
#print "Cheater code: "+v2
def isDone(v):
    for i in range(len(v)):
        if v[i] == '_':
            return 0
    return 1
def initEmpty(a, b):
    for i in range(len(a)):
        b.append('_')
def checkLetter(a, b, check):
    for i in range(len(a)):
        if a[i] == check:
            b[i] = check
def checkIfThere(a, check):
    for i in range(len(a)):
        if a[i] == check:
            return 1
    return 0
def printLeftOnes(v):
    for i in range(len(v)):
        print v[i],
nrMistakes = 0
initEmpty(v2, v1)
while nrMistakes < 5:
    printLeftOnes(v1)
    leddah = raw_input("What letter is your guess? ")
    if checkIfThere(v2, leddah) == 0:
        print "Wrong. ",
        nrMistakes += 1
    else:
        checkLetter(v2, v1, leddah)
        print "Good job. ",
    if isDone(v1) == 1:
        print "Congratulations! You've won."
        exit()
if nrMistakes == 5:
    print "You lost."
    exit()