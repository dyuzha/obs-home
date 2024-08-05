> Back
> [[Lin]]
# Варианты 
---
```sh
cat /var/run/dmesg.boot | grep CPU:
```

```sh
grep CPU: /var/run/dmesg.boot
```

```sh
</var/run/dmesg.boot grep CPU:
```

>[!Info] Считать количество строк
>`wc -l` или `-c`

>[!Example] test.txt
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
Вывести весь файл
```sh
 grep ".*" test.txt
```

`-w` Позволяет искать по слову целиком:
>[!example] 
>**seven**eight one eight three
> sixteen seventeen eighteen **seven**
>        twenty **seven**


```sh
grep '\<seven' test.txt
```
- По началу слова

```sh
grep 'seven\>' test.txt
```
- По концу слова

```sh
grep '^seven' test.txt
```
- Стоящее в начале строки

```sh
grep 'seven$' test.txt
```
- Стоящее в конце строки

```sh
grep -C 1 twentyseven test.txt
```
- Строки в окрестности (+-1) искомого слова
	-B (Up)
	-A (Dowm)

```sh
grep "twenty[1-4]" test.txt
```
- включая данные строки

```sh
grep "twenty[^1-4]" test.txt
```
- исключая данные строки

 Источник: [Habr. Что такое grep и с чем его едят](https://habr.com/ru/articles/229501/)
