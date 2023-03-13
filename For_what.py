#Завдання: у рамдомному списку потрібно вивести кількість елементів "3"
#або іх відсутність
import random
a = input("Введіть бажану довжину списку:")
thislist = [random.randint(0,9) for x in range(0,int(a))]
print(thislist)
#print(thislist.count(3))
nums = thislist.count(3)
if nums != 0:
    print('У списку присутні ' + str(nums) + ' елементи "3"')
else:
    print("На жаль, такого елементу у списку немає")



