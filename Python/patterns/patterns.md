---
id: patterns
aliases: []
tags: []
---
**Back**
    [[!Python]]

## Patterns
---

[[factory_pattern]] — Создает готовые объекты, скрывая детали реализации, не привязываясь к конкретным классам.

[[builder_pattern]] — используется для создания сложных объектов шаг за шагом.


3. **Iterator** — предоставляет возможность перебора элементов коллекции без раскрытия её внутреннего представления

4. **Decorator** — добавляет поведение к существующему объекту без изменения его структуры.

5. **Singleton** — гарантирует, что существует только один экземпляр класса.


**Применение паттернов к коду:**

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
