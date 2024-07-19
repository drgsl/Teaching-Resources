



if __name__ == '__main__':

    str1 = 'Hello'
    str2 = 'World'

    print(str1 + str2)  # HelloWorld
    print(str1 * 3)  # HelloHelloHello
    print(str1[1])  # e
    print(str1[1:3])  # el
    print('H' in str1)  # True
    print('H' not in str1)  # False
    print(r'\n')  # \n
    print('Hello \n World')  # Hello
                            # World
    print(str1 == str2)  # False
    var1 = 10
    var2 = 20

    print(f"{str1} {var1} {str2}") # Hello 10 World

    # print if the string is a number
    print(str1.isnumeric()) # False
    # print(var1.isnumeric()) # AttributeError: 'int' object has no attribute 'isnumeric'
    print(str(var1).isnumeric()) # True

    sentance = "Hello World How are you doing"

    print (sentance.split()) # ['Hello', 'World', 'How', 'are', 'you', 'doing']

    for word in sentance.split():
        print(word) 

    for word in sentance.split('o'):
        print(word)

    print(sentance.upper())
    print(sentance.lower())

    print(sentance.replace('o', '0'))

    print(sentance.startswith('Hello')) # True
    print(sentance.endswith('doing'))   # True

    print(sentance.find('World')) # 6

    print(sentance.count('o')) # 3

    


