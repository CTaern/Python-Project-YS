

def monthlygain():
    base_money = int(input("Enter base money: "))
    a = int(input("Weekly or daily? (1 For week, 2 For day: "))
    percent_of_gain = int(input("Each percentage of gaining? "))
    time = int(input("How many months: "))
    if a == 1:
        for i in range(4 * time):
            base_money = base_money + ((base_money / 100) * percent_of_gain)
        return base_money
    elif a == 2:
        for i in range(30 * time):
            base_money = base_money + ((base_money / 100) * percent_of_gain)
        return base_money

while True:
    print(monthlygain())
    user_input = int(input("1 For retest, 2 For quit: "))
    if user_input == 2:
        break