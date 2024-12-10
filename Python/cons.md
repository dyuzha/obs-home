# Pip и venv
---
#### Просмотр версий
---
```bash
# Просмотр версий

py3 --version
pip3 --version
py3 -m pip --version

# Установка пакета
py3 -m pip install <mave-pkg>[=2.5.4] # версия
```

#### Проверка установленных пакетов
```bash
pip3 list
```

## Виртуальная среда
---
```bash
# Создание виртуальной среды 
py3 -m venv <name-venv>
  
# Активация/деактивация виртуальной среды
$ source <name-venv>/bin/activate
$ deactivate
```

## Перенос уст. пакетов в др. среду
---
- Виртуальная оболочка должна быть активирована

1) Экспортируем имена пакетов:
```bash
py3 -m pip freeze > pachages.txt
```
>[!Example] packeges.txt
```bash
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
requests==2.31.0
urllib3==2.0.5
```


https://pythoner.name/pip-venv
