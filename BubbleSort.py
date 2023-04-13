arr = [int(i) for i in open("arr.txt")] #5000 items
print(arr)  

temp = 0

while min(arr) != arr[0]:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp

print(arr)

# average exite time = ~1.8 seconds
# (slower than default .sort())