---
id: gpg_cli
aliases:
  - gpg_cli
tags: []
---

# gpg_cli
---
```bash
gpg -c file.txt  # Зашифрует с паролем (симметричное шифрование)
gpg -e -r user@example.com file.txt  # Зашифрует открытым ключом получателя
gpg --full-generate-key  # Создаст пару RSA (публичный + приватный ключ)
gpg --sign file.txt  # Создаст подпись
```

