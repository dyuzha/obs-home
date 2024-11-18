**Back**
  [[CLI]]

transmission-cli - CLI for torrent client 

**browser-sync**

```bash
# Установка
npm install -g browser-sync
# -g - globally

# Запуск
browser-sync start --server --files .

# Рекомендация
alias serce="browser-sync start --server --files ."

# In order to access the server inside private network and test the webpage on several devices.
# browser-sync config
# Get the current local IP address
export SERVER_IP=`hostname -I`

# The command alias to start the browser-sync server
alias serve="browser-sync start --server -b vimb --files . --no-notify --host $SERVER_IP --port 9000"
```
