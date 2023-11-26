#!/usr/bin/env python3
length = 10
def print_fibonacci(length):
    fibonnacci_length = []
    if length <= 0:
       print([]) 
    elif length == 1:
        print([0])
    elif length == 2:
        print ([0,1])
    else:
        fibonnacci_length = [0,1]
        for i in range(2, length):
           num = fibonnacci_length[-1] + fibonnacci_length[-2] 
           fibonnacci_length.append(num)
        print(fibonnacci_length)   
    
    pass