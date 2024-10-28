def find_index(list_of_items, item):
    """Функция по поиску индекса товара в списке товаров"""
    items_index = None  # Индекс искомого предмета, None в случае отсутствия
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            items_index = i
            break
    return items_index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
