![image](https://github.com/user-attachments/assets/62018770-4c1b-40cc-aca1-475469befbb0)

# Первый запуск postgres 

 `sudo -iu postgres`

## Для русской локали 

`initdb --locale=ru_RU.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data --data-checksums`

# Создаем юзверя

`createuser -W --interactive` 

-W пароль. 
user к примеру testrole

## Создаем нашу базу
`psql -U postgres`

`CREATE DATABASE bot1;`

### Передаем права к доступу от суперюзера нашему "обычному" юзеру

`ALTER DATABASE bot1 OWNER TO testrole;`

#### Создаем таблицу данных 
``CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50),
  first_name VARCHAR(50)
);``

![image](https://github.com/user-attachments/assets/969e77fd-1202-4142-a45e-83f858c90f80)








 
