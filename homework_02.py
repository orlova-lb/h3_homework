"""
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """


def validate_password(password):
    error_list = list()
    if not _validate_symbols(password):
        error_list.append("Сontains prohibited characters")
    if not _validate_letters_even(password):
        error_list.append("Сontains an odd number of letters")
    if not _validate_numbers_odd(password):
        error_list.append("Сontains an even number of digits")

    return error_list


"""
  Проверяет строку на наличие запрещенных символов
  Подсказка: у строк есть метод, проверяющий наличие только букв и цифр
  Возвращает True\False
  """


def _validate_symbols(input_str):
    return input_str.isalnum()


"""
  Проверяет строку на четное количество букв
  Возвращает True\False
  """


def _validate_letters_even(input_str):
    match_let = [let for let in input_str if let.isalpha()]
    if not len(match_let) % 2:
        return True
    return False


"""
  Проверяет строку на нечетное количество цифр
  Возвращает True\False
  """


def _validate_numbers_odd(input_str):
    match_numb = [numb for numb in input_str if numb.isdigit()]
    if not len(match_numb) % 2:
        return True
    return False

