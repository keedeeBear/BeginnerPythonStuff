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
    '''Print the cartesian form of the number'''
    def printCartesian(self):
        return "The number's real part is "+str(self.__r) + " and its imaginary part is "+ str(self.__i)