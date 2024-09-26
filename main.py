def main():
    import random

    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    num3 = random.randint(0,100)

    print (num1)
    print (num2)
    print (num3)

    minval = num1
    # first assume for first number, to begin comparison --> initialize variable

    if num2 < minval:
        minval = num2
    else:
        if num3 < minval:
            minval = num3

    print(f'\n{minval} is the smallest number')
    

if __name__ == '__main__':
    main()