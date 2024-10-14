TOTAL_DISK = 1.44 * 1024 * 1024  # Объём дискеты в байтах
CHR_USE = 4  # Символ весит 4 байта

pages = 100  # Количество страниц
str_in_page = 50  # Количество строк в странице
chr_in_str = 25  # Количество символов в строке

book_use = pages * str_in_page * chr_in_str * CHR_USE  # Вес книги в байтах
count_books = int(TOTAL_DISK // book_use)  # Число книг, помещающихся на дискету

print("Количество книг, помещающихся на дискету:", count_books)
