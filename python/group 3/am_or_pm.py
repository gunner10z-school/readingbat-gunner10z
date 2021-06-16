# @desc Description of **am_or_pm.py**

def exponents(time):
    if time<13:
        return ('AM')
    else:
        return ('PM')

def main():
    print(exponents(7))
    print(exponents(0))
    print(exponents(13))
    print(exponents(17))
    print(exponents(24))
    print(exponents(12.5))


if __name__ == '__main__':
    main()