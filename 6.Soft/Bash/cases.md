---
id: cases
aliases:
  - Добавляем папку bin в переменную PATH
tags: []
---

## Устанавливаем права доступа к скопированным файлам и папкам

```bash
find "$HOME" -type f -exec chmod 644 {} \;
find "$HOME" -type d -exec chmod 755 {} \;
```


## Добавляем папку bin в переменную PATH
```bash
export PATH="$PATH:$HOME/.dotfiles/bin"
```


## Дозаписать в файл с правими root
---
```bash
echo "some text" | sudo tee -a /file/with/sudo/permited
# or
sudo sh -c `echo "some text" >> /file/with/sudo/permited`
```
