import heapq

arrayNumbers = input().split()#Ввод любых данных через пробел
arrayNumbers = [int(x) for x in arrayNumbers if x.isdigit()]#Удаление всех данных, которые не являются целыми числами

if len(arrayNumbers)<2:#Если целых чисел меньше 2
    print("Введено не достаточное количество целых чисел")
    exit()#Прекращение работы программы
minimumNumbers = heapq.nsmallest(2, arrayNumbers)#Нахождение 2 минимальных чисел
sum = minimumNumbers[0] + minimumNumbers[1]#Вычисление суммы 2 минимальных чисел

print(f"Два минимальных числа: {minimumNumbers[0]}, {minimumNumbers[1]}; сумма {sum}")#Вывод чисел и их суммы
