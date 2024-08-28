**Back**
- [[py-modules]] [тык](py-modules.md)

**More**
- [[zip]] [тык](zip.md)

Источник: [Metanit - запись и чтение архивных zip-файлоф](https://metanit.com/python/tutorial/4.7.php)
# Class ZipFile
---
## Параметры
---
- `file` - puth/to/file
- `mode`: r / w / a (adding to file)
- `compression` - тип сжатия файла
    - `ZIP_STOREDA`: архивация без сжатия (знач. по умолч.)
    - `ZIP_DEFLATED`: стандартный тип сжатия при архивации в `zip`
    - `ZIP_BZIP2`: архивация без сжатия (знач. по умолч.)
    - `ZIP_LZMA`: архивация без сжатия (знач. по умолч.)
- `allowZip64`: если равно *True*, то *zip*-файл мб больше 4гб
- `compresslevel`: уровень сжатия при записи файла. 
    - Для типов сжатия ZIP_STORED и ZIP_LZMA не применяется.
    - Для типа zip_deflated доп. знач. [0-9]
    - Для типа zip_ BZIP доп. знач. [1-9]
- `strict_timestamps`: при значении **False** позволяет работать c *zip*-файлами ранее 01.01.1980 и позже 31.12.2107
- `metadata_encoding`: применяется для декодирования метаданных *zip*-файла (например, коментариев)

## Metods
---
- `close()` - закрывает *zip*-файл
- `getinfo()`: возвращает информацию об одном файле из архива в виде объекта **ZipInfo**
- `namelist()`: возвращает список файлов архива
- `infolist()`: возвращает информацию обо всех файлах из архива в виде списка объектов **ZipInfo**
- `open()`: предоставляет доступ к одному из файлов в архиве
- `read()`: считывает файл из архива в набор байтов
- `extract()`: извлекает из архива один файл
- `extractall()`: извлекает из архива все элементы
- `setpassword()`: кто-бы мог подумать...extractall().
- `printdir()`: выводит на консоль содержимое архива


# Действия
---
### Create and close file
---
```python
from zipfile import ZipFile

myzip = ZipFile("metanit.zip", "w")
myzip.close()
```
- `close()` - обязательно

Альтернатива:
```python
with ZipFile("metanit.zip", "w") as myzip:
    pass
```
### Writing file
---
```python
write(filename, 
      arcname=None,         # произвольное имя для файла внутри архива
      compress_type=None,   
      compresslevel=None)`
```






