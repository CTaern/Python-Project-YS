class Student:

    def __init__(self, id, name, lastname):
        self.name = name
        self.lastname = lastname
        self.id = id

    def sbooktype(self, sbooktype):
        self.sbooktype = sbooktype

    def sanswers(self, sanswers):
        self.sanswers = sanswers

    def schoices(self, schoices):
        self.schoices = schoices

class University:

    def __init__(self, id, name, department, point, cap):
        self.id = id
        self.name = name
        self.department = department
        self.point = point
        self.cap = cap


students = {}
f = open("student.txt", 'r')
for line in f:
    lines = line.split()
    id = lines[0]
    name = lines[1]
    lastname = lines[2]
    students[id] = Student(id, name, lastname)
f.close()

key = []
keya = []
keyb = []
f = open("key.txt", 'r')
for line in f:
    key.append((line))
f.close()
keya = list(key[0])
keyb = list(key[1])
del keya[-1]
del keyb[-1]







answers = {}
f = open("answers.txt", 'r')
for line in f:
    lines = line.split()
    student_id = lines[0]
    type = lines[1]
    answer = lines[2]
    choice = lines[3:]
    student = students[student_id]
    student.sbooktype(type)
    student.sanswers(answer)
    student.schoices(choice)

f.close()

abookanswers = []
abookstudents = []
abook = []
bbookanswers = []
bbookstudents = []
bbook = []
allstudents = []
allbooks = []
corrects = []
corrects0 = []
incorrects = []
incorrects0 = []
blanks = []
blanks0 = []
points = []
netcorrects = []
netcorrects0 = []
sswp = []
sswp0 = []
sswp0withchoices = []
abookchoicesstr = []
bbookchoicesstr = []
allchoicesstr = []
abookchoices = []
bbookchoices = []
allbookschoices = []
newallbookschoices = []
unibasepoints = []
uni1 = []
uni2 = []
uni3 = []
uni4 = []
uni5 = []
uni6 = []
uni7 = []
uni8 = []
uni9 = []
uni10 = []
uni11 = []
nonplacedstud = []
capacities = []
uninames = []


universities = {}
f = open('university.txt', 'r')
for line in f:
    lines = line.split()
    id = lines[0]
    name = lines[1:-2]
    a = lines.index("University")
    department = lines[a+1:-2]
    cap = lines[-1]
    caps = cap.split(",")
    capacity = caps[-1]
    point = caps[-2]
    unibasepoints.append(int(point))
    capacities.append(capacity)
    universities[id] = University(id, name, department, point, capacity)
f.close()



f = open("university.txt", "r")
departments = []
for line in f:
    lines = line.split(",")
    id = lines[0]
    name = lines[1]
    uninames.append(name)
    point = lines[2]
    a = name.split("University")
    department = a[1]
    departments.append(department)
f.close()


def uniquedepartments(departments):
    list_set = set(departments)
    uniquelist = list(list_set)
    for i in uniquelist:
        print(i)


f = open("university.txt", 'r')
unis = []
for line in f:
    lines = line.split(",")
    uni = lines[1:3]
    unis.append(uni)
f.close()




