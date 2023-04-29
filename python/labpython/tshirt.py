f = open("tshirt.txt", "r")
def numberofm():
    number = 0
    for line in f:
        lines = line.split()
        size = lines[2]
        if size == "M":
            number = number + 1
    f.close()
    return number
print("Number of m sized ", numberofm())

f = open("tshirt.txt", "r")
def numberofl():
    number = 0
    for line in f:
        lines = line.split()
        size = lines[2]
        if size == "L":
            number = number + 1
    f.close()
    return number
print("Number of L sized ", numberofl())

f = open("tshirt.txt", "r")
def maxhl():
    height = []
    for line in f:
        lines = line.split()
        size = lines[2]
        heights = 0
        if size == "L":
            heights = lines[0]
            height.append(heights)
    x = sorted(height)
    print(height)
    f.close()
    return x[-1]
print(maxhl())

f = open("tshirt.txt", "r")
def maxweight():
    weight = []
    for line in f:
        lines = line.split()
        weights = lines[1]
        weight.append(weights)
        x = sorted(weight)
    f.close()
    return x[-1]
print("Maximum weight of customers is ", maxweight())


        
