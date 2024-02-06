class Aktan:
    
    def getString(self):
        self.str = input()
    
    def printString(self):
        print(self.str.upper())

obj = Aktan()
obj.getString()
obj.printString()
