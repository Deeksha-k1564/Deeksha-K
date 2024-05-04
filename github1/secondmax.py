if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    lt = sorted(arr, reverse=True)
    print(lt[1])