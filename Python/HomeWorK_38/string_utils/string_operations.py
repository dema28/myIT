"""Напишите функцию reverse_string(s), которая принимает строку и возвращает её
перевёрнутый вариант.
Напишите функцию capitalize_words(s), которая принимает строку и делает
первую букву каждого слова заглавной.
"""

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return' '.join(word.capitalize() for word in s.split())



