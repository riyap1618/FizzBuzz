# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
"""

# Press the green button in the gutter to run the script.
from math import floor

"""if __name__ == '__main__':
    print_hi('PyCharm')"""

def multipleOfY(x,y):
    return(x%y==0)

def reverse(str):
    length = len(str)
    num = floor(length/4)
    result = ''
    for i in range(0,num):
        end = length - i*4
        result += str[end - 4:end]
    return result

def processNumber(i,multipleOfThree, multipleOfFive,multipleOfSeven,multipleOfEleven,multipleOfThirteen,multipleOfSeventeen):
    result = ''
    if multipleOfY(i,3) & (multipleOfThree == 'True'):
        result += 'Fizz'
    if multipleOfY(i,13) & (multipleOfThirteen== 'True'):
        result += 'Fezz'
    if (multipleOfY(i,5)) & (multipleOfFive== 'True'):
        result += 'Buzz'
    if (multipleOfY(i,7)) & (multipleOfSeven== 'True'):
        result += 'Bang'

    if (multipleOfY(i,11)) & (multipleOfEleven== 'True'):
        if result != 'Fezz':
            result = ''
        result += 'Bong'

    if (multipleOfY(i,17)) & (multipleOfSeventeen== 'True'):
        result = reverse(result)

    if result == '':
        return i
    else:
        return result
    
def printUpToNum(x,multipleOfThree, multipleOfFive,multipleOfSeven,multipleOfEleven,multipleOfThirteen,multipleOfSeventeen):
    for i in range(1,x):
        result = processNumber(i,multipleOfThree, multipleOfFive,multipleOfSeven,multipleOfEleven,multipleOfThirteen,multipleOfSeventeen)
        print(result)

integer = input('What number do you want to print up to?')

multipleOfThree = input('Multiple of Three Rule? (True or False)')
multipleOfFive = input('Multiple of Five Rule? (True or False)')
multipleOfSeven = input('Multiple of Seven Rule? (True or False)')
multipleOfEleven = input('Multiple of Eleven Rule? (True or False)')
multipleOfThirteen = input('Multiple of Thirteen Rule? (True or False)')
multipleOfSeventeen = input('Multiple of Seventeen Rule? (True or False)')

printUpToNum(int(integer) + 1,multipleOfThree,multipleOfFive,multipleOfSeven,multipleOfEleven, multipleOfThirteen, multipleOfSeventeen)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
