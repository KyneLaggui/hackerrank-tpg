def time_table(a, b):
    if b > 0:
        for i in range(1, b + 1):
            print(f"{a} * {i} = {a * i}")
    else:
        for i in range(b, 1):
            print(f"{a} * {i} = {a * i}")

def constraints(a, b):
    if -10 <= a <= 10 and -10 <= b <= 10:
        return True
    else:
        return False

def main():
    a = int(input())
    b = int(input())

    if not constraints(a, b):
        return False
    else:
        time_table(a, b)

main()
    