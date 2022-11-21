#int -> int
#if number = even -> n / 2
#if number = odd -> 3n + 1
#return how many steps this application does

def collatz():
    num = int(input('Input an integer: '))
    count = 0
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
        count = count + 1
    else:
        print('Done!')
    print(count)


collatz()