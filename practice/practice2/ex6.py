"""
Даны два слова. Напечатать только те буквы слов,  которые встречаются в обоих словах только один раз.
"""

words1 = input()
words2 = input()
common_letters = set(words1) | set(words2)
for letter in common_letters:
    if words1.count(letter) == 1 and words2.count(letter) == 1:
        print(letter)