for key in students.keys():
    student = students.get(key)
    if student.sbooktype == "A":
        a = list(student.sanswers)
        abookanswers.append(a)
        abookstudents.append(student.id +" "+ student.name +" "+ student.lastname)
        abook.append(student.sbooktype)
        b = student.schoices
        c = (b)
        abookchoicesstr.append(c)
        for i in b:
            if i == "1":
                abookchoices.append(uninames[0])
            elif i == "2":
                abookchoices.append(uninames[1])
            elif i == "3":
                abookchoices.append(uninames[2])
            elif i == "4":
                abookchoices.append(uninames[3])
            elif i == "5":
                abookchoices.append(uninames[4])
            elif i == "6":
                abookchoices.append(uninames[5])
            elif i == "7":
                abookchoices.append(uninames[6])
            elif i == "8":
                abookchoices.append(uninames[7])
            elif i == "9":
                abookchoices.append(uninames[8])
            elif i == "10":
                abookchoices.append(uninames[9])
            elif i == "11":
                abookchoices.append(uninames[10])

    elif student.sbooktype == "B":
        a = list(student.sanswers)
        bbookanswers.append(a)
        bbookstudents.append((student.id +" "+ student.name +" "+ student.lastname))
        bbook.append(student.sbooktype)
        b = student.schoices
        c = (b)
        bbookchoicesstr.append(c)
        for i in b:
            if i == "1":
                abookchoices.append(uninames[0])
            elif i == "2":
                abookchoices.append(uninames[1])
            elif i == "3":
                abookchoices.append(uninames[2])
            elif i == "4":
                abookchoices.append(uninames[3])
            elif i == "5":
                abookchoices.append(uninames[4])
            elif i == "6":
                abookchoices.append(uninames[5])
            elif i == "7":
                abookchoices.append(uninames[6])
            elif i == "8":
                abookchoices.append(uninames[7])
            elif i == "9":
                abookchoices.append(uninames[8])
            elif i == "10":
                abookchoices.append(uninames[9])
            elif i == "11":
                abookchoices.append(uninames[10])


for x in abookstudents:
    allstudents.append(x)
for x in abook:
    allbooks.append(x)
for x in abookchoices:
    allbookschoices.append(x)
for x in abookchoicesstr:
    allchoicesstr.append(x)
for y in bbookstudents:
    allstudents.append(y)
for y in bbook:
    allbooks.append(y)
for y in bbookchoices:
    allbookschoices.append(y)
for y in bbookchoicesstr:
    allchoicesstr.append(y)

for line in abookanswers:
    c = 0
    ic = 0
    b = 0
    for i in range(40):
        if line[i] == keya[i]:
            c += 1
        elif line[i] == "-":
            b += 1
        elif line[i] != keya[i]:
            ic += 1
    corrects0.append(str(c))
    corrects.append(c)
    incorrects.append(ic)
    incorrects0.append(str(ic))
    blanks.append(b)
    blanks0.append(str(b))
    netcorrect = ((40 - int(b)) - (float(ic*1.25)))
    netcorrects0.append(str(netcorrect))
    netcorrects.append(netcorrect)
    spoint = str(netcorrect * 15)
    points.append(spoint)

for line in bbookanswers:
    c = 0
    ic = 0
    b = 0
    for i in range(40):
        if line[i] == keya[i]:
            c += 1
        elif line[i] == "-":
            b += 1
        elif line[i] != keya[i]:
            ic += 1
    corrects.append(c)
    corrects0.append((str(c)))
    incorrects.append(ic)
    incorrects0.append(str(ic))
    blanks.append(b)
    blanks0.append(str(b))
    netcorrect = ((40 - int(b)) - (float(ic * 1.25)))
    netcorrects.append(netcorrect)
    netcorrects0.append(str(netcorrect))
    spoint = str(netcorrect * 15)
    points.append(spoint)

for i1, i2 in zip(allstudents, points):
    sswp.append(i1 + ", " + i2)
for line in sswp:
    lines = line.split(", ")
    sswp0.append(lines)




def ndelement(elem):
    return elem[1]
def ndelement0(elem):
    return float(elem[1])

unis.sort(key=ndelement, reverse=True)
sswp0.sort(key=ndelement0, reverse=True)


resulttextlist = []
for i in range(len(allstudents)):
    resulttextlist.append(allstudents[i] + " " + allbooks[i] + " " + corrects0[i] + " " + incorrects0[i] + " " + blanks0[i] + " " + netcorrects0[i] + " " + points[i] + " " + allbookschoices[i] +", "+ allbookschoices[i+1]+", " + allbookschoices[i+2]+", " + allbookschoices[i+3]+", " + allbookschoices[i+4] + " ")



for i in range(len(sswp0)):
    sswp0withchoices.append(sswp0[i] + allchoicesstr[i])

for i in sswp0withchoices:
    if float(i[1]) <= 0:
        nonplacedstud.append(i[0])



