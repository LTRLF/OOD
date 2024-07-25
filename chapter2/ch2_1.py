"""
จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

M=1000    CM=900    D=500    CD=400,

C=100    XC=90    L=50    XL=40,

X=10    IX=9    V=5    IV=4    I=1

เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

(https://roman-numerals.info/)
"""

x = []

class translator:
    def __init__(self):
        self.roman = []
        self.ans = 0

    def deciToRoman(self, num):
        self.num = num
        while num != 0:
            if num>999:
                self.roman.append("M")
                num = num-1000

            elif num>899:
                self.roman.append("CM")
                num = num-900

            elif num>499:
                self.roman.append("D")
                num = num-500

            elif num>399:
                self.roman.append("CD")
                num = num-400
            
            elif num>99:
                self.roman.append("C")
                num = num-100

            elif num>89:
                self.roman.append("XC")
                num = num-90
            
            elif num>49:
                self.roman.append("L")
                num = num-50

            elif num>39:
                self.roman.append("XL")
                num = num-40

            elif num>9:
                self.roman.append("X")
                num = num-10

            elif num>8:
                self.roman.append("IX")
                num = num-9

            elif num>4:
                self.roman.append("V")
                num = num-5

            elif num>3:
                self.roman.append("IV")
                num = num-4

            elif num>0:
                self.roman.append("I")
                num = num-1
        global x 
        x = self.roman
        return "".join(self.roman)
            
# CM CD C
    def RomanToDeci(self, s):
        for i in x:
            if i == "M":
                self.ans = self.ans + 1000
            elif i == "CM":
                self.ans+= 900
                
            elif i == "D":
                self.ans+= 500
            elif i == "CD":
                self.ans+= 400
            elif i == "C":
                self.ans+= 100
            elif i == "XC":
                self.ans+= 90
            elif i == "L":
                self.ans+= 50
            elif i == "XL":
                self.ans+= 40
            elif i == "X":
                self.ans+= 10
            elif i == "IX":
                self.ans+= 9
            elif i == "V":
                self.ans+= 5
            elif i == "IV":
                self.ans+= 4
            elif i == "I":
                self.ans+= 1

        return self.ans

            


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().RomanToDeci(translator().deciToRoman(num)))