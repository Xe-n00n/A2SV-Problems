def is_even_dividable(weight):
    if weight % 2 == 0 and weight > 2:
        return "YES"
    else:
        return "NO"




if __name__ == "__main__":
    weight = int(input())
    print(is_even_dividable(weight))