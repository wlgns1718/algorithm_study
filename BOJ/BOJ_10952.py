"""
 title: A+B-5
 level : Standard
 tag: implementation, arithmetic, math
 date:20230222
"""

import sys

input = sys.stdin.readline

while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)


