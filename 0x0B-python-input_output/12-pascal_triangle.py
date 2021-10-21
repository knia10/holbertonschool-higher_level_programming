#!/usr/bin/python3
'''
Module 12-pascal_triangle
Has a function that returns a list
of lists of integers representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing the Pascal’s triangle
    Returns an empty list if n <= 0
    '''
    if n <= 0:
        return []
    #l_int = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if(j < i):
                if (j == 0):
                    pascal_triangle.append(1)
                else:
                    pascal_triangle[i].append(pascal_triangle[i-1][j]+[i-1][j-1])
            elif(j == i):
                pascal_triangle[i].append(1)
