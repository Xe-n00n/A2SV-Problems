
if __name__ == "__main__":
    k,w,n=map(int,input().split())
    total_cost = 0 
    # arithmetic progression sum formula: n/2 * (first_term + last_term)
    total_cost = k*n*(n+1)//2 
    print(max(0,int(total_cost-w)))