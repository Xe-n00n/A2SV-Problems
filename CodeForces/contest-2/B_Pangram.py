def is_pangram(word_len,word):
    
    word_set=set(word.lower())
    if len(word_set)==26:
        print('YES')
    else:
        print('NO')


     

if __name__=="__main__":
    word_len=int(input())
    word=input()
    is_pangram(word_len,word)

