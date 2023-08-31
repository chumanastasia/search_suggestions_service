# Сервис поиска подсказок Wizard_entity в поисковых запросах

## Инструкция по установке

1. Склонируйте репозиторий
```bash
git clone https://github.com/chumanastasia/search_suggestions_service.git
```

2. Добавьте в корень проекта файл .env с переменными окружения
```bash
DSN="redis://redis:6379"
TTL=86400
PORT=8000
HOST="0.0.0.0"
```

3. Запустите docker-compose
```bash
docker-compose up -d --build
```

4. Готово! Сервис доступен по адресу http://{host}:{port}
