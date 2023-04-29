x = True                      #Cemal Taner ALTUNDAŞ - 200709037
total_average = 0
average_list = [0]
student_ID_list = [0]
midterm_list = [0]
homework_list = [0]
final_list = [0]
letter_list = [0]


while x:
    student_ID = int(input("Student ID: "))
    midterm = int(input("Midterm: "))
    homework = int(input("Homework: "))
    final = int(input("Final: "))
    average = midterm * 0.2 + homework * 0.2 + final * 0.6
    total_average = total_average + average

    average_list.append(average)
    student_ID_list.append(student_ID)
    midterm_list.append(midterm)
    homework_list.append(homework)
    final_list.append(final)

    new = input("Do you want to add a new student? (Y) or (N)")
    if new == "N":
        x = False
print("Average is: ", total_average / (len(student_ID_list)-1))

print("ID", end="    "), print("M", end="     "), print("H", end="     ")
print("F", end="      "), print("A", end="     ")
print("L", end="      "), print("S")
print("--"*22)

for i in range(1,(len(student_ID_list))):
    print(student_ID_list[i], end="    ")
    print(midterm_list[i], end="    ")
    print(homework_list[i], end="    ")
    print(final_list[i], end="    ")
    if average_list[i] < 60:
        print(average_list[i], end="    ")
        print("F", end="    ")
        print("Failed")
    elif average_list[i] < 70:
        print(average_list[i], end="    ")
        print("D", end="    ")
        if final_list[i] < 60:
            print("Failed")
        else:
            print("Passed")
    elif average_list[i] < 80:
        print(average_list[i], end="    ")
        print("C", end="    ")
        if final_list[i] < 60:
            print("Failed")
        else:
            print("Passed")
    elif average_list[i] < 90:
        print(average_list[i], end="    ")
        print("B", end="    ")
        if final_list[i] < 60:
            print("Failed")
        else:
            print("Passed")
    else:
        print(average_list[i], end="    ")
        print("A", end="    ")
        if final_list[i] < 60:
            print("Failed")
        else:
            print("Passed")
