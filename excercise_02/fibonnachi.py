import random
import time

start = time.time()
x = 34
y = 2
a = 0
b = 1
c = 0

def fib(a,b):
    global y
    global c
    c = a + b
    if (y < x):
        y += 1
        fib(b,c)

fib (a, b)

end = time.time()

print("fib(", x, ") is", c)

print("fib(", x, ") is", end - start)
