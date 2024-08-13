from django import forms


class CardForms(forms.Form):
    last_name = forms.CharField('Фамилий', max_length=100)
    first_name = forms.CharField('Имя', max_length=100)
    surname = forms.CharField('Отчество', max_length=100)
    date_of_birth = forms.DateField('Дата рождения', input_formats='DD.MM.YYYY')
    address = forms.CharField('Адрес', widget=forms.Textarea, max_length=200)
    cause = forms.CharField('Повод к вызову', widget=forms.Textarea, max_length=200)
    status = forms.SelectMultiple("Статус вызова", choices=[("Принят","Принят"),
                                                            ("Назначен бригаде","Назначен бригаде"), 
                                                            ("Завершен","Завершен"),
                                                            ("Отменён","Отменён")], 
                                                            initial=("Принят"))
    crew = forms.SelectMultiple('Бригада', choices=[('crew1','crew1'),('crew2','crew2')])
    # times
    time_of_receipt = forms.DateTimeField('Время приема', format='%H:%M')
    transmission_time = forms.DateTimeField('Время передачи', format='%H:%M')
    departure_time = forms.DateTimeField('Время принятия вызова', format='%H:%M')
    arrival_time = forms.DateTimeField('Время прибытия', format='%H:%M')
    start_time_of_hospitalization = forms.DateTimeField('Время начала госпитализации', format='%H:%M')
    time_of_arrival_at_hospital = forms.DateTimeField('Время прибытия в стационар', format='%H:%M')
    call_end_time = forms.DateTimeField('Окончание вызова', format='%H:%M')
    complaints = forms.CharField('Жалобы', widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Жалобы пациента..."}))
    anamnesis = forms.CharField('Анамнез',widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Анамнез"}))
    general_assessment = forms.SelectMultiple('Общее состояние', choices=[("Удовлетворительное", "Удовлетворительное"), 
                                                                          ("Средней степени тяжести", "Средней степени тяжести"), 
                                                                          ("Тяжелое", "Тяжелое"), 
                                                                          ("Терминальное", "Терминальное")], 
                                                                    initial=("Удовлетворительное"))
    сonsciousness = forms.SelectMultiple('Сознание', choices=[("Ясное", "Ясное"), 
                                                              ("Оглушение", "Оглушение"), 
                                                              ("Сопор", "Сопор"), 
                                                              ("Кома", "Кома")], 
                                                              initial=("Ясное"))
    glasgow_scale = forms.IntegerField('Шкала Глазго',initial=15)


    body_position = forms.SelectMultiple("Положение тела", choices=[("Активное", "Активное"), 
                                                                    ("Пассивное", "Пассивное"), 
                                                                    ("Вынужденное", "Вынужденное")], 
                                                                    initial=("Активное"))
    temperature_before = forms.FloatField("Температура тела", initial=36.6)
    respiratory_rate_before = forms.IntegerField("ЧДД", initial=16)
    saturation_before = forms.IntegerField("SpO2", initial=98)
    heartbite_before = forms.IntegerField("ЧСС", initial=60)
    pulse_before = forms.IntegerField("Пульс", initial=60)
    blood_pressure_systolic_before = forms.IntegerField("Систолическое давление", initial=120)
    blood_pressure_diastolic_before = forms.IntegerField("Диастолическое давление", initial=80)
    normal_blood_pressure_systolic = forms.IntegerField("Систолическое давление", initial=120)
    normal_blood_pressure_diastolic = forms.IntegerField("Диастолическое давление", initial=80)
    blood_glucose_before = forms.FloatField("Сахар крови", initial=4)
    dry_skin = forms.SelectMultiple("Кожные покровы", choices=[("Сухие", "Сухие"), 
                                                               ("Влажные", "Влажные")], 
                                                               initial="Сухие")
    color_skin = forms.SelectMultiple("Цвет", choices=[("Обычной окраски", "Обычные"), 
                                                       ("Бледные", "Бледные"), 
                                                       ("Гиперемированные", "Гиперемированные"), 
                                                       ("Цианоз", "Цианоз")], 
                                                       initial=("Обычные"))
    jaundice = forms.CharField("Желтушность", initial="Нет")
    rash = forms.SelectMultiple("Сыпь", choices=[("Нет", "Нет"), 
                                                 ("Петехиальная", "Петехиальная"), 
                                                 ("Пустулёзная", "Пустулёзная"), 
                                                 ("Везикулярная", "Везикулярная"), 
                                                 ("Узелковая", "Узелковая"), 
                                                 ("Другое", "Другое")], 
                                                 initial=("Нет"))
    throat = forms.SelectMultiple("Зев", choices=[("Спокоен", "Спокоен"), 
                                                  ("Гиперемирован", "Гиперемирован")], 
                                                  initial=("Спокоен"))
    tonsils = forms.CharField("Миндалины", initial="Не увеличинены")
    lymph_nodes = forms.CharField("Лимфоузлы", initial="Не увеличинены")
    swelling = forms.SelectMultiple("Отеки", choices=[("Нет", "Нет"), 
                                                      ("Голени", "Голени"), 
                                                      ("Лицо", "Лицо"), 
                                                      ("Туловище", "Туловище"), 
                                                      ("Руки", "Руки")], 
                                                      initial=("Нет", "Нет"))
    
    #breathing system
    respiratory_type = forms.SelectMultiple("Тип дыхания", choices=[("Везикулярное", "Везикулярное"), 
                                                                    ("Жёсткое", "Жёсткое"), 
                                                                    ("Бронхиальное", "Бронхиальное"), 
                                                                    ("Пуэриальное", "Пуэрильное"), 
                                                                    ("Ослабленное", "Ослабленное"), 
                                                                    ("Отсутствует", "Отсутствует")], 
                                                                    initial=("Везикулярное", "Везикулярное"))
    wheezing = forms.SelectMultiple("Хрипы", choices=[("Нет", "Нет"), 
                                                      ("Влажные", "Влажные"), 
                                                      ("Сухие", "Сухие")], 
                                                      initial=("Нет", "Нет"))
    wheezing_localisation = forms.CharField("Локализация хрипов", initial="Нет хрипов")
    dyspnea = forms.SelectMultiple("Одышка", choices=[("Нет", "Нет"), 
                                                      ("Инспираторная", "Инспираторная"), 
                                                      ("Экспираторная", "Экспираторная"), 
                                                      ("Смешанная", "Смешанная")], 
                                                      initial=("Нет", "Нет"))
    
    #cardiovascular system
    """ heart_sounds = forms.SelectMultiple("Тоны сердца", choices=[("Ритмичные", "Ритмичные"), ("Аритмичные", "Аритмичные")], initial=("Ритмичные", "Ритмичные")) """
    tone_of_heart = forms.SelectMultiple("Тоны сердца", choices=[("Ясные", "Ясные"), 
                                                                 ("Глухие", "Глухие"), 
                                                                 ("Приглушены", "Приглушены"), 
                                                                 ("Отсутствуют", "Отсутствуют")], 
                                                                 initial=("Ясные", "Ясные"))
    murmur = forms.SelectMultiple("Шум", choices=[("Нет", "Нет"), 
                                                  ("Систолический", "Систолический"),
                                                  ("Диастолический", "Диастолический"), 
                                                  ("Трения перикарда", "Трения перикарда"), 
                                                  ("Другое", "Другое")], initial=("Нет", "Нет"))
    rhythmic_tone = forms.SelectMultiple("Ритм тона", choices=[("Ритмичный", "Ритмичный"), 
                                                               ("Аритмичный", "Аритмичный")], 
                                                               initial=("Ритмичный", "Ритмичный"))
    rhythmic_pulse = forms.SelectMultiple("Ритм пульса", choices=[("Ритмичный", "Ритмичный"), 
                                                                  ("Аритмичный", "Аритмичный")], 
                                                                  initial=("Ритмичный", "Ритмичный"))
    characteristic_pulse = forms.SelectMultiple("Пульс", choices=[("Нормальный", "Нормальный"),
                                                                  ("Слабого наполнения", "Слабого наполнения"), 
                                                                  ("Напряжённый", "Напряжённый"), 
                                                                  ("Нитевидный", "Нитевидный"), 
                                                                  ("Отсутствует", "Отсутствует")], 
                                                                  initial=("Нормальный", "Нормальный"))
    heart_rate_deficit = forms.BooleanField("Дефицит пульса", initial=False)
    heart_tone_accent = forms.CharField("Акцент тона", initial=("Нет"))
    
    
    #abdominal
    pain_stomach = forms.SelectMultiple("Живот", choices=[("Безболезненный", "Безболезненный"), 
                                                          ("Болезненный", "Болезненный")], 
                                                          initial=(("Безболезненный", "Безболезненный")))
    characteristic_stomach = forms.SelectMultiple("Живот", choices=[("Мягкий", "Мягкий"), 
                                                                    ("Напряжён", "Напряжён"), 
                                                                    ("Вздут", "Вздут")], 
                                                                    initial=(("Мягкий", "Мягкий")))
    involved_in_the_act_of_breathing = forms.BooleanField(label="Участвует в акте дыхания", initial=True)
    is_shchetkin_blumberg = forms.BooleanField(label="Щёткина-Блюмберга", initial=False)
    is_voskresensky = forms.BooleanField(label="Воскресенского", initial=False)
    is_ortner = forms.BooleanField(label="Ортнера", initial=False)
    is_rovzinga = forms.BooleanField(label="Ровзинга", initial=False)
    is_pasternatsky = forms.BooleanField(label="Пастернацкого", initial=False)
    is_sitkovsky = forms.BooleanField(label="Ситковкого", initial=False)
    is_obraztsova = forms.BooleanField(label="Образцова", initial=False)
    is_murphy = forms.BooleanField(label="Мёрфи", initial=False)
    """ other_perritonial_symptoms = forms.CharField("Другие симптомы", initial=("Нет")) """
    liver = forms.CharField("Печень", initial=("Не увеличена"))
    formed_type_stool = forms.SelectMultiple("Стул", choices=[("Оформлен", "Оформлен"), 
                                                              ("Разжижен", "Разжижен"), 
                                                              ("Жидкий", "Жидкий"), 
                                                              ("Отсутсвует", "Отсутствует")], 
                                                              initial=[("Оформлен", "Оформлен")])
    regular_stool = forms.SelectMultiple("Реглярность", choices=[("Регулярный", "Регулярный"), 
                                                                 ("Нерегулярный", "Нерегулярный"), 
                                                                 ("отсутствует", "Отсутствует")], 
                                                                 initial=("Регулярный", "Регулярный"))
    rate_stool = forms.IntegerField("Частота стула", initial=1)
    
    #nervous system
    behaviour = forms.SelectMultiple("Поведение", choices=[("Спокойное", "Спокойное"), 
                                                           ("Возбуждённое", "Возбуждённое"), 
                                                           ("Агрессивное", "Агрессивное"), 
                                                           ("Депрессивное", "Депрессивное")], 
                                                           initial=[("Спокойное", "Спокойное")])
    none_symptoms = forms.BooleanField(label="Нет менингиальных симптомов:", initial=False)
    nuchal_rigidity = forms.BooleanField(label="Ригидность затылочных мыщц:", initial=False)
    is_kernig_symptom = forms.BooleanField(label="Синдром Кернинга:", initial=False)
    is_brudzinski_symptom = forms.BooleanField(label="Синдром Брудзинского:", initial=False) 
    reaction_to_light = forms.BooleanField("Реакция на свет:", initial="Есть")
    pupils_of_the_eyes = forms.SelectMultiple("Зрачки", choices=[("Нормальные", "Нормальные"), 
                                                                 ("Широкие", "Широкие"), 
                                                                 ("Узкие", "Узкие")], 
                                                                 initial=[("Нормальные", "Нормальные")])
    anisocoria = forms.BooleanField("Анизокория:", initial=False)
    nystagmus = forms.BooleanField("Нистагм:", initial=False)
    focal_signs =  forms.BooleanField("Очаговые симптомы:", initial=True)
    speech = forms.SelectMultiple("Речь", choices=[("Внятная", "Внятная"), 
                                                   ("Афазия", "Афазия"), 
                                                   ("Дизартрия", "Дизартрия")], 
                                                   initial=[("Внятная", "Внятная")])
    paralysis = forms.SelectMultiple("Параличи, парезы", choices=[("Нет", "Нет"), 
                                                                  ("Справа", "Справа"), 
                                                                  ("Слева", "Слева")], 
                                                                  initial=("Нет", "Нет"))
    sensitive = forms.SelectMultiple("Чувствительность", choices=[("Сохранена", "Сохранена"), 
                                                                  ("Отсутствует", "Отсутствует"), 
                                                                  ("Снижена", "Снижена"), 
                                                                  ("Слева", "Слева"), 
                                                                  ("Справа", "Справа")], 
                                                                  initial=("Сохранена", "Сохранена"))
    
    #urogenital system
    painless_urination = forms.SelectMultiple("Мочеимспускание:", choices=[("Безболезненное", "Безболезненное"), 
                                                                           ("Болезненное", "Болезненное")], 
                                                                           initial=("Безболезненное", "Безболезненное"))
    characteristic_urination =  forms.SelectMultiple("Мочеиспускание", choices=[("Свободное", "Свободное"), 
                                                                                ("Затруднено", "Затруднено"), 
                                                                                ("Отсутствует", "Отсутствует")], 
                                                                                initial=("Свободное", "Свободное"))
    kidney_punch = forms.SelectMultiple("Симптом поколачивания", choices=[("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"), 
                                                                          ("Положительный слева", "Положительный слева"), 
                                                                          ("Положительный справа", "Положительный справа"), 
                                                                          ("Положительный с обеих сторон", "Положительный с обеих сторон"), 
                                                                          ("Слабоположительный слева", "Слабоположительный слева"), 
                                                                          ("Слабоположительный справа", "Слабоположительный справа"), 
                                                                          ("Слабоположительный с обеих сторон", "Слабоположительный с обеих сторон")], 
                                                                          initial=("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"))
    characteristic_urine = forms.SelectMultiple("Моча", choices=[("Светло-жёлтая", "Светло-жёлтая"), 
                                                                 ("Мутная", "Мутная"), 
                                                                 ("С включениями", "С включениями"), 
                                                                 ("С осадком", "С осадком")], 
                                                                 initial=("Светло-жёлтая", "Светло-жёлтая"))
    
    #local status
    status_localis = forms.CharField("Локальный статус", widget=forms.Textarea(attr={"class": "form-control", "placeholder" : "Локальный статус..."}))

    #aid
    ecg_before =  forms.CharField("ЭКГ до оказания помощи", widget=forms.Textarea(attr={"class": "form-control", "placeholder" : "ЭКГ до оказания помощи..."}))
    ecg_after =  forms.CharField("ЭКГ после оказания помощи", widget=forms.Textarea(attr={"class": "form-control", "placeholder" : "ЭКГ после оказания помощи..."}))
    aid = forms.CharField("Оказанная помощь", widget=forms.Textarea(attr={"class": "form-control", "placeholder" : "Оказанная помощь..."}))
    temperature_after = forms.FloatField("Температура тела", initial=36.6)
    respiratory_rate_after = forms.IntegerField("ЧДД", initial=0)
    saturation_after = forms.IntegerField("SpO2", initial=0)
    heartbite_after = forms.IntegerField("ЧСС", initial=0)
    pulse_after = forms.IntegerField("Пульс", initial=0)
    blood_pressure_systolic_after = forms.IntegerField("Систолическое давление", initial=120)
    blood_pressure_diastolic_after = forms.IntegerField("Диастолическое давление", initial=80)
    blood_glucose_after = forms.FloatField("Сахар крови", initial=4)
    #diagnosis
    diagnosis = forms.CharField("Диагноз", render_kw={"class": "form-control", "placeholder" : "Диагноз..."})
    