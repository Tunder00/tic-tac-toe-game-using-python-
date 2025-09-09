print("----------------")
print("tic tac toe")
print("----------------")

a=["","",""]
b=["","",""]
c=["","",""]
print("\n")
print("now game starts")
print(a)
print(b)
print(c)
while True:
    player = input("enter the choice x or o: ")
    row = int(input("row starts from 0,1,2...,enter row number: "))
    col = int(input("col starts from 0,,1,2...,enter col number: "))
    if player =='x' or player=='o':
        if row > 2 or col > 2:
            print("----------------------------------------------")
            print("enter a valid row or column number")
            print("row can have values 0 or 1 or 2")
            print("col can have values 0 or 1 or 2")
            print("----------------------------------------------")
        else:
            if row == 0:
                a[col] = player
            elif row == 1:
                b[col] = player
            elif row == 2:
                c[col] = player
            print(a)
            print(b)
            print(c)
            if ((a[0] == 'x' and a[1] == 'x' and a[2] == 'x') or
                    (b[0] == 'x' and b[1] == 'x' and b[2] == 'x') or
                    (c[0] == 'x' and c[1] == 'x' and c[2] == 'x') or
                    (a[0] == 'x' and b[0] == 'x' and c[0] == 'x') or
                    (a[1] == 'x' and b[1] == 'x' and c[1] == 'x') or
                    (a[2] == 'x' and b[2] == 'x' and c[2] == 'x') or
                    (a[0] == 'x' and b[1] == 'x' and c[2] == 'x') or
                    (a[2] == 'x' and b[1] == 'x' and c[0] == 'x')):
                print("-------")
                print("x wins")
                print("-------")
                break
            elif ((a[0] == 'o' and a[1] == 'o' and a[2] == 'o') or
                  (b[0] == 'o' and b[1] == 'o' and b[2] == 'o') or
                  (c[0] == 'o' and c[1] == 'o' and c[2] == 'o') or
                  (a[0] == 'o' and b[0] == 'o' and c[0] == 'o') or
                  (a[1] == 'o' and b[1] == 'o' and c[1] == 'o') or
                  (a[2] == 'o' and b[2] == 'o' and c[2] == 'o') or
                  (a[0] == 'o' and b[1] == 'o' and c[2] == 'o') or
                  (a[2] == 'o' and b[1] == 'o' and c[0] == 'o')):
                print("-------")
                print("o wins")
                print("-------")
                break
    else:
        print("----------------------------------------------")
        print("you have entered character other than x and o")
        print("----------------------------------------------")
