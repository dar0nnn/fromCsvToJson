# from csv to json

### Тестовое задание:

Нужно перевести данные о командах и юзерах в формат Json вида:

```JSON
{
    "commands": [
        {
            "function": "foo1", 
            "name": "test1", 
            "param": [
                {
                    "user": "user1"
                }, 
                {
                    "user": "user2"
                }
            ], 
            "module": "module1"
        }
    ]
}```

Данные поступают из трех csv файлов вида:

| module | name | function |
| ------ | ---- | -------- | 
| module1 | test1 | foo1 |
| module1 | test2 | foo2 |
| module2 | test3 | foo3 |