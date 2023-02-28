<<<<<<< HEAD
"""
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
dict1 = [1,2,3,4,5,5]
dict=[]


def Gbs(a,b):
    if a % b == 0:
        return b
    else:
        return Gbs(b,a%b)


list1 = [None]*8
list1.insert(0,1)
print(list1)
x = list1[0]
print(x,list1)
max = 10
x = 2
value = 3 if x != max else 0
value1 =4 if max == 10 else 0
def size(self):
    if self:
        return self.size()
    else:
        return 0


def solution(a, N):
    if a < 10:
        list1 = [int(i) for i in str(a)]
        list1.insert(0, 0)
        New = list1[0]+list1[1]
        New_list = [int(i) for i in str(New)]
        result = [list1[-1],New_list[-1]]
        return int(''.join(map(str,result))),N+1
    else:
        list1 = [int(i) for i in str(a)]
        New = list1[0] + list1[1]
        New_list = [int(i) for i in str(New)]
        result = [list1[-1], New_list[-1]]
        return int(''.join(map(str, result))), N+1
import sys

N = int(sys.stdin.readline())
table = [[0]*2 for _ in range(N)]
for i in range(N):
    str, end = map(int, sys.stdin.readline().split())
    table[i][0] = str
    table[i][1] = end
table.sort(key=lambda x:(x[1],x[0]))

cnt =1
end_time = table[0][1]
for i in range(1,N):
    if table[i][0] >= end_time:
        cnt += 1
        end_time = table[i][1]
print(cnt)


import sys
N = int(sys.stdin.readline())
count = 0
while N >= 0:
    if N % 5 ==0:
        count += int(N//5)
        print(count)
        break
    N -= 3
    count +=1
else:
    print(-1)
"""

'''
from collections import deque


def DFS(start, home, visit, res,first_start):
    result = 0
    temp = visit
    print(temp)
    temp_res = res
    if start == first_start:
        temp_res = 0

    temp_home = deque()
    for i in range(len(home)):
        next_home = home[i]
        temp_res += abs(start[0] - next_home[0]) + abs(start[1] - next_home[1])
        if temp_res > res:
            return
        temp.add((next_home[0], next_home[1]))
        for j in home:
            if (j[0], j[1]) not in temp:
                temp_home.append(j)
        if temp_home:
            DFS(next_home, temp_home, temp, temp_res,first_start)
        res = min(res,temp_res)

    return res


T = int(input())

for test_case in range(1, T):
    answer = float("INF")
    visit = set()
    n = int(input())
    arr = list(map(int, input().split()))
    home = [[x, y] for x, y in zip(arr[::2], arr[1::2])]
    start = home.pop(0)
    end = home.pop(0)
    visit.add((start[0], start[1]))
    print(visit)
    temp = deque()
    for i in home:
        if (i[0], i[1]) not in visit:
            temp.append(i)

    print(DFS(start, temp, visit, answer,start))
'''

"""
def DFS(start, end, home, visit,result):
    visit.append(start)
    for i in home:
        if i not in visit:
            temp = DFS(i,end,home,visit,result)

    if len(visit) == len(home):
        return abs(end[0]-visit[-1][0])+abs(end[1]-visit[-1][1]),visit.pop()
    else:
        cur = visit.pop()
        return abs(cur[0]-temp[1][0]) + abs(cur[1]-temp[1][1]) + temp[0],cur


T =int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    start = arr[:2]
    end = arr[2:4]
    home = [[x,y] for x,y in zip(arr[4::2],arr[5::2])]
"""
"""
from itertools import permutations


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    start = arr[:2]
    end = arr[2:4]
    home = [[x,y] for x,y in zip(arr[4::2],arr[5::2])]
    answer = []
    for temp in permutations(home,len(home)):
        res = 0
        res += abs(start[0]-temp[0][0])
        res += abs(start[1] - temp[0][1])
        for i in range(len(temp)-1):
            res += abs(temp[i][0]-temp[i+1][0])
            res += abs(temp[i][1] - temp[i+1][1])
        res += abs(temp[-1][0]-end[0])
        res += abs(temp[-1][1]-end[1])
        answer.append(res)
    print('#{0} {1}'.format(test_case,min(answer)))


from itertools import permutations

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    l = list(map(int,input().split()))

    company = (l[0],l[1])

    house = (l[2],l[3])

    l = l[4:]

    location = []

    for i in range(len(l)//2):
        temp = i*2
        location.append((l[temp],l[1+temp]))

    answer_list = []
    for temp in permutations(location,len(location)):
        answer = 0
        answer += abs(company[0] - temp[0][0])
        answer += abs(company[1] - temp[0][1])
        for k in range(len(temp)-1):
            answer += abs(temp[k][0] - temp[k+1][0])
            answer += abs(temp[k][1] - temp[k+1][1])
        answer += abs(house[0] - temp[-1][0])
        answer += abs(house[1] - temp[-1][1])
        answer_list.append(answer)

    # print(answer_list)
    answer = min(answer_list)
    print(f"#{tc} {answer}")


print('#{0} {1}'.format(di,a[-1]))
"""


