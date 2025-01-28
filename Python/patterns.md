---
id: patterns
aliases: []
tags: []
---

1. **Factory Method** — позволяет создавать объекты, не привязываясь к конкретным классам.

2. **Builder** — используется для создания сложных объектов шаг за шагом. В вашем случае это может помочь в создании архива с различными настройками сжатия и другими параметрами.

3. **Iterator** — предоставляет возможность перебора элементов коллекции без раскрытия её внутреннего представления. Это может упростить работу с архивами, позволяя легко перебирать их содержимое.

4. **Decorator** — добавляет поведение к существующему объекту без изменения его структуры. В контексте вашего кода это может позволить добавлять дополнительные функции к архивам, такие как шифрование или сжатие.

5. **Singleton** — гарантирует, что существует только один экземпляр класса. Это может быть полезным для управления общими ресурсами, такими как папка результатов.

**Применение паттернов к коду:**

1. *Factory Method:*

   * Создайте базовый класс `ArchiveBuilder`, который определяет общие методы для работы с архивами.
   * Реализуйте подклассы для различных типов архивов (`ZipFile`, `RarFile` и т. д.), которые наследуют от `ArchiveBuilder`.
   * В вашем основном коде используйте фабричный метод для создания нужного типа архива.

2. *Builder:*

   * Определите интерфейс `ArchiveBuilderInterface` с методами для настройки параметров архива.
   * Реализуйте класс `DefaultArchiveBuilder`, который использует `ZipFile`.
   * Предоставьте возможность настройки параметров через интерфейс `ArchiveBuilderInterface`.

3. *Iterator:*

   * Преобразуйте ваш код в итератор, который будет перебирать файлы в папке и добавлять их в архив.
   * Используйте методы `__iter__` и `__next__` для реализации итератора.

4. *Decorator:*

   * Создайте декоратор `ArchiveDecorator`, который принимает экземпляр `ArchiveBuilder` и добавляет дополнительные функции.
   * Например, вы можете добавить шифрование, сжатие и другие параметры.

5. *Singleton:*

   * Объявите класс `ResultsFolder` как синглтон.
   * Гарантируйте, что будет создана только одна папка результатов, независимо от количества вызовов.

Пример применения этих паттернов может выглядеть следующим образом:
```python
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path, PurePath
from abc import ABC, abstractmethod

class ArchiveBuilder(ABC):
    @abstractmethod
    def build_archive(self, files):
        pass

class DefaultArchiveBuilder(ArchiveBuilder):
    def __init__(self, compression=ZIP_DEFLATED, allow_zip64=True):
        self.compression = compression
        self.allow_zip64 = allow_zip64

    def build_archive(self, files):
        with ZipFile(archive_path, mode="w", compression=self.compression,
                     allowZip64=self.allow_zip64) as myzip:
            for file in files:
                myzip.write(file)

class ResultsFolder(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def create_folder(self):
        TARGET / Path(TICKET).mkdir()

class TemplateProcessor(object):
    def process_templates(self, templates):
        for template in templates:
            archive_path = Path(TARGET / Path(template + ".zip"))
            databases = self.get_databases(template)
            self.create_archive(databases, archive_path)

    def get_databases(self, template):
        databases = list()  # Список информационных баз из шаблона
        with open(Path(TEMPLATES / template), 'r') as file:
            for line in file.readlines():
                line = line[:-1]
                databases.append(line)
        return databases

    def create_archive(self, databases, archive_path):
        builder = DefaultArchiveBuilder()
        for db_name in databases:
            file = Path(DATA / db_name)
            builder.build_archive([file])

if __name__ == "__main__":
    results_folder = ResultsFolder()
    results_folder.create_folder()
    processor = TemplateProcessor()
    processor.process_templates(["pat_2", "pat_3"])
```
Этот код демонстрирует использование нескольких паттернов для улучшения структуры и гибкости вашего приложения.
