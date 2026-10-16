"""SLICE THE BREAD"""
w, h, m, n = map(int, input().split())
x= [0]+list(map(int, input().split()))+[w]
y = [0]+list(map(int, input().split()))+[h]

X = []
for i in range(m+1):
    X.append(x[i+1] - x[i])
Y = []
for i in range(n+1):
    Y.append(y[i+1] - y[i])
X.sort(reverse=True)
Y.sort(reverse=True)
max1 = X[0]* Y[0]
max2 = max(X[1]*Y[0],X[0]*Y[1])
print(f"{max1} {max2}")
