number = int(input("Введіть число з 4 цифр: "))
if number < 1000 or number > 9999:
    print("ведіть 4 значне число ")
else:
    n1 = number // 1000
    print(n1)
    n2 = number // 100 % 10
    print(n2)
    n3 = number // 10 % 10
    print(n3)
    n4 = number % 10
    print(n4)
number_five = int(input("Введіть число з 5 цифр: "))
if number_five < 9999 or number > 99999:
    print("ведіть 4 значне число ")
else:
    n1 = number_five // 10000
    n2 = number_five // 1000 % 10
    n3 = number_five // 100 % 10
    n4 = number_five //10 % 10
    n5 = number_five % 10
print(f"{n5}{n4}{n3}{n2}{n1}")

