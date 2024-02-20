
# A Sample class with init method
class tester:
 
    # init method or constructor
    def __init__(test, whacky):
        test.whacky = whacky
 
# Sample Method
    def say_hi(test):
        print('Hello, my name is', test.whacky)
 
 


# A Sample class with init method
class Class:
 
    # init method or constructor
    def __init__(self, id):
        self.guy = id
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.guy)
 
 
# Creating different objects
p1 = tester('Nikhil')
p2 = tester('Abhinav')
p3 = tester('Anshul')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()
