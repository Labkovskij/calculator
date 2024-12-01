# test_string_inverter.py

import pytest
from app.string_inverter import invert_string

# Тест на правильність інвертування звичайного рядка
def test_invert_string_normal():
    assert invert_string("hello") == "olleh"

# Тест на порожній рядок
def test_invert_string_empty():
    assert invert_string("") == ""

# Тест на однорідний рядок (де всі символи однакові)
def test_invert_string_single_char():
    assert invert_string("aaaaa") == "aaaaa"

# Тест на рядок з пробілами
def test_invert_string_with_spaces():
    assert invert_string("hello world") == "dlrow olleh"

# Тест на рядок з чисел
def test_invert_string_with_numbers():
    assert invert_string("12345") == "54321"

# Тест на рядок з символами
def test_invert_string_with_special_chars():
    assert invert_string("!@# $%^") == "^%$ #@!"

# Тест на рядок з великими та малими літерами
def test_invert_string_case_sensitivity():
    assert invert_string("AbCdEfG") == "GfEdCbA"

# Тест на числовий рядок як ввід
def test_invert_string_numeric_input():
    assert invert_string("123abc") == "cba321"
