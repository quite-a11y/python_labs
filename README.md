# python_labs
## Лабораторная работа 1

### Задание 1
```python
name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст:'))
print(f"Привет, {name}! Через год тебе будет {age+1}")
```
![Картинка 1](./images/lab01/task1.png)

### Задание 2
```python
a = input()
a2 = float(a.replace(',','.'))
b = input()
b2 = float(a.replace(',','.'))
print(f'sum={a2+b2:.2f}; avg={((a2+b2)/2):.2f}')
```
![Картинка 2](./images/lab01/task2.png)

### Задание 3
```python
price = float(input())
discont = float(input())
vat = float(input())
base = price * (1 - (discont/100))
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}₽ \n НДС: {vat_amount:.2f}₽ \n Итого к оплате: {total:.2f}₽')
```
![Картинка 3](./images/lab01/task3.png)

### Задание 4
```python
m = int(input())
print(f'{m//60}:{m%60}')
```
![Картинка 4](./images/lab01/task4.png)

### Задание 5
```python
name = input()
name2 = name.split()
print(f'Инициалы: {name2[0][0]+name2[1][0]+name2[2][0]}')
print(len(name2[0]) + len(name2[1]) + len(name2[2]) + 2)
```
![Картинка 5](./images/lab01/task5.png)

# python_labs
## Лабораторная работа 2

### Задание 1.1
```python
def min_max(arr):
    if len(arr) == 0:
        raise ValueError
    else:
        k = arr[0]
        k2 = arr[0]
        for i in arr:
            if i > k:
                k = i
            if i < k2:
                k2 = i
        return(k2,k)
```
![Картинка 1.1](./images/lab02/task1.png)

### Задание 1.2
```python
def unique_sorted(arr):
    if len(arr) == 0:
        return []
    else:
        arr2 = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    a = arr[i]
                    arr[i] = arr[j]
                    arr[j] = a
        for i in arr:
            if arr.count(i) == 1:
                arr2.append(i)
            elif arr.count(i) != 1:
                arr2.append(i)
        return arr2
```
![Картинка 1.2](./images/lab02/task1_2.png)

### Задание 1.3
```python
def flatten(arr):
    arr2 = []
    for i in arr:
        if isinstance(i,(tuple,list)):
            for j in i:
                arr2.append(j)
        else:
            raise TypeError
    return arr2
```
![Картинка 1.3](./images/lab02/task1_3.png)

### Задание 2.1
```python
def transpose(arr):
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if len(i) != len(arr[0]):
                raise ValueError
        arr2 = []
        for i in range(len(arr[0])):
            new = []
            for j in range(len(arr)):
                new.append(arr[j][i])
            arr2.append(new)
        return arr2
```
![Картинка 2.1](./images/lab02/task2.png)


### Задание 2.2
```python
def row_sums(arr):
    if len(arr) == 0:
        return []
    arr2 = []
    for i in range(len(arr)):
        if len(arr[i]) != len(arr[0]):
            raise ValueError
        else:
            arr2.append(sum(arr[i]))
    return arr2
```
![Картинка 2.2](./images/lab02/task2_2.png)

### Задание 2.3
```python
def col_sums(arr):
    if len(arr) == 0:
        return []
    for i in arr:
        if len(i) != len(arr[0]):
            raise ValueError
    a2 = []
    for i in range(len(arr[0])):
        s = 0
        for j in range(len(arr)):
            s += arr[j][i]
        a2.append(s)
    return a2
```
![Картинка 2.3](./images/lab02/task2_3.png)

### Задание 3
```python
def f(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio = ' '.join(fio.split()).strip()
    fio2 = fio.split()
    if len(fio2) < 2 or len(group.strip()) == 0 or gpa < 0:
        raise ValueError
    s = ''
    if len(fio2) == 3:
        s = f'{fio2[0].title()} {fio2[1][0].title()}.{fio2[2][0].title()}., '
    else:
        s = f'{fio2[0].title()} {fio2[1][0].title()}., '
    s += f'гр. {group}, '
    s += f'GPA {gpa:.2f}'
    return s

```
![Картинка 3](./images/lab02/task_3.png)

# python_labs
## Лабораторная работа 3

### Задание 1.1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    for i in ["\t", "\n", "\r"]:
        text = text.replace(i, ' ')
    text = ' '.join(text.split()).strip()
    return text

```
![Картинка 1](./images/lab03/task1_1.png)

### Задание 1.2
```python
def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return findall(r'\w+(?:-\w+)*', text)

```
![Картинка 2](./images/lab03/task1_2.png)

### Задание 1.3-1.4
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    a = {}
    for i in tokens:
        a[i] = tokens.count(i)
    return a 

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items = sorted(items, key=lambda l: (-l[1], l[0]))
    return items[:n]
```
![Картинка 3](./images/lab03/task1_3.png)

### Задание 2
```python
import sys
from text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read()
nt = normalize(text)
t = tokenize(nt)
f = count_freq(t)
top_words = top_n(f, 5)

print(f"Всего слов: {len(t)}")
print(f"Уникальных слов: {len(f)}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}: {count}")
```
![Картинка 4](./images/lab03/task2.png)