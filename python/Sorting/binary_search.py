input = [1, 2, 3, 4, 5, 6, 7, 8]


def binary_search(input, value):
    inp_len = len(input)
    if inp_len <= 0:
        return None
    mid = inp_len/2
    if value == input[mid]:
        return mid
    elif value < input[mid]:
        return binary_search(input[:mid], value)
    else:
        a = binary_search(input[mid+1:], value)
        if a == None:
            return None
        else:
            return mid + a + 1


value = 2
print(input)
idx = binary_search(input, value)
print idx
