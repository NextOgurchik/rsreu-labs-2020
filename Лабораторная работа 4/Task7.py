def BubbleSort(array):
    i = 0
    j = 1
    arr = array.copy()
    while j < len(arr):
        i = 0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i = i + 1
        j = j + 1
    return arr

def SecondMax(array):
    IsEnd = False
    arr = BubbleSort(array)
    i = len(arr) - 1
    while not IsEnd:
        if i < 1:
            IsEnd = True
            firstMax = i
        elif arr[i] > arr[i-1]:
            IsEnd = True
            firstMax = i
        i = i - 1
    if firstMax > 0 and arr[firstMax] > arr[firstMax-1]:
        secondMax = "Второй максимум: " + str(arr[firstMax-1])
    else:
        secondMax = "Второго максимума нет"
    return secondMax

arr = [5,5,5,5,5,5,5]
print(SecondMax(arr))
