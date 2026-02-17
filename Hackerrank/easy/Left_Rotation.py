def leftRotate(arr,d):
    array=arr[d:]+arr[:d]
    return array



if __name__ == "__main__":
    length,rotations = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*leftRotate(arr,rotations))