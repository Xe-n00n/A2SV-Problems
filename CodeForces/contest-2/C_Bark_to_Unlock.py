def can_bark(passowrd,number_barks,barks):
    letter1=False
    letter2=False
    for bark in barks:
        if bark==password:
            letter1=True
            letter2=True
            break
        if bark[0]==passowrd[1]:
            letter2=True
        if bark[1]==password[0]:
            letter1=True
    if letter1 and letter2:
        print('YES')
    else:
        print('NO')


     

if __name__=="__main__":
    password=input()
    number_barks=int(input())
    barks=[]
    for _ in range(number_barks):
        barks.append(input())

    can_bark(password,number_barks,barks)
