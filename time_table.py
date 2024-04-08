def time_table(a, b):
    for i in range(1, b + 1):
        print(f"{a} * {i} = {a * i}")

def constraints(a, b):
    if -10 <= a <= 10 and -10 <= b <= 10:
        return True
    else:
        return False

def main():
    a = int(input("Enter the timetable number: "))
    b = int(input("Enter the range of timetable: "))

    if not constraints(a, b):
        return False
    else:
        time_table(a, b)

main()
    