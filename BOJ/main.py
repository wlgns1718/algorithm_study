import sys

input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 0

string  = str(a*b)
for i in string[::-1]:
    if i =='0':
        cnt += 1
    else:
        break