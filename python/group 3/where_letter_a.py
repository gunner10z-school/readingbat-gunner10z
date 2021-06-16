# @desc Description of **where_letter_a**

def where_letter_a(word):
    for count,letter in enumerate(word):
        if letter=='a':
            return count
    return False
def main():
    print(where_letter_a('a'))
    print(where_letter_a(''))
    print(where_letter_a('Apple'))
    print(where_letter_a('orangutan'))
    print(where_letter_a('lamp'))
    print(where_letter_a('aaaaaaaaa'))


if __name__ == '__main__':
    main()