for i in sswp0withchoices:
    for y in range(2,len(i)):
        if i[y] == str(1) and float(i[1]) >= float(unibasepoints[0]) and len(uni1) < int(capacities[0]):
            uni1.append(i[0])
        elif i[y] == str(2) and float(i[1]) >= float(unibasepoints[1]) and len(uni2) < int(capacities[1]):
            uni2.append(i[0])
        elif i[y] == str(3) and float(i[1]) >= float(unibasepoints[2]) and len(uni3) < int(capacities[2]):
            uni3.append(i[0])
        elif i[y] == str(4) and float(i[1]) >= float(unibasepoints[3]) and len(uni4) < int(capacities[3]):
            uni4.append(i[0])
        elif i[y] == str(5) and float(i[1]) >= float(unibasepoints[4]) and len(uni5) < int(capacities[4]):
            uni5.append(i[0])
        elif i[y] == str(6) and float(i[1]) >= float(unibasepoints[5]) and len(uni6) < int(capacities[5]):
            uni6.append(i[0])
        elif i[y] == str(7) and float(i[1]) >= float(unibasepoints[6]) and len(uni7) < int(capacities[6]):
            uni7.append(i[0])
        elif i[y] == str(8) and float(i[1]) >= float(unibasepoints[7]) and len(uni8) < int(capacities[7]):
            uni8.append(i[0])
        elif i[y] == str(9) and float(i[1]) >= float(unibasepoints[8]) and len(uni9) < int(capacities[8]):
            uni9.append(i[0])
        elif i[y] == str(10) and float(i[1]) >= float(unibasepoints[9]) and len(uni10) < int(capacities[9]):
            uni10.append(i[0])
        elif i[y] == str(11) and float(i[1]) >= float(unibasepoints[10]) and len(uni11) < int(capacities[10]):
            uni11.append(i[0])
        else:
            nonplacedstud.append(i[0])
        break

menu = True
while menu:
    print("(0) For exit")
    print("(1) For search for student with ID")
    print("(2) For list of universities")
    print("(3) For result.txt that contains student's id, name, lastname, scores, name of universities as chosen")
    print("(4) For list of students sorted with scores")
    print("(5) For list of every student placed universities and which one")
    print("(6) For list of nonplaced students")
    print("(7) For list of departments")
    userinput = int(input("Select option: "))
    print("--" * 15)
    if userinput == 0:
        menu = False
    elif userinput == 1:
        idinput = input("Enter ID: ")
        for key in students.keys():
            Student = students.get(key)
            if idinput == Student.id:
                print(Student.name, Student.lastname)
                print("--" * 15)
                menu = True
        if idinput not in students:
            print("Not found")
            print("--" * 15)
            menu = True
    elif userinput == 2:
        for i in unis:
            print(", ".join(i))
        print("--" * 15)
    elif userinput == 7:
        uniquedepartments(departments)
        print("--" * 15)
    elif userinput == 4:
        for i in sswp0:
            print(i[0] + ", " + i[1])
        print("--"*15)
    elif userinput == 3:
        f = open("result.txt", 'w')
        for i in resulttextlist:
            f.write(i)
        f.close()
    elif userinput == 5:
        print(uninames[0])
        print("--" * 15)
        for i in uni1:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[1])
        print("--" * 15)
        for i in uni2:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[2])
        print("--" * 15)
        for i in uni3:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[3])
        print("--" * 15)
        for i in uni4:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[4])
        print("--" * 15)
        for i in uni5:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[5])
        print("--" * 15)
        for i in uni6:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[6])
        print("--" * 15)
        for i in uni7:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[7])
        print("--" * 15)
        for i in uni8:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[8])
        print("--" * 15)
        for i in uni9:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[9])
        print("--" * 15)
        for i in uni10:
            print(i)
        print("--" * 15)
        print("\t")
        print(uninames[10])
        print("--" * 15)
        for i in uni11:
            print(i)
        print("--" * 15)
        print("\t")
    elif userinput == 6:
        print("Nonplaced students")
        print("--"*15)
        nonplacedstud0 = set(nonplacedstud)
        for i in nonplacedstud0:
            print(i)
        print("--"*15)

