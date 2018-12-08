nrStrikes = 0
v = []
score = []
scoreRound = 0
pas = 1
nrRounds = int(raw_input("Number of rounds, please: "))
print "Press a # > 10 when you wish to finish."
while 1:
    pinsDown = int(raw_input("Pins: "))
    if (pinsDown > 10):
        break
    v.append(pinsDown)
print "All the pins you brought down are "
for i in range(len(v)):
    print (str)(v[i]),
for i in range(len(v)):
    try:
        if v[i] + v[i+1] == 10:
            print "The value of current i is "+str(v[i])+" and o next i is "+str(v[i+1])
            print "You have made a spare. You will have an extra of "+str(v[i+2])+" points."
            scoreRound = v[i] + v[i + 1] + v[i + 2]
    except:
        pass
    if v[i] == 10 and i <= len(v) - 2:
        print "The value of current i is "
        bonus = v[i + 1] + v[i + 2]
        print "You have made a strike. You will have an extra of"+str(bonus)+" points."
        scoreRound = v[i] + bonus
        pas = 0
    elif i <= len(v) - 1:
        print "Current i is "+str(v[i])+" and of next i is "+str(v[i + 1])
        scoreRound = v[i] + v[i + 1]
    if pas != 0:
        i += 1
        score.append(scoreRound)
        print "This round's score is "+str(scoreRound)
for i in range(len(score)):
    print score[i],