]#problem https://www.hackerrank.com/challenges/np-inner-and-outer/problem
import numpy
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(f'{numpy.inner(A, B)}\n{numpy.outer(A, B)}')     