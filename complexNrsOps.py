import math
class nrComplex:
    '''init'''
    def __init__(self, reeal, imm):
        self.__r = reeal
        self.__i = imm
    '''getters'''
    def getReal(self):
        return self.__r
    def getImm(self):
        return self.__i
    '''setters'''
    def setReal(self, newR):
        self.__r = newR
    def setImm(self, newI):
        self.__i = newI
    def printResult(self):
        return "The result has the following form: c = "+str(self.__r)+" + "+str(self.__i)+"i."
    '''simple operations with one complex number'''
    def printCartesian(self):
        return "The number's real part is "+str(self.__r) + " and its imaginary part is "+ str(self.__i)
    
    def printConjugate(self):
        return "The conjugate has its real part of "+str(self.__r)+" and its imaginary part is -"+str(self.__i)
    
    def printPolar(self):
        m = math.sqrt(self.__r* self.__r + self.__i*self.__i) #modulus of the number
        cosphi = self.__r / m
        sinphi = self.__i/m
        return "The number's polar form is the following: c = "+str(m)+"("+str(cosphi)+" + "+str(sinphi)+"i)."
    def multiplyByReal(self, reCoeff):
        self.__r = self.__r * reCoeff
        nrComplex.printResult(self)
    def multiplyByIm(self, imCoeff):
        self.__i = self.__i * imCoeff
        nrComplex.printResult(self)
    '''operations with two complex numbers'''
    def addTwo(self, other):
        self.__r = self.__r + other.__r
        self.__i = self.__i + other.__i
        nrComplex.printResult(self)
    def multiplyTwo(self, other):
        self.__r = self.__r * other.__r - self.__i * other.__i
        self.__i = self.__r * other.__i + self.__i * other.__r
        nrComplex.printResult(self)
    '''complex operations with one complex number'''
    def matrixForm(self):
        #mat = [[self.__r, -self.__i], [self.__i, self.__a]]
        return str(self.__r)+' -'+str(self.__i)+'\n'+str(self.__i)+' '+str(self.__r)
    def powNumber(self, newPow):
        while newPow > 0:
            nrComplex.multiplyTwo(self, self)
        return nrComplex.printResult(self)
    def sqrtNumber(self):
        m = math.sqrt(self.__r* self.__r + self.__i*self.__i) #modulus of the number
        phi = math.atan(self.__i/self.__r)*180/math.pi
        m = math.sqrt(m)
        return "The result is c = "+str(m)+"(cos("+str(phi/2)+") + isin("+str(phi/2)+"))."
    def expNumber(self):
        #e^(a + ib) = e^a* (e^ib)
        #e^ib = cosb + isinb
        self.__r = math.exp(self.__r)*math.cos(self.__i)
        self.__i = math.exp(self.__r)*math.sin(self.__i)
        nrComplex.printResult(self)
'''UI'''
print "Hi! Thanks for dropping by. Here you'll be able to do a lot of stuff with, you guessed it, complex numbers!"
print "You'll need to press the following numbers for their corresponding actions:"
print "1 - See the Cartesian form of the number you input!\t\t\t2 - See the Conjugate of the number you input!"
print "3 - See the Polar form of the number you input!\t\t\t\t4 - Multiply your number by a real number!"
print "5 - Multiply your number with a imaginary number!\t\t\t6 - Add two complex numbers!"
print "7 - Multiply two complex numbers!\t\t\t\t\t8 - See a number in its matrix form!"
print "9 - See the number you input to a power n!\t\t\t\t10 - See the square root of the number you input!"
print "11 - See the exponential of the number you input!"
print "If you don't want to do one of the beforementioned actions, feel free to press 0. Have fun!"
a = int(raw_input("Please input the real part of the number!"))
b = int(raw_input("Please input the imaginary part of the number!"))
numar = nrComplex(a, b)
while 1:
    choice = int(raw_input("So, what do you want to do?"))
    if choice == 1:
        print nrComplex.printCartesian(numar)
    elif choice == 2:
        print nrComplex.printConjugate(numar)
    elif choice == 3:
        print nrComplex.printPolar(numar)
    elif choice == 4:
        reAl = int(raw_input("Hi! Please input the real number!"))
        print nrComplex.multiplyByReal(numar, reAl)
    elif choice == 5:
        imAg = int(raw_input("Hi! Please input the imaginary coefficient!"))
        print nrComplex.multiplyByIm(numar, imAg)
    elif choice == 6:
        c = int(raw_input("Hi! Please input the real part of the second number!"))
        d = int(raw_input("Hi! Please input the imaginary coefficient of the second number!"))
        numarDoi = nrComplex(c, d)
        print nrComplex.addTwo(numar, numarDoi)
    elif choice == 7:
        c = int(raw_input("Hi! Please input the real part of the second number!"))
        d = int(raw_input("Hi! Please input the imaginary coefficient of the second number!"))
        numarDoi = nrComplex(c, d)
        print nrComplex.multiplyTwo(numar, numarDoi)
    elif choice == 8:
        print nrComplex.matrixForm(numar)
    elif choice == 9:
        putere = int(raw_input("Hi! To what power do you want to raise the complex number?"))
        print nrComplex.powNumber(numar, putere)
    elif choice == 10:
        print nrComplex.sqrtNumber(numar)
    elif choice == 11:
        print nrComplex.expNumber(numar)
    elif choice == 0:
        print "See you soon!"
        exit()
    else:
        print "Please input a number between 0 and 11!"