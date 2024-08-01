from datetime import datetime
import time
def binary_search(data, target):
    data.sort()
    low = 0
    index = len(data) - 1
    step = 0
    while True:
        time.sleep(1)
        midle = (index + low) // 2
        if target == data[midle]:
            step += 1
            break
        if target > data[midle]:
            low = midle + 1
            step += 1
        if target < data[midle]:
            index = midle - 1
            step += 1
        if low > index:
            print("bunday raqam mavjud emas")
            break
    print(step)
def liner_search(data, target):
    for i in data:
        time.sleep(1)

        if target == i:
            print(i)
            break
if __name__ == "__main__":
    data = [1, 2, 3, 8, 10, 56, 11, 4, 5, 7, 9]
    target = int(input("target: "))
    print(datetime.now().time())
    liner_search(data, target)
    print(datetime.now().time())
