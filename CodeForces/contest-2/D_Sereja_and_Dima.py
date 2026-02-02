def who_wins(number_cards,cards):
    sereja=0
    dima=0
    turn=0 
    # even turns are for Sereja, odds are for Dima
    for i in range(number_cards):
        picked_card=0
        if cards[0]>cards[-1]:
            picked_card=cards[0]
            cards.pop(0)
        
        else:
            picked_card=cards[-1]
            cards.pop(-1)


        if turn%2==0:
            sereja+=picked_card
        else:
            dima+=picked_card
        
        turn+=1

    print(f'{sereja} {dima}')

     

if __name__=="__main__":
    number_cards=int(input())
    cards=input().split(' ')
    int_cards = list(map(int, cards))
    who_wins(number_cards,int_cards)
