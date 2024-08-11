arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85

fib2, fib1, fibM = 0, 1, 1
while fibM < len(arr):
    fib2, fib1 = fib1, fibM
    fibM = fib1 + fib2

offset = -1
index = -1

while fibM > 1:
    i = offset + fib2
    if i >= len(arr):
        i = len(arr) - 1

    if arr[i] < x:
        fibM, fib1 = fib1, fib2
        fib2 = fibM - fib1
        offset = i
    elif arr[i] > x:
        fibM, fib1 = fib2, fib1 - fib2
        fib2 = fibM - fib1
    else:
        index = i
        break

if index == -1 and fib1 and arr[offset + 1] == x:
    index = offset + 1

print(f"Found at index: {index}" if index >= 0 else "Not found")
