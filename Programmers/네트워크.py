"""
"""
"""
 title: 네트워크
 level : Level3
 tag: DFS, BFS
 date:20230211
"""


def DFS(i, computers, temp, length):
    temp.add(i)
    for com in range(length):
        if com in temp:
            continue
        if com != i and computers[i][com] == 1:
            DFS(com, computers, temp, length)

    return temp


def solution(n, computers):
    answer = 0
    length = len(computers)
    link = []
    visit = set()
    for i in range(length):
        temp = set()
        if i in visit:
            continue
        update = DFS(i, computers, temp, length)
        link.append(update)
        visit.update(update)

    return len(link)
