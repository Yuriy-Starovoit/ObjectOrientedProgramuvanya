# Звіт до роботи
## Тема: Основи пайтон
### Мета роботи:Навчитись даним пайтон та створити програми
---
### Виконання роботи
-
1. Створив програму з допоиогою ChatGPT
```python
# Створення tuple та list
my_tuple = (1, 2, 3, 4, 5)
my_list = [6, 7, 8, 9, 10]

# Використання lambda-функції для додавання двох чисел
add_numbers = lambda x, y: x + y

# Створення set
my_set = set([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])

# Використання try-except для обробки помилки
try:
    result = 0
    for num in my_list:
        if num % 2 == 0:
            result += num
except TypeError as e:
    result = str(e)  # Зафіксуємо помилку у result

# Використання циклу for для виводу елементів tuple
for item in my_tuple:
    print(item)

# Використання циклу while для виводу елементів set
while len(my_set) > 0:
    element = my_set.pop()
    print(element)

# Вивід результату
print("Результат:", result)
```
2. Результат виконання програми:
-
![alt text](https://github.com/Yuriy-Starovoit/ObjectOrientedProgramuvanya/blob/main/2%D0%BB%D0%B0%D0%B1%D0%B0/pictures/%D0%B0%D0%B2%D1%96.png "Результат")
-
### Висновок
Я навчився використовувати дані мови програмування python, написав програму, де використав цикли та інші функції.
