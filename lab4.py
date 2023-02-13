import csv


#1. Определите количество наименований товаров в каждой из 4-х категорий.

name_company = set()

with open("p4_data_26.csv") as f:
    reader = csv.reader(f)
    for stolb in reader:
        name_company.add(stolb[1])
print("Количество наименований товаров:",len(name_company))

#2. Вычислите суммарный объем (в валюте) товаров по каждому из 4-х поставщиков, о также по товарам, у которых не указан поставщик.


summ_tovarov = []
stroka = ['ID', 'Name', 'Company', 'Price', 'Count', 'Category', 'discount']


with open("p4_data_26.csv") as f:
    reader = csv.reader(f)
    for stolb in reader:
        if stolb != stroka:
            summ_tovarov.append(float(stolb[3][1:]))
print("Суммарный объем:",'$'+str(sum(summ_tovarov)))

#3. Найдите самый дорогой товар с учетом скидки.

maxi_price = -10000000000

name_company = ''

with open("p4_data_26.csv") as f:
    reader = csv.reader(f)
    for stolb in reader:
        if (stolb != stroka) and (stolb[6] != ''):
            maxi_price = max(maxi_price,float(stolb[3][1:]))
            name_company = stolb[2]
            

print("Самый дорогой товар с учётом скидки:",name_company,"$"+str(maxi_price))
            
#4. Найдите товар с минимальным количеством.

min_kolvo = 10**10

name_company_min= ""

with open("p4_data_26.csv") as f:
    reader = csv.reader(f)
    for stolb in reader:
        if (stolb != stroka):
            if min_kolvo > int(stolb[4]):
                min_kolvo = int(stolb[4])
                name_company_min = stolb[1]
print('Товар с минимальным количеством:',name_company_min+'.','С количеством в',min_kolvo,'eд.')
