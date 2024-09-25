def main():
    import random

    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    num3 = random.randint(0,100)

    print (num1)
    print (num2)
    print (num3)

    minval = num1
    # first assume for first number, to begin comparison

    if num2 < minval:
        minval = num2
        if num3 < minval:
            minval = num3
    else:
        minval
    print(f'\n{minval}')
    

if __name__ == '__main__':
    main()