#!/usr/bin/env python3
# -*- coding: utf-8 -*-


word1 = "password"
word2 = "pillow"
# приводим каждое из слов множеству и находим пересичение этих множеств
common_letters = set(word1) & set(word2)
# получили множество букв, которые есть в обоих словах
# в данном случае это {'p', 'o', 'w'}
# выводим размер множества (т.е. количество совпадающих букв):
print(len(common_letters))
print(common_letters) # просто выводим совпадающие буквы в виде множества
print(', '.join(common_letters)) # выводим буквы через запятую