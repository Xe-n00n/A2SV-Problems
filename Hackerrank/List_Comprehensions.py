def permutations(x, y, z):
    permutations=x*z*y
    results=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n:
                    results.append([i,j,k])

    return results

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    possibilities=permutations(x, y, z)
     
    print(possibilities)