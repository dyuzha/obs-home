>Back

>[[Git]]

1. Сгенерироватьu ssh-ключ
>[!example]
```shell
ssh-keygen -t ed25519 -c "your_email@example.com"
```
2. Добавить *ssh* ключ.pub на *Github*
3. Отредактировать *config*  в ~/.ssh
>[!~/.ssh/config]
```shell
Host [host-name] 
	HostName github.com
	IdentityFile ~/.ssh/[secret-key-name]
	IdentitiesOnly yes
```
4. Создать репозиторий на *Github*
5. В инициализированном *git*-репозитории написать 
>[!example]
```shell
git push --set-upstream git@[host-name]:[dyuzha/me.git] master
```
