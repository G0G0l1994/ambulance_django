# Медицинские константы для карт скорой помощи

# Общее состояние пациента
GENERAL_ASSESSMENT_CHOICES = [
    ('satisfactory', 'Удовлетворительное'),
    ('moderate', 'Средней степени тяжести'),
    ('severe', 'Тяжелое'),
    ('terminal', 'Терминальное'),
]

# Сознание пациента
CONSCIOUSNESS_CHOICES = [
    ('clear', 'Ясное'),
    ('confused', 'Оглушение'),
    ('stupor', 'Сопор'),
    ('coma', 'Кома'),
]

# Положение тела
BODY_POSITION_CHOICES = [
    ('active', 'Активное'),
    ('passive', 'Пассивное'),
    ('forced', 'Вынужденное'),
]

# Кожные покровы - сухость
SKIN_DRYNESS_CHOICES = [
    ('dry', 'Сухие'),
    ('moist', 'Влажные'),
]

# Цвет кожных покровов
SKIN_COLOR_CHOICES = [
    ('normal', 'Обычной окраски'),
    ('pale', 'Бледные'),
    ('hyperemic', 'Гиперемированные'),
    ('cyanotic', 'Цианоз'),
]

# Типы сыпи
RASH_CHOICES = [
    ('none', 'Нет'),
    ('petechial', 'Петехиальная'),
    ('pustular', 'Пустулёзная'),
    ('vesicular', 'Везикулярная'),
    ('nodular', 'Узелковая'),
    ('other', 'Другое'),
]

# Состояние зева
THROAT_CHOICES = [
    ('calm', 'Спокоен'),
    ('hyperemic', 'Гиперемирован'),
]

# Типы отеков
SWELLING_CHOICES = [
    ('none', 'Нет'),
    ('legs', 'Голени'),
    ('face', 'Лицо'),
    ('torso', 'Туловище'),
    ('arms', 'Руки'),
]

# Типы дыхания
RESPIRATORY_TYPE_CHOICES = [
    ('vesicular', 'Везикулярное'),
    ('hard', 'Жёсткое'),
    ('bronchial', 'Бронхиальное'),
    ('puerile', 'Пуэриальное'),
    ('weakened', 'Ослабленное'),
    ('absent', 'Отсутствует'),
]

# Типы хрипов
WHEEZING_CHOICES = [
    ('none', 'Нет'),
    ('wet', 'Влажные'),
    ('dry', 'Сухие'),
]

# Типы одышки
DYSPNEA_CHOICES = [
    ('none', 'Нет'),
    ('inspiratory', 'Инспираторная'),
    ('expiratory', 'Экспираторная'),
    ('mixed', 'Смешанная'),
]

# Тоны сердца
TONE_OF_HEART_CHOICES = [
    ('clear', 'Ясные'),
    ('muffled', 'Глухие'),
    ('dull', 'Приглушены'),
    ('absent', 'Отсутствуют'),
]

# Типы шумов сердца
MURMUR_CHOICES = [
    ('none', 'Нет'),
    ('systolic', 'Систолический'),
    ('diastolic', 'Диастолический'),
    ('pericardial_friction', 'Трения перикарда'),
    ('other', 'Другое'),
]

# Ритм тонов сердца
RHYTHMIC_TONE_CHOICES = [
    ('rhythmic', 'Ритмичный'),
    ('arrhythmic', 'Аритмичный'),
]

# Ритм пульса
RHYTHMIC_PULSE_CHOICES = [
    ('rhythmic', 'Ритмичный'),
    ('arrhythmic', 'Аритмичный'),
]

# Характеристики пульса
CHARACTERISTIC_PULSE_CHOICES = [
    ('normal', 'Нормальный'),
    ('weak_filling', 'Слабого наполнения'),
    ('tense', 'Напряжённый'),
    ('threadlike', 'Нитевидный'),
    ('absent', 'Отсутствует'),
]

# Болезненность живота
PAIN_STOMACH_CHOICES = [
    ('painless', 'Безболезненный'),
    ('painful', 'Болезненный'),
]

# Характеристика живота
CHARACTERISTIC_STOMACH_CHOICES = [
    ('soft', 'Мягкий'),
    ('tense', 'Напряжён'),
    ('bloated', 'Вздут'),
]

# Типы стула
FORMED_TYPE_STOOL_CHOICES = [
    ('formed', 'Оформлен'),
    ('loose', 'Разжижен'),
    ('liquid', 'Жидкий'),
    ('absent', 'Отсутствует'),
]

# Регулярность стула
REGULAR_STOOL_CHOICES = [
    ('regular', 'Регулярный'),
    ('irregular', 'Нерегулярный'),
    ('absent', 'Отсутствует'),
]

# Поведение пациента
BEHAVIOUR_CHOICES = [
    ('calm', 'Спокойное'),
    ('excited', 'Возбуждённое'),
    ('aggressive', 'Агрессивное'),
    ('depressive', 'Депрессивное'),
]

