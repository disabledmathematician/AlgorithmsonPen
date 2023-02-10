# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:51:16 2023

@author: Charles_Truscott
"""


def three_swap(L):
    pass
def Charles(L):
    i, j, k = 1, 0, 0
    temp = 0
    while(i <= (len(L) - 1) and j <= (len(L) - 1)):
        t1 = L[j]
        t2 = L[i]
        L[j] = t2
        L[i] = t1
        print(L, j, i)
        R = L.copy()
        for x in range(1, len(L)):
            if x != i:
                s1 = R[j]
                s2 = R[x]
                R[j] = s2
                R[x] = s1
                print(R, x, i, j)
                
        i += 1
        j += 1
L = [1, 2, 3, 4, 5]
if __name__ == "__main__": Charles(L)