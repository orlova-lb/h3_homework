def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = list()
    for url in url_list:
        if '/catalog/' in url:
            result_list.append(url)
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    if len(input_str) % 2:
        output_str = input_str[(len(input_str) // 2) - 1:(len(input_str) // 2) + 2]
    else:
        output_str = input_str[(len(input_str) // 2) - 1:(len(input_str) // 2) + 1]
    return output_str


from collections import Counter


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = dict(Counter(input_str))
    print(output_dict)
    output_dict = None
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    half_str1 = int(len(str1) / 2)
    result_str = str1[:half_str1] + str2 + str1[half_str1:]
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    even_int_list = [i for i in range(0, 101) if not i % 2]
    return even_int_list

