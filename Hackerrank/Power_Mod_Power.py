
if __name__=='__main__':
    base = int(input())
    exponent = int(input())
    modular = int(input())
    result = pow(base, exponent)
    print(result)
    result_mod =result % modular
    print(result_mod)