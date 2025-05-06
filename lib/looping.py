#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    ran = False

    while i >= 1:
        print(i)
        i -= 1
        ran =True
    
    if ran:
        print("Happy New Year!")
   

def square_integers(int_list):
    # code goes here!
    squared = [num ** 2 for num in int_list]
    return squared



def fizzbuzz():
    # code goes here!
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else :
            print(i)
fizzbuzz()
