---
id: archive
aliases: []
tags: []
---
**Back**
    [[!Lin]]

В линукс отдельно выполняется
1. Архивация (tar)
2. Сжатие (zip, bz, xz, lzma и тд)

## Tar
---
**Стандартная утилита для архивации в Linux**

```bash
# Создание архива
tar -cvf archive.tar /path/to/files
  # -c - создание архива (Create)
  # -v - показать подробную информацию о процессе работы
  # -f - файл для записи архива

# Создание сжатого архива gzip
tar -zcvf archive.tar.gz /path/to/files
  # -z - шифрование gzip
  # -j - шифрование bzip

# Распаковка архива
tar -xvf archive.tar
  # -x - извлечь файлы из архива (eXtract)

# Распаковка сжатого архива gzip
tar -zxvf archive.tar.gz

# Добавить фойл в архив
tar -rvf archive.tar file.txt

# Извлечь фойл из архива
tar -xvf archive.tar file.txt

# Извлечь файлы по шаблону соответсвия
tar -xvf archive.tar --wildcards'*.php'

# Изменить папку для распокавки
tar -xvf archive.tar -C /path/to/dir # (Default ./)
```

## Альтернативные способы
---
```bash
# Создание архива
tar -cvf archive.tar /path/to/file

# Сжатие архива с помощью утилилиты gzip
gzip archive.tar

# Убрать сжатие
gunzip archive.tar.gz
```
