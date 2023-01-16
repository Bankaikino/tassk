m = []
m2 = []
c = int(input())
for i in range(c):
    j1 = int(input())
    j2 = int(input())
    m.append(max(j1,j2))
    m2.append(min(j1,j2))
f = True
x = (m)
z = (m2)
if sum(x)%5!=0:
    print(sum(x))
    print("gg")
else:
    while f:
        for j in range(len(x)):
            x[j]=z[j]
            if sum(x)%5!=0:
                print(sum(x))
                print("gg")
                f = False
                break
        if f==True:
            print(0)
            break
            

# def f(n):
#     if n <=5:
#         return 2*n
#     if n%2==0:
#         return f(n-2) +3*f(n//2) + n
#     else:
#         return f(n-1)+f(n-2)+f(n-3)
#
# print(f(99)+f(100))
