# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 #Обьем дискеты в Мб
Number_of_pages = 100 #Количество страниц в книге
Number_of_rows = 50 #Число строк на странице
Number_of_characters = 25 #Количество символов в строке
b = 4 #Размер одного символа в байтах
disk_size_mb = disk_size * 1024 * 1024 #Обьем дискреты в байтах
a = Number_of_pages * Number_of_rows * Number_of_characters #Общее количество символов
book_size_bytes = a * b #Вес книги в байтах
books = int(disk_size_mb // book_size_bytes)
print("Количество книг, помещающихся на дискету:", books)
