#!/bin/sh

set -e

echo $INITIAL_SETUP
echo $STATIC

if [ ! -f "/backend/db_data/db.sqlite3" ]; then
    INITIAL_SETUP=true
fi
python manage.py shell -c "from django.conf import settings;import pprint; print(settings.DATABASES)"


echo "Запускаю миграцию..."
python manage.py migrate
echo "конец миграции"

if [ "$INITIAL_SETUP" = true ]; then
    echo "Наполняю базу данных..."
    python manage.py load_mkb
    python create_test_data.py  
    INITIAL_SETUP=false  
fi
if [ ! -f "/backend/staticfiles" ]; then
    STATIC=false
fi

if [ "$STATIC" = true ]; then
    echo "Собираем статику"
    python manage.py collectstatic --noinput
    STATIC=true
fi

echo "Запуск сервера Daphne"

exec "$@"