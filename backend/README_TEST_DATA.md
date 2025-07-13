# Создание тестовых карт скорой помощи

Этот скрипт создает тестовые карты скорой помощи в базе данных для разработки и тестирования.

## Требования

- Пользователь с ID = 32 должен существовать в базе данных
- Профиль с ID = 15 должен существовать в базе данных
- Django проект должен быть настроен

## Использование

### Способ 1: Прямой запуск
```bash
cd backend
python create_test_cards.py
```

### Способ 2: Через Django manage.py
```bash
cd backend
python manage.py shell
```

В shell выполните:
```python
from create_test_cards import create_test_cards
create_test_cards()
```

### Способ 3: Простой скрипт
```bash
cd backend
python run_test_data.py
```

## Что создается

Скрипт создает:

1. **5 пациентов** с разными данными
2. **3 карты скорой помощи** с полными данными:
   - Карта 1001: ОРВИ (умеренная тяжесть)
   - Карта 1002: Острый коронарный синдром (тяжелое состояние)
   - Карта 1003: Сотрясение головного мозга (умеренная тяжесть)

### Для каждой карты создаются:
- ✅ Основная карта (Card)
- ✅ Данные о времени (DateTimeData)
- ✅ Общие сведения (CommonData)
- ✅ Показатели до лечения (ParametersBefore)
- ✅ Кожные покровы (SkinData)
- ✅ Дыхательная система (AirData)
- ✅ Сердечно-сосудистая система (HeartData)
- ✅ Живот (StomachData)
- ✅ Нервная система (NervousData)
- ✅ Мочеполовая система (UrinaryData)
- ✅ ЭКГ данные (ECGData)
- ✅ Данные о помощи (AIDData)
- ✅ Показатели после лечения (ParametersAfter)
- ✅ Диагноз (DiagnosisData)

## Проверка результатов

После выполнения скрипта вы можете проверить созданные данные:

```python
from card.models import Card
from user.models import Profile

# Проверить количество карт
print(f"Всего карт: {Card.objects.count()}")

# Проверить карты конкретного врача
user = User.objects.get(id=32)
print(f"Карт у врача {user.username}: {user.doctor_cards.count()}")

# Посмотреть детали карты
card = Card.objects.get(id=1001)
print(f"Карта {card.id}: {card.cause}")
print(f"Пациент: {card.patient_id.get_full_name()}")
```

## Настройка

Если нужно изменить ID пользователя или профиля, отредактируйте файл `create_test_cards.py`:

```python
# Изменить эти строки:
user = User.objects.get(id=32)  # Ваш ID пользователя
profile = Profile.objects.get(id=15)  # Ваш ID профиля
```

## Удаление тестовых данных

Для удаления всех тестовых карт:

```python
from card.models import Card
Card.objects.filter(id__in=[1001, 1002, 1003]).delete()
```

## Структура файлов

- `create_test_cards.py` - Основной скрипт создания данных
- `run_test_data.py` - Простой скрипт для запуска
- `README_TEST_DATA.md` - Эта инструкция 