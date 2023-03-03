"""
 title: 반복하지 않은 수
 level : Silver4
 tag: bruteforcing, implementation
 date:20230226
"""

import sys
input = sys.stdin.readline
idx = 0
count = 0
answer = [""]
while count<1000001:
    for i in range(10):
        if idx == 0 and i ==0:
            continue
        if str(i) not in answer[idx]:
            answer.append(answer[idx]+str(i))
            count+=1
    idx += 1
while True:
    N = int(input())
    if N ==0 :
        break
    print(int(answer[N]))