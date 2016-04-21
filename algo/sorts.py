#! /usr/bin/python
import random

def quicksort(input, lo, hi):
    if lo < hi:
        pivot, i = input[hi], lo;
        for j in range(lo, hi):
            if input[j] > pivot:
                input[i], input[j] = input[j], input[i]
                i = i+1
        input[hi], input[i] = input[i], input[hi]
        quicksort(input, lo, i-1)
        quicksort(input, i+1, hi)
    return input

def merge(a, b):
    c= []
    i, j = 0, 0
    while 1:
        if a[i] > b[j]:
            c.append(b[j])
            j = j + 1
            if j == len(b):
                break
        else:
            c.append(a[i])
            i = i + 1
            if i == len(a):
                break
    if i<len(a):
        for e in range(i, len(a)):
            c.append(a[e])
    if j<len(b):
        for f in range(j, len(b)):
            c.append(b[f])
    return c


def mergesort(input, lo, hi):
    if hi != lo:
        mid = (lo+hi) / 2
        a = mergesort(input, lo, mid)
        b = mergesort(input, mid+1, hi)
        c = merge(a, b)
        return c 
    else:
        return [input[lo]] 


if __name__ == "__main__":
    input = random.sample(xrange(100), 100)
    print input
    print quicksort(input, 0, len(input)-1)
    print mergesort(input, 0, len(input)-1)

