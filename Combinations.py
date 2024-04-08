def C(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return C(n-1, k) + C(n-1, k-1)
    else:
        return n

n,k = map(int, input().split())
if (1<=n<=10) and (0<=k<=10):
    print(C(n, k))
