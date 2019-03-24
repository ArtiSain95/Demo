# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
#create fun
def SayHello(name):
    print("Hello" +name)

SayHello('Arti')

#return val
def getSum(num1,num2):
    total = num1+num2
    return  total
print(getSum(2,5))

def addOneNum(num):
    num = num +1
    return  num
print(addOneNum(3))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum1  = lambda num1,num2 : num1+num2
print(getSum1(2,5))