"""
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            if (a+b+c == n):
                if(c >= b+2):
                    if(a%2==0):
                        answer += 1
print(answer)
"""

'''
from itertools import combinations
T = int(input())
x_list = []
y_list = []
answer = []
for _ in range(T):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
print(x_list,y_list)
for i in range(1,T+1):
    if i == 1:
        answer.append(0)
        continue
    all_case = combinations(range(T),i)
    x_temp = []
    y_temp = []
    temp = float("INF")
    for case in all_case:
        for c in case:
            x_temp.append(x_list[c])
            y_temp.append(y_list[c])
        x_temp.sort()
        y_temp.sort()
        x_mid = x_temp[i//2]
        y_mid = y_temp[i//2]
        sol = 0
        for idx in range(i):
            sol += abs(x_mid-x_temp[idx])
            sol += abs(y_mid-y_temp[idx])
        temp = min(temp,sol)
    print(temp)
'''
'''
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

pillar = [list(map(int,input().split())) for _ in range(n)]
pillar.sort(key=lambda x:x[0])
queue = deque()
queue.append(pillar[0])
answer = 0
h,w=0,0
for case in pillar[1:]:
    if case[1] <= queue[0][1]:
        queue.append(case)
    else:
        while queue:
            temp = queue.pop()
            w = temp[0]
            h = max(h,temp[1])
        answer += (case[0]- w)*h
        queue.append(case)
w,h = 0,0
while len(queue)>1:
    temp = queue.pop()
    h=max(h,temp[1])
    w=max(w,temp[0])
answer += h * (w-queue[0][0])
answer += queue[0][1]
print(answer)

'''
# T = int(input())
# row = [-1, -1, -1, 0, 0, 1, 1, 1]
# col = [-1, 0, 1, -1, 1, -1, 0, 1]
# sol = []
# trigger = 0
# for test_case in range(1,T+1):
#     m = int(input())
#     build = [list(map(str,input().split()))for _ in range(m)]
#
#     ans = 0
#     for i in range(m):
#         for j in range(m):
#             temp = 0
#             if build[i][j]=="G":
#                 temp =2
#             else:
#                 trigger =0
#                 for c in range(len(row)):
#                     new_row = i+row[c]
#                     new_col = j+col[c]
#                     if (new_row>=0 and new_col >=0 and new_row <m and new_col <m) and build[new_row][new_col] =="G":
#                         temp = 2
#                         trigger = 1
#                         break
#                 if trigger != 1:
#                     temp = 1
#                     new_row = i-1
#                     new_col = j-1
#                     while new_row>=0:
#                         if build[new_row][j] == "G":
#                             break
#                         new_row -= 1
#                         temp += 1
#
#                     while new_col >=0:
#                         if build[i][new_col] =="G":
#                             break
#                         new_col -= 1
#                         temp +=1
#
#                     new_row = i+1
#                     new_col = j+1
#                     while new_row < m:
#                         if build[new_row][j]=="G":
#                             break
#                         new_row +=1
#                         temp +=1
#
#                     while new_col < m:
#                         if build[i][new_col] =="G":
#                             break
#                         new_col +=1
#                         temp +=1
#
#             if temp>ans:
#                 ans = temp
#
#     sol.append(ans)
# print(sol)
'''
a는 물고기 번호 b는 방향 1 : 위 2: 왼위 3: 왼쪽 4: 왼아 5 : 아 6: 오아 7: 오 8: 오위 

for test_case in range(1,11):
    x,y = 0,-1
    dump = int(input())
    box = list(map(int,input().split()))
    new_box = [0] * 101
    for i in box:
        new_box[i] += 1
    for _ in range(dump):
        while new_box[x] == 0:
            x += 1
        while new_box[y] == 0:
            y -= 1
        if x> 100 or y < -101:
            break
        if x==(y+101) or x==(y+102):
            break
        new_box[y] -= 1
        new_box[y-1] += 1
        new_box[x] -= 1
        new_box[x+1] += 1
    if x != 100 and new_box[x]==0:
        x+= 1
    if y != -101 and new_box[y]==0:
        y -=1
    print("#{0} {1}".format(test_case,y-x+101))
'''


import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a,b = map(str,input().split())
    answer = ""
    for i in b:
        answer += i*int(a)
    print(answer)












=======
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
>>>>>>> b182ec4c42d69b3f74ac419ba90e2d939ef2ae21
