t = int(input())
N,E,H,A,B,C = list(map(int,input().split(' ')))
def minv(A, B):
    if(A < B):
        return A
    return B
    
def maxv(A, B):
    if(A > B):
        return A 
    return B 
    
for i in range(t):
    ans = res(N,E,H,A,B,C)
    if(ans == 1e15):
        print(-1)
    else:
        print(ans)
    
def res(N,E,H,A,B,C):
    if(N <= 0):
        return 0
    if((N <= E) and (N <= H)):
        ans = minv(ans, N * C)
    if(3 * N <= H):
        ans = minv(ans, N * B)
    if(2 * N <= E):
        ans = minv(ans, N * A)
    if(((H - N)/2 >= 1) and ((H - N)/2 >= N - E)):
        if(B - C >= 0):
            temp = minv(N -1,(H - N)/2)
            ans = minv(ans, (B - C) * temp + N * C)
        else:
            temp = maxv(1, N - E)
            ans = minv(ans, (B - C)* temp + N * C)
    if(E - N >= 1 and E - N >= N - H):
        if(A - C < 0):
            temp = minv(N - 1, E - N)
            ans = minv(ans, (A - C)*temp + N*C)
        else:
            temp = maxv(1, N - H)
            ans = minv(ans, (A - C)*temp + N*C)
    if((E/2 >= 1) and (E/2 >= (3*N - H + 2)/3)):
        if(A - B < 0):
            temp = minv(n-1, E/2)
            ans = minv(ans, (A - B)*temp + N*B)
        else:
            temp = maxv(1, (3*N - H + 2)/3)
            ans = minv(ans, (A - B)*temp + N*B)
    if((E >= 3) and (H >= 4) and (N >= 3)):
        ans = minv(ans, A + B + C + res(N - 3, E -3, H - 4, A, B, C))
    return ans
