# Найдите сумму цифр трехзначного числа.
x = int(input('Введите число:'))
print(x//100 + (x//10)%10 + x%10)