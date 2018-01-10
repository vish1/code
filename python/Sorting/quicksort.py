import random

def sift_down(numbers, start, len):
    root = start
    swap = root
    while root*2 <= len:
        if numbers[root*2 - 1] > numbers[root - 1]:
            swap = root*2
        if root*2 +1 <= len and numbers[root*2 + 1 - 1] > numbers[swap - 1]:
            swap = root*2 + 1
        if swap == root:
            return
        else:
            numbers[swap-1], numbers[root-1] = numbers[root-1], numbers[swap-1]
            root = swap

def max_heapify(numbers):
    list_len = len(numbers)
    start = int(list_len/2)
    while start >= 1:
        sift_down(numbers, start, list_len)
        start = start - 1
    return numbers


def heapsort(numbers):
    list_len = len(numbers)
    max_heapify(numbers)
    for i in range(list_len-1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        sift_down(numbers, 1, i)
    return numbers


def merge(numA, numB):
    if len(numA) <= 0:
        return numB
    if len(numB) <= 0:
        return numA

    i, j, numC = 0, 0, []
    while True:
        if numA[i] < numB[j]:
            numC.append(numA[i])
            i = i + 1
        else:
            numC.append(numB[j])
            j = j + 1
        if i >= len(numA):
            numC.extend(numB[j:])
            break
        if j >= len(numB):
            numC.extend(numA[i:])
            break
    return numC


def mergesort(numbers):
    list_len = len(numbers)
    if list_len <= 1:
        return numbers
    mid = int(list_len/2)
    numbers = merge(mergesort(numbers[:mid]), mergesort(numbers[mid:]))
    return numbers

def selectionsort(numbers):
    list_len = len(numbers)
    for i in range(list_len, 0, -1):
        max, idx = numbers[i-1], i-1
        for j in range(i):
            if numbers[j] > max:
                max, idx = numbers[j], j
        numbers[i-1], numbers[idx] = numbers[idx], numbers[i-1]
    return numbers


def bubblesort(numbers):
    list_len = len(numbers)
    for i in range(list_len-1):
        for j in range(i+1, list_len):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def quicksort(numbers):
    list_len = len(numbers)
    if list_len <= 1: return numbers
    pivot = numbers[-1]
    back = list_len-2
    front = 0
    while front < back:
        if numbers[front] > pivot:
            numbers[front], numbers[back] = numbers[back], numbers[front]
            back = back - 1
        else: front = front + 1
    if numbers[front] > pivot:
        numbers[-1], numbers[front] = numbers[front], numbers[-1]
    numbers = quicksort(numbers[:front+1]) + quicksort(numbers[front+1:])
    return numbers


if __name__ == '__main__':
    test_lists = []
    test_lists.append([2])
    test_lists.append([2, 1])
    test_lists.append([2, 1, 4])
    test_lists.append([2, 1, 1, 4])
    test_lists.append(list(range(10)))
    test_lists.append(list(reversed(list(range(10)))))
    test_lists.append(random.sample(range(1, 1000), 10))

    sorts = {
                "Quicksort":quicksort,
                "Bubblesort":bubblesort,
                "Selectionsort":selectionsort,
                "Mergesort": mergesort,
                "Heapsort": heapsort,
             }

    for name, func in sorts.items():
        print "Running " + name
        for numlist in test_lists:
            print "Input: " + str(numlist) + "  Output: " + str(func(numlist[:]))

