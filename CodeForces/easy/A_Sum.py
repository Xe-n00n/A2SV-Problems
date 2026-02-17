def is_sum(a,b,c):
    if a+b == c or a+c == b or b+c == a:
        return "YES"
    return "NO"


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a,b,c = list(map(int, input().split()))
        print(is_sum(a,b,c))