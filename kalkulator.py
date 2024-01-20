print("Kalkulator")

znak = input("Wybierz jednen ze znakow (+ - * /) ")
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if znak == "+":
    print(a+b)
elif znak == "-":
    print(a-b)
elif znak == "*":
    print(a*b)
elif znak == "/":
    print(a/b)
else:
    print("Bledny znak")
