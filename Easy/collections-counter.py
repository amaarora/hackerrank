# Problem https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter 
X = int(input())
shoes = Counter([int(k) for k in (input().split())])
N = int(input())
amt = 0
for _ in range(N):
    m = [int(k) for k in (input().split())]
    size=m[0]
    value=m[1]
    if shoes[size]>0:
        amt+= value
        shoes[size]-=1
print(amt)    
