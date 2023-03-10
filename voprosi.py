# 1. Напишите код для печати суммы элементов списка p:
p = [10, 100, 34, 56, 45, 45]
print('Сумма элементов:',sum(p))

#2. Напишите код для печати количества элементов списка p:
p = [10, 100, 34, 56, 45, 45]
print("Количество элементов:",len(p))


#3. Напишите код для печати суммы элементов кратных 7:
summ = 0
p = [10, 100, 35, 34, 56, 45, 45, 21]
for i in range(len(p)):
    if p[i] % 7 == 0:
        summ += p[i]
print("Cумма элементов кратных 7:",summ)

#Напишите код для поиска ключей словаря d, для которых значения превышают 45:

p = {4:10, 12:100, 35:3, 34:56, 56:11, 45:"abc"}
for key, cifr in p.items():
  if str(cifr).isdigit() and int(cifr) > 45:
    print('Ключи словаря d:',key,sep = " ")

#5. Напишите код, который выводит список, составленный из квадратов чисел от 1 до 100. Сам список также необходимо сгенерировать.
spisok = []
for i in range(1,100 + 1):
    spisok.append(i*i)
print('Список квадратов чисел:', spisok)
#6. Опишите структуру файла csv. Поясните последовательность действий при чтении файла csv

#1      В файле значений, разделенных запятыми (CSV), данные сохраняются в виде обычного текста. 
        #Первая строка значений в файле CSV представляет собой информацию заголовка и служит для описания содержимого следующих столбцов. 
        #Допустимые типы параметров: NUMBER, LENGTH, AREA, VOLUME, ANGLE и OTHER
#2 
#import csv Импортируем библиотеку CSV для легкой работы с CSV файлами
        
#with open("namefile") as f: открываем файл
#    reader = csv.reader(f)   переменная reader отвечает за чтение
#    for line in reader:   ходим по строчкам 