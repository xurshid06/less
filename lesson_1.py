variant B

#1 Quyidagilardan immuteblelarni tanlang;
 #JAvob: B
#2. mv eski_repozitoriya_ismi
#   cd yangi_repozitoriya_ismi

#3 git log --oneline
4.
prime_numbers = []
def find_prime_number():
    global prime_numbers
    for a in range(1, 501):
        b = 0
        c = [x for x in range(1, a+1) if a % x == 0]
    if len(c) == 2:
        prime_numbers.append(a)



5.
def generator():
    def find_prime_number():
        for a in range(1, 501):
            b = 0
            c = [x for x in range(1, a + 1) if a % x == 0]
        if len(c) == 2:
            return True
        return False
    yield find_prime_number()

#6 javob: C
7.
import threading
import time
def worker():
    print("Dastur ishga tushdi")
    time.sleep(2)
    print("Dastur tugadi")

def main():
"os" modulini ishlatgan holda, ishlab turgan python faylini nomini "__main__.py" ga o'zgartiring, so'ngra bir soniyadan so'ng yana qaytarib o'zini nomiga qaytaradigan dastur yoz.
    thread = threading.Thread(target=worker)
    thread.start()
    for i in range(1, 11):
        print(i)
    thread.join()

if __name__ == "__main__":
    main()


9.
import os
import time

def main():
    current_filename = os.path.basename(__file__)
    new_filename = "__main__.py"
    os.rename(current_filename, new_filename)
    time.sleep(1)
    os.rename(new_filename, current_filename)

if __name__ == "__main__":
    main()
