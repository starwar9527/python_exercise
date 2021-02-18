import math


def q1():
    """
    Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    :return:
    """
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            print(num, end=',')
    print('\n')


def a1():
    """
    Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    :return:
    """
    l = []
    for num in range(2000, 3201):
        if (num % 7 == 0) and (num % 5 != 0):
            l.append(str(num))

    print(','.join(l))


def q2(num_list):
    """
    Question:
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320
    """
    result = []
    for num in num_list:
        value = 1
        for i in range(1, num + 1):
            value = value * i
        result.append(str(value))
    print(','.join(result))


def q3(num):
    """
    Question:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
    such that is an integral number between 1 and n (both included).
    and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    :return:
    """
    res = {}
    for i in range(1, num + 1):
        res[i] = i * i
    print(res)


def q4():
    """
    Question:
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
    which contains every number.

    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
    :return:
    """
    user_input = input("$:")
    alist = user_input.split(',')
    alist = list(alist)
    atuple = tuple(alist)
    print(alist)
    print(atuple)


# -------------------------------------------------------------------------------------------
class Q5Class:

    @staticmethod
    def get_string(prompt='$:'):
        return input(prompt)

    @staticmethod
    def print_string(string):
        print(string.upper())


def q5():
    """
    Question 5
    Level 1

    Question:
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    :return:
    """


# -------------------------------------------------------------------------------------------
def q6(l):
    """
    Question:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
    :return:
    """
    c = 50
    h = 30
    out = []
    input = l.split(',')
    for d in input:
        q = math.sqrt(2*c*int(d)/h)
        out.append(str(int(q)))
    print(','.join(out))


# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    q6('100,150,180')
