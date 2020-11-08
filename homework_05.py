#Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида
# "test string" в "<i><b>test string</b></i>"
import os


def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }


        def wrapper(text):
            result = text
            for tag in tags:
                if tag in tag_base:
                    result = tag_base[tag].replace('%text%', result)
            return result
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных


def log_reading(func):
    def wrapper(*args):
        return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".log")]
    return wrapper


@log_reading
def get_files():
    return os.listdir()

