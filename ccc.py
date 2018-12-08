import string
fisier1 = open("level1-1.in", "r")

'''print fisier1.readline()'''

stars = string.split(fisier1.readline(), " ")
lightWave = []
lastvalue = stars[3]
k = 0
toP = stars[1]
def isnum(s):
    try:
        float(s)
    except:
        return(False)
    else:
        return(True)
    
'''print toP,'''
lastPrint = toP
solarFlare = 0
transit = 0
events = []
lightWave.append(stars[1])
for i in range(3, len(stars)):
    if isnum(stars[i-1]) == False:
        lastvalue = stars[i+1]
    elif stars[i] == lastvalue :
        k += 1
    elif stars[i] != lastvalue:
        lightWave.append(lastvalue)
        lightWave.append(k)
        k = 0
        if isnum(stars[i]) == True:
            lastvalue = stars[i]
            k=1
    if isnum(stars[i]) == False:
        lightWave.append(stars[i])
ok = 0
events.append(lightWave[0])
solarFlare=0
print lightWave[0],
for i in range(len(lightWave)):   
    if isnum(lightWave[i]) == True:
        ok = 1
        try:
            if int(lightWave[i]) > 1000000 and isnum(lightWave[i]) == True:
                solarFlare += 1

            elif int(lightWave[i]) <= 995000 and int(lightWave[i]) > 500 and int(lightWave[i+1]) >= 5 and int(lightWave[i+1]) <= 15:
                transit+= 1
        except:
            pass
    else:
        if (ok == 1):
            if transit >= 3:
                print "YES",lightWave[i],
            else:
                print "NO",lightWave[i],
            events.append(solarFlare)
            events.append(transit)
            events.append(lightWave[i])
            solarFlare = 0 
            transit = 0
'''for i in lightWave:
    print i,
'''
print '\n'


for i in lightWave:
    print i,


