#!/usr/bin/python3
'''Module'''


def pascal_triangle(n):
    """Pascal triangle implementation
    Check README.md file for full documentatio and algorithm"""
    if n <= 0:  # if n is less than or eqaul to 0
        return []   # Return empty list

    # Empty sublists of nth length
    lpd = [[] for _ in range(n)]

    for i in range(n):
        lpd[i].append(1)
        for j in range(i-1):
            lpd[i].append(lpd[i-1][j] + lpd[i-1][j+1])
        if i > 0:
            lpd[i].append(1)
    return lpd
