def busca_binaria(arr, target):

    right = len(arr) - 1
    left = 0

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] == right:
            right = mid - 1

        else:
            left = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 4

resultado = busca_binaria(arr, target)


print(resultado)



