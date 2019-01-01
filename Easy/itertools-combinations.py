#problem https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import combinations
s,n = input().split()
n = int(n)
for x in range(1,n+1):
    print(*[''.join(i) for i in combinations(sorted(s),x)],sep='\n')