REACTION_TO_LIGHT = [
    ('yes','Есть'),
    ('no','Отсутствует')
]

# Состояние зрачков
PUPILS_OF_THE_EYES_CHOICES = [
    ('normal', 'Нормальные'),
    ('wide', 'Широкие'),
    ('narrow', 'Узкие'),
]

# Речь пациента
SPEECH_CHOICES = [
    ('clear', 'Внятная'),
    ('aphasia', 'Афазия'),
    ('dysarthria', 'Дизартрия'),
]

# Параличи и парезы
PARALYSIS_CHOICES = [
    ('none', 'Нет'),
    ('right', 'Справа'),
    ('left', 'Слева'),
]

# Чувствительность
SENSITIVE_CHOICES = [
    ('preserved', 'Сохранена'),
    ('absent', 'Отсутствует'),
    ('reduced', 'Снижена'),
    ('left', 'Слева'),
    ('right', 'Справа'),
]

# Болезненность мочеиспускания
PAINLESS_URINATION_CHOICES = [
    ('painless', 'Безболезненное'),
    ('painful', 'Болезненное'),
]

# Характеристика мочеиспускания
CHARACTERISTIC_URINATION_CHOICES = [
    ('free', 'Свободное'),
    ('difficult', 'Затруднено'),
    ('absent', 'Отсутствует'),
]

# Симптом поколачивания почек
KIDNEY_PUNCH_CHOICES = [
    ('negative_both', 'Отрицательный с обеих сторон'),
    ('positive_left', 'Положительный слева'),
    ('positive_right', 'Положительный справа'),
    ('positive_both', 'Положительный с обеих сторон'),
    ('weak_positive_left', 'Слабоположительный слева'),
    ('weak_positive_right', 'Слабоположительный справа'),
    ('weak_positive_both', 'Слабоположительный с обеих сторон'),
]

# Характеристика мочи
CHARACTERISTIC_URINE_CHOICES = [
    ('light_yellow', 'Светло-жёлтая'),
    ('cloudy', 'Мутная'),
]

AID_EFFECTS = [
    ('improvement','Улучшение'),
    ('worsening','Ухудшение'),
    ('no_effects','Без эффекта')

]

# Статусы карт
CARD_STATUS_CHOICES = [
    ('created', 'Создана'),
    ('handed_crew', 'Передана бригаде'),
    ('in_progress', 'Принята'),
    ('hospital', 'Госпитализация'),
    ('completed', 'Завершена'),
    ('cancelled', 'Отменена'),
]

# Роли пользователей
USER_ROLE_CHOICES = [
    ('doctor', 'Врач'),
    ('paramedic', 'Фельдшер'),
    ('dispatcher', 'Диспетчер'),
    ('admin', 'Администратор'),
]

# UI состояния
UI_CHOICES = {
    'LOADING_STATES': [
        ('idle', 'Ожидание'),
        ('loading', 'Загрузка'),
        ('success', 'Успех'),
        ('error', 'Ошибка'),
    ],
    
    'FORM_MODES': [
        ('create', 'Создание'),
        ('edit', 'Редактирование'),
        ('view', 'Просмотр'),
    ],
}

# Значения по умолчанию
DEFAULT_VALUES = {
    'glasgow_scale': 15,
    'temperature_before': 36.6,
    'temperature_after': 36.6,
    'respiratory_rate_before': 16,
    'respiratory_rate_after': 0,
    'saturation_before': 98,
    'saturation_after': 98,
    'heartbite_before': 60,
    'heartbite_after': 60,
    'pulse_before': 60,
    'pulse_after': 60,
    'blood_pressure_systolic_before': 120,
    'blood_pressure_systolic_after': 120,
    'blood_pressure_diastolic_before': 80,
    'blood_pressure_diastolic_after': 80,
    'normal_blood_pressure_systolic': 120,
    'normal_blood_pressure_diastolic': 80,
    'blood_glucose_before': 4.0,
    'blood_glucose_after': 4.0,
    'rate_stool': 1,
    'jaundice': 'Нет',
    'tonsils': 'Не увеличены',
    'lymph_nodes': 'Не увеличены',
    'wheezing_localisation': 'Нет хрипов',
    'heart_tone_accent': 'Нет',
    'liver': 'Не увеличена',
    'reaction_to_light': 'Есть',
}

# Валидационные ограничения
VALIDATION_LIMITS = {
    'glasgow_scale': {'min': 3, 'max': 15},
    'temperature': {'min': 30.0, 'max': 45.0},
    'respiratory_rate': {'min': 0, 'max': 100},
    'saturation': {'min': 0, 'max': 100},
    'heart_rate': {'min': 0, 'max': 300},
    'blood_pressure_systolic': {'min': 50, 'max': 300},
    'blood_pressure_diastolic': {'min': 30, 'max': 200},
    'blood_glucose': {'min': 0.0, 'max': 50.0},
    'rate_stool': {'min': 0, 'max': 20},
}