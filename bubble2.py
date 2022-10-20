import random


string = input("昇順なら１、降順なら２を入力してください:")

if string == '1':
    def bubble_sort(arr):
        length = len(arr)
        for i in range(length):
            for j in reversed(range(i + 1, length)):
             if arr[j - 1] > arr[j]:
                 arr[j - 1], arr[j] = arr[j], arr[j - 1]
        return arr

    if __name__ == "__main__" :
        arr = list(range(1, 100 + 1))
        src = random.sample(arr, 5)
        print(src)
        dst = bubble_sort(src)
        print(dst)

else:
    def bubble_sort(num):
        length = len(num)
        for i in range(length):
            for j in reversed(range(i + 1, length)):
             if num[j - 1] < num[j]:
                 num[j - 1], num[j] = num[j], num[j - 1]
        return num

    if __name__ == "__main__" :
        num = list(range(1, 100 + 1))
        src = random.sample(num, 5)
        print(src)
        dst = bubble_sort(src)
        print(dst)
