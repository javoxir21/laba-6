#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
line = "hello жавохир пока world"
russian_words = " ".join(re.findall(r"[а-я ]+", line, re.I))
english_words = " ".join(re.findall(r"[a-z ]+", line, re.I))

# Так же чтобы удалить лишние пробелы можно использовать конструкцию:

russian_words = " ".join(russian_words.split()).strip()

print(russian_words)
print(english_words)

