---
tags:
  - bash
---


```
history
```
- histoty list
```
!<n_cmd>
```
 - input number command 
> [!Info]
> bash ~ !<n_cmd>!
> n_cmd m/b "-"

```
!<n_cmd>:p
```
- Выводит команду по номеру 
 
```
!*
```
- Подставляет аргументы последней команды


!:  <n_arg>
     0      	- commands
     $      	- last arg 
     ^      	- first arg 
	 2-3    	- range arg


Alt+.   		- ~analog. !$
Ctrl+r  		- find command 
        		- что бы отредактировать нажимаем -> или <- 
        		- Alt+r - Reset command after edit                 

| Ctrl+p | - Copy last command            |
| ------ | ------------------------------ |
| Ctrl+o | - Exec commands from clipboard |
| Ctrl+a | Begin string                   |
| Ctrl+e | End string                     |
| Ctrl+d | - delete right symbol          |
| Ctrl+b | -> symbols (alt = words)       |
Ctrl+f			<- symbols  

Ctrl+u			- Cut LEFT 
Ctrl+k			- Cut RIGHT
Ctrl+w 			- Cut WORD 

Ctrl+y   		- Insert  	

Ctrl+t			- Change 2 symbols (Alt = words)

```
cd -			
```
- Return dir ex 

```
^<old_arg>^<new_arg>
```
- change dir

