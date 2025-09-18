import random

test_random = random.randint(0, 10)
 
print("--เกมเดาใจตัวเลข คอมพิวเตอร์--")

guess_number = int(input("What is your guess number (0-9)?:" ))

if test_random == guess_number:
    print(" เกงมากมั่วถูก ")

if guess_number < test_random:
    print(" ผิดจ้า น้อยไปเนอะ ")

if guess_number > test_random :
    print (" ผิดจ้า มากไปเนอะ ")
