T = int(input())
for _ in range(0,T):
    n,m = map(int,input().split())
    if n > m:
        print(n - m)
    else:
        print(0)
