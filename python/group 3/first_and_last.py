# @desc Description of **first_and_last.py**

def first_and_last(s):
    if s[0]==s[-1]:
        return True
    else:
        return False


def main():
    print(first_and_last('abab'))
    print(first_and_last('abba'))
    print(first_and_last(''))
    print(first_and_last('123'))
    print(first_and_last('6796'))


if __name__ == '__main__':
    main()
