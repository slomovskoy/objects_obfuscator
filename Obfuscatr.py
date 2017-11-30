import json
import Dictionary
import os, sys

class Obfuscatr:
    """
    Класс обфускатора объектов
    Имеет поля:
        delimiter - разделитель сгенерированных слов
        words_count - количество слов в результате
        Сеттеры и геттеры решил для единственного класса не делать. На Java сделал бы, даже поля приватными сделал бы
        Количество вариантов обфускации не кодировал, потому что принцип тот же. Нужно только добавить ещё один цикл
    """
    pass

    def __init__(self):
        self.delimiter = "" # разделитель слов
        self.words_count = 1 # количество слов в результате


    def obfuscate(self, object):
        """
        Основной метод.
        Объект преобразовываем в json
        Циклически выполняем следующий алгоритм:
            обфусцируем строку
            получаем её код
            добавляем код в список
        Количество итераций = количтсву требуемых слов
        По списку кодов получаем список слов, соедняем разделителем, возвращаем результат
        :param object:
        :return string:
        """
        integers_list = []
        source_json = get_json_from_something(object)
        words_count = self.words_count
        for i in range(words_count):
            source_json = hash_string(source_json)
            word_index = get_int_from_string(source_json)
            integers_list.append(word_index)
        words_list = get_words_for_integers(integers_list)
        return self.delimiter.join(words_list)


def get_json_from_something(something):
    """
    Преобразуем нечто в JSON. Помня вредную привычку JSON::XS в Perl вызывать die() по любому поводу,
    на всякий случай, обернул код в try
    :param something:
    :return:
    """
    try:
        json_string = json.dumps(something)
    except:
        print("Obfuscation failed. Invalid input data :-P")
    return json_string

def get_int_from_string(string):
    """
    Получаем из строки числовой код. Делаем это следующим образом:
    Конкатенируем ASCII-коды всех символов строки, умножаем на её длину.
    Это делается для получения, по возможности, большого числа, преобразовать которое в исходную строку невозможно,
    даже зная её длину. Для получения числа, наименее зависимого от длины строки,
     а также для удобства последующего преобразования в слово, берём остаток от деления на 100 (кол-во слов в словаре)
    :param string:
    :return int:
    """
    string_length = len(string)
    chars_hash = 0
    for char in string:
        chars_hash += ord(char)
    final_int = (string_length * chars_hash) % 100
    return final_int

def hash_string(string):
    """
    Хешируем строку. Вначале хотел использовать свой аналог SHA1, но для простоты решил выполнить своеобразную "свёртку"
    Для потока символов мы выполняем сложение по модулю 2 бинарного представления каждого из них. То есть:
    Для каждого символа мы преобразуем в двоичный вид его ASCII-код. Выполняем сравнение по XOR с предыдущим символом,
    результат преобразуем сначала в есятичный вид, затем в ASCII-символ с идентичным кодом.
    Минус данного подхода в том, что A ^ B = C; A ^ C = B; B ^ C = A. То есть после N итераций, где N - число символов,
    мы получим исходную строку. Данная функция вызывается только для увеличения количества вариантов закодированных слов
    :param string:
    :return:
    """
    prev_char = string[0]
    string = string[1:]
    new_string = prev_char
    for char in string:
        new_char = chr(int(ord(char)) ^ int(ord(prev_char)))
        new_string += new_char
        prev_char = char
    return new_string

def get_words_for_integers(integers_list):
    """
    Имеем файл. В файле имеем 100 случайных слов (для их разнообразия решил взять их тут:
    https://www.randomlists.com/random-words) 100 слов выбрано, исходя из условия 1000000 уникальных вариантов для 3-х слов.
    Кубический корень из 1000000 = 100. Таким образом, при непрерывном равномерном распределении вариантов обфусцирования,
    вероятность нахождения коллизии - 1:1000000

     Открываем файл, выбираем слово по номеру строки, возвращаем список слов
    :param integers_list:
    :return:
    """
    dictionary = Dictionary.get_dictionary()
    words_list = []
    for integer in integers_list:
        words_list.append(dictionary[integer].capitalize())
    return words_list