import time
import random

def printTrack(end):
    for i in range(end+1):
        print(i, end=" ")
    print()
def trackSide(end):
    for i in range(end+2):
        print("--", end="")
    print()

def trackA(end):
    for i in range(end+1):
        if a == i:
            print("A", end="")
        else:
            print("-", end=" ")
    print()
def trackB(end):
    for i in range(end+1):
        if b == i:
            print("B", end="")
        else:
            print("-", end=" ")
    print()
def trackC(end):
    for i in range(end+1):
        if c == i:
            print("C", end="")
        else:
            print("-", end=" ")
    print()
def moveOrder(x, end):
        a = random.randint(0, 9)
        if a == 0:
            return x - 2
        elif a == 1 or a == 2:
            return x - 1
        elif a == 3 or a == 4:
            return x
        elif a == 5 or a == 6 or a == 7 or a == 8:
            return x + 1
        elif a == 9:
            return x + 2
a = 0
b = 0
c = 0
end = int(input("Enter the length of track: "))

while a < end and b < end and c < end:
    if a < 0:
        a = 0
    elif b < 0:
        b = 0
    elif c < 0:
        c = 0
    printTrack(end)
    trackSide(end)
    trackA(end)
    trackB(end)
    trackC(end)
    time.sleep(0.5)
    a = moveOrder(a, end)
    b = moveOrder(b, end)
    c = moveOrder(c, end)
    if a > end:
        a = end
    elif b > end:
        b = end
    elif c > end:
        c = end


(printTrack(end))
(trackSide(end))
(trackA(end))
(trackB(end))
(trackC(end))

if a > b and a > c:
    print("A wins")
elif b > a and b > c:
    print("B wins")
elif c > a and c > b:
    print("C wins")
elif a == b or a == c or b == c:
    print("It's a tie")

