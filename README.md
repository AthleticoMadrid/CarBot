# Проект CarBot

CarBot - это бот для Telegram, который отправляет пользователю фото автомобиля и считывает геоданные пользователя

## Установка

1. Клонируйте репозиторий с GitHub
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = "API-ключ бота"
PROXY_URL = 'Адрес прокси'
PROXY_USERNAME = 'Логин на прокси'
PROXY_PASSWORD = 'Пароль на прокси'
USER_EMOJI = [':car:', ':taxi:', ':oncoming_taxi:', ':red_car:', ':blue_car:']
```
6. Запустите бота командой `python botTwo.py`
