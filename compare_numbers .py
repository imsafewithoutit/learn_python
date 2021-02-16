a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(a)
        print(c)
        print(b)
    if b < c:
        if a > c:
            print(a)
            print(b)
            print(c)
        else:
            print(c)
            print(b)
            print(a)
    if b == c:
        print(a)
        print(b)
        print(c)

elif a < b:
    if b < c:
        print(c)
        print(a)
        print(b)
    if b > c:
        if a < c:
            print(b)
            print(a)
            print(c)
        else:
            print(b)
            print(c)
            print(a)
    if b == c:
        print(b)
        print(a)
        print(c)

elif a == b:
    if b == c:
        print(a)
        print(b)
        print(c)
    if b > c:
        print(a)
        print(c)
        print(b)
    if b < c:
        print(c)
        print(a)
        print(b)
