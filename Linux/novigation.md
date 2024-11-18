**back**
     [[CLI]]

# Навигация

## Статический режим
```bash
# Выводит историю команд
history
histoty list

# Вызывает команду по номеру из истории
!<№_cmd>

# Можно использовать для того чтобы дополнить предыдущую команду
sudo !<№_cmd> | tail 

# Можно обращаться к команде по отрицательному индексу
sudo !<-№_cmd> | tail 
#zsh автоматически заменит конструкцию !<№> на команду, после нажатия на пробел

# Выведет команду по номеру 
!<№_cmd>:p

# Подставляет аргументы последней команды
!*

# Подставляет аргумент (по его номеру) предыдущей команды
!:<№_arg>

# Подставит саму команду
!:0 

# Последний аргумент
!:$  

# Первый аргумент
!:^ 

# Диапазон аргументов
!:2-5 

```

## Итерактивный режим
---
```bash
# Листает команды в обратном направлении
# Можно использовать в середине команды
Alt + .  		

# Поиск команды
Ctrl + r
# что бы отредактировать нажимаем -> или <- 
# Alt+r - Reset command after edit                 
```

| Cmd    | Description                      |
| ------ | -------------------------------- |
| Ctrl+p | - Copy last command              |
| Ctrl+o | - Exec commands from clipboard   |
| Ctrl+a | - Begin string                   |
| Ctrl+e | - End string                     |
| Ctrl+d | - delete right symbol            |
| Ctrl+b | - -> symbols (alt = words)       |
| Ctrl+f | - <- symbols                     |
| Ctrl+u | - Cut LEFT                       |
| Ctrl+k | - Cut RIGHT                      |
| Ctrl+w | - Cut WORD                       |
| Ctrl+y | - Insert                         |
| Ctrl+t | - Change 2 symbols (Alt = words) |
| Ctrl+l | - Clean terminal                 |
| Ctrl+v | - Ввод следующего символа        |


```bash
# Я не знаю что это и откуда это
^<old_arg>^<new_arg>
```
