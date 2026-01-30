if __name__=="__main__":
    n=int(input())
    phonebook={}
    for i in range(n):
        name,number=input().split()
        phonebook[name]=number
    
    while True:
        try:
            request=input()
            if request in phonebook.keys():
                print(f'{request}={phonebook[request]}')

            else:
                print("Not found")
        except EOFError:
            break