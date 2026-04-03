import math

numberBeginningRange, numberEndRange = map(int, input("Введите целое число начала диапазона и конца через пробел: ").split())
arrayNumbers = list(range(numberBeginningRange, numberEndRange + 1))# Заполнение списка от начального числа до конечного
greatestCommonDivisor = arrayNumbers[0] #Присвоение самого первого числа в списке
for number in arrayNumbers[1:]:#Проход по списку от 2 числа
    greatestCommonDivisor = math.gcd(greatestCommonDivisor, number)#Вычисление НОД
    if(greatestCommonDivisor == 1):#Если НОД = 1
        break#Выход из цикла
print(greatestCommonDivisor)#Вывод НОД
