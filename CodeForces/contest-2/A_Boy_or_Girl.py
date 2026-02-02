def boy_or_girl(name):
    name_set=set(name)
    if len(name_set)%2==0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
    

if __name__=="__main__":
    name=input()
    boy_or_girl(name)

