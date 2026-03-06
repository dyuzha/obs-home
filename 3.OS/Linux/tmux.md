---
id: tmux
aliases:
  - tmux
  - Tmux
tags: []
---

# Tmux
---
**Терминальный мультиплексер**

*Tmux сохраняет сессии даже после разрыва SSH-соединения, что делает его незаменимым для удалённой работы. 🚀*

```bash
# Создать новую сессию
tmux new -s <session_name>

# Показать все активные сесси
tmux ls

# Подключиться к сесси
tmux attach -t <session_name>

# Отсоедениться от сессии (оставить в фоне)
Ctrl + B, D

# Убить сессию
tmux kill-session -t <session_name>
```


 ## Окна (Windows)
 ---
-- Полноэкранные контейнеры (внутри которых мб панели)

Ctrl + B, _

| Command (_) | Action               |
|-------------|----------------------|
| C           | Create new window    |
| N           | Next window          |
| P           | Prev window          |
| 0-9         | to numb              |
| &           | close current window |


 ## Панели (Panes)
 ---
 -- Разделы внутри одного окна

 Ctrl + B, _

| Command (_) | Action              |
|-------------|---------------------|
| %           | Vertical split      |
| "           | Horizontal split    |
| <arches>    | Move beetwen panels |
| X           | Close current panel |
| Z           | Full display        |
| Q           | Show numbers        |


## Config
---
`~/.tmux.conf`

```bash
set -g prefix C-a
unbind C-b
bind C-a send-prefix
```
