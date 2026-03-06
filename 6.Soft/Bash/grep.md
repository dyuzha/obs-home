---
id: grep
aliases:
  - Syntax
tags: []
---

**Back**
 [[!Lin]]

# Syntax
---
```bash
grep -ri <pattern> path/to/file # поиск файла по содержимому
		-r 			# Рекурсивный обход
		-i 			# Case ignor
```

# Варианты
---
```bash
cat /var/run/dmesg.boot | grep CPU:
grep CPU: /var/run/dmesg.boot
</var/run/dmesg.boot grep CPU:
```

>[!Info] Считать количество строк
>`wc -l <target>` или `-c`

>[!Summary] test.txt
```
one two three
seven eight one eight three
thirteen fourteen fifteen

 sixteen seventeen eighteen seven
sixteen seventeen eighteen
        twenty seven
one 504 one
one 503 one
one     504     one
one     504 one
#comment UP
twentyseven
        #comment down
twenty1
twenty3
twenty5
twenty7
```

```bash
Вывести весь файл
grep ".*" test.txt
```

`-w` Позволяет искать по слову целиком:
>[!example]
>**seven**eight one eight three
> sixteen seventeen eighteen **seven**
>        twenty **seven**


```bash
# По началу слова
grep '\<seven' test.txt

# По концу слова
grep 'seven\>' test.txt

# Стоящее в начале строки
grep '^seven' test.txt

# Стоящее в конце строки
grep 'seven$' test.txt

# Строки в окрестности (+-1) искомого слова
grep -C 1 twentyseven test.txt

# Строки сверху (+1) искомого слова
grep -B 1 twentyseven test.txt

# Строки снизу (-1) искомого слова
grep -A 1 twentyseven test.txt

# включая данные строки
grep "twenty[1-4]" test.txt

# исключая данные строки
grep "twenty[^1-4]" test.txt
```

source: [Habr. Что такое grep и с чем его едят](https://habr.com/ru/articles/229501/)
