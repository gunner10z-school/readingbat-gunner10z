# @desc Description of **first_and_last.py**

def greater_than_less_than(s):
    if s>10 and s<20:
        return True
    else:
        return False

def main():
    print(greater_than_less_than(5))
    print(greater_than_less_than(0))
    print(greater_than_less_than(13))
    print(greater_than_less_than(10.5))
    print(greater_than_less_than(20.5))


if __name__ == '__main__':
    main()