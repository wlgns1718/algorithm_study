def sol(K,queue):
    visit = set()
    answer = []
    time = float("INF")
    while queue:
        cur = queue.popleft()
        visit.add(cur[0])
        print(visit)
        if cur[0] ==K:
            answer.append([cur])
            time = cur[1]
        else:
            if cur[0]+1 not in visit and cur[0]*2>=0 and cur[0]*2<=K and cur[1]<=time:
                queue.append([cur[0]+1,cur[1]+1])
            if cur[0]-1 not in visit and cur[0]*2>=0 and cur[0]*2<=K and cur[1]<=time:
                queue.append([cur[0]-1,cur[1]+1])
            if cur[0]*2 not in visit and cur[0]*2>=0 and cur[0]*2<=K and cur[1]<=time:
                queue.append([cur[0]*2,cur[1]+1])
        
    return answer

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())

queue = deque()
queue.append([N,0])

print(sol(K,queue))