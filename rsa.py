import math
import sympy
import random

class RSA(object):

    def checkP(p):
        """
        Checks if parameter p is a prime number. If p is a prime number
        it returns True, otherwise it returns False.
        input: p must be an integer, otherwise "MUST INSERT INTEGER" statement
        is printed.
        """
        if type(p) != int:
            print("MUST INSERT INTEGER")
            return False
        if p == 1:
            return False
        if p == 2:
            return True

        for i in range(int(math.sqrt(p+2))):
            if p%(i+2) == 0:
                return False

        return True



    def getPrK(p,q):
        """
        Given parameters "p" and "q", if they are prime then 
        """
        if RSA.checkP(p)==False or RSA.checkP(q)==False:
            return("EITHER P OR Q NOT PRIME NUMBER")

        eList = []
        RSA.n = p*q
        RSA.phi = (p-1)*(q-1)
        for i in range (2,RSA.phi):
            if math.gcd(i, RSA.phi)==1:
                eList.append(i)
                #break
        RSA.e = eList[random.randint(0, len(eList)-1)]
        RSA.d = sympy.mod_inverse(RSA.e, RSA.phi)
        #print(eList)
        print("d: " +str(RSA.d))
        print ("phi(n): "+str(RSA.phi))
        print ("n: "+str(RSA.n))
        return((RSA.d,RSA.phi,RSA.n))


    def getPuK():
        print("e: " +str(RSA.e))
        print("n: " +str(RSA.n))
        return ((RSA.e, RSA.n))




def GCD(x , y):
    """This is used to calculate the GCD of the given two numbers.
    You remember the farm land problem where we need to find the
    largest , equal size , square plots of a given plot?"""
    if y == 0:
        return x
    r = int(x % y)
    return GCD(y , r)

    #def encrypt():
        #print("n: " +string(p*q)/ "phi(n): "+string((p-1)*(q-1)))


    #def decrypt():
        #print("n: " +string(p*q)/ "phi(n): "+string((p-1)*(q-1)))
