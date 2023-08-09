#sabe-se que um vetor contenha apenas os valores 1, 2 e 3  ordene esse vetor em tempo o(n)
def sort_123(arr):
    left, mid, right = 0, 0, len(arr) - 1
    while mid <= right:
        if arr[mid] == 1:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 2:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr