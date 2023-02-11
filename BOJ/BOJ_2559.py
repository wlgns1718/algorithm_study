"""
"""
"""
 title: 수열
 level : Silver3
 tag: prefix_sum, sliding_window, two_pointer
 date:20230211
"""


import sys
input = sys.stdin.readline

answer = 0
N,K = map(int,input().split())
num_list = list(map(int,input().split()))
prefix = [num_list[0]]
for i in range(1,N):
    prefix.append(prefix[i-1]+num_list[i])
answer = prefix[K-1]
for i in range(K,N):
    temp = prefix[i]-prefix[i-K]
    if(answer < temp):
        answer = temp
print(answer)