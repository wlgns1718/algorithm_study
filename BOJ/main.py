def sol(queue,answer,visit,b,cnt):
    while queue:
        idx = queue.popleft()
        for i in range(N + 1):
            if idx in answer[i] and i not in visit:
                queue.append(i)
                cnt += 1
                if b in answer[i]:
                    return cnt+1
                break
    return -1
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
answer = [[] for _ in range(N+1)]

a,b = map(int,input().split())
M = int(input())
dict = {i : [] for i in range(1,N+1)}
for _ in range(M):
    x,y = map(int,input().split())
    answer[x].append(y)
print(answer)
queue = deque();
visit = set()
cnt = 1
for i in range(N+1):
    if a in answer[i]:
        queue.append(i)
        visit.add(i)
        break

print(sol(queue,answer,visit,b,cnt))