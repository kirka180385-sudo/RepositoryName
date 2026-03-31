numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#Найдем индекс None
none_index = numbers.index(None)
numbers [none_index] = 0 #Присвоил индексу 0, чтобы в списке были int значения для вычисления суммы

arithmetic_mean = sum(numbers) / len(numbers)
numbers [none_index] = arithmetic_mean

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
