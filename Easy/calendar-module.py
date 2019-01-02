# problem: https://www.hackerrank.com/challenges/calendar-module/problem
from datetime import datetime 
m = '-'.join(input().split())
date = datetime.strptime(m, '%m-%d-%Y')
days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 
        3:'Thursday', 4:'Friday', 5:'Saturday',
        6:'Sunday'}
print(days[date.weekday()].upper())
