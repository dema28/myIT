"""Используйте функции из этих модулей для обработки и анализа строки, введённой
пользователем."""
from HomeWork_38.string_utils.string_analysis import count_vowels, count_char
from HomeWork_38.string_utils.string_operations import reverse_string, capitalize_words



input_user = input("Введите текст: ")

rev_str = reverse_string(input_user)
print(f"Перевернутая строка: {rev_str}")

capitalize_str = capitalize_words(input_user)
print(f"Строка с заглавной первой буквой каждого слова: {capitalize_str}")

vow_count = count_vowels(input_user)
print(f"Количество гласных букв в тексте: {vow_count}")

char_count = count_char(input_user)
print(f"Количество букв в тексте: {char_count}")