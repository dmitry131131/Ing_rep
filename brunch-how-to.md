# Как добавить работать с GitHub по SSH

### Создание SSH ключа

В терминале набираем команду:

```bash
    ssh-keygen -t ed25519 -C "имя.фамилия@phystech.edu"
```


```bash
    eval "$(ssh-agent -s)"
```

И пишем команду:

```bash
    ssh-add ~/.ssh/id_ed25519
```

Она должна вернуть: `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`