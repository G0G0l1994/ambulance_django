from django import forms


class CardForms(forms.Form):
    last_name = forms.CharField(label='Фамилий', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Отчество', max_length=100)
    date_of_birth = forms.DateField(label='Дата рождения', input_formats='DD.MM.YYYY')
    address = forms.CharField(label='Адрес', widget=forms.Textarea, max_length=200)
    cause = forms.CharField(label='Повод к вызову', widget=forms.Textarea, max_length=200)
    status = forms.ChoiceField(label="Статус вызова", choices=[("Принят","Принят"),
                                                            ("Назначен бригаде","Назначен бригаде"), 
                                                            ("Завершен","Завершен"),
                                                            ("Отменён","Отменён")], 
                                                            )
    crew = forms.ChoiceField(label='Бригада', choices=[('crew1','crew1'),('crew2','crew2')])
    # times
    time_of_receipt = forms.DateTimeField(label='Время приема', input_formats='%H:%M')
    transmission_time = forms.DateTimeField(label='Время передачи', input_formats='%H:%M')
    departure_time = forms.DateTimeField(label='Время принятия вызова', input_formats='%H:%M')
    arrival_time = forms.DateTimeField(label='Время прибытия', input_formats='%H:%M')
    start_time_of_hospitalization = forms.DateTimeField(label='Время начала госпитализации', input_formats='%H:%M')
    time_of_arrival_at_hospital = forms.DateTimeField(label='Время прибытия в стационар', input_formats='%H:%M')
    call_end_time = forms.DateTimeField(label='Окончание вызова', input_formats='%H:%M')
    complaints = forms.CharField(label='Жалобы', widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Жалобы пациента..."}))
    anamnesis = forms.CharField(label='Анамнез',widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Анамнез"}))
    general_assessment = forms.ChoiceField(label='Общее состояние', choices=[("Удовлетворительное", "Удовлетворительное"), 
                                                                          ("Средней степени тяжести", "Средней степени тяжести"), 
                                                                          ("Тяжелое", "Тяжелое"), 
                                                                          ("Терминальное", "Терминальное")], 
                                                                    )
    сonsciousness = forms.ChoiceField(label='Сознание', choices=[("Ясное", "Ясное"), 
                                                              ("Оглушение", "Оглушение"), 
                                                              ("Сопор", "Сопор"), 
                                                              ("Кома", "Кома")], 
                                                              )
    glasgow_scale = forms.IntegerField(label='Шкала Глазго',)


    body_position = forms.ChoiceField(label="Положение тела", choices=[("Активное", "Активное"), 
                                                                    ("Пассивное", "Пассивное"), 
                                                                    ("Вынужденное", "Вынужденное")], 
                                                                    )
    temperature_before = forms.FloatField(label="Температура тела",)
    respiratory_rate_before = forms.IntegerField(label="ЧДД",) 
    saturation_before = forms.IntegerField(label="SpO2",)
    heartbite_before = forms.IntegerField(label="ЧСС",)
    pulse_before = forms.IntegerField(label="Пульс",) 
    blood_pressure_systolic_before = forms.IntegerField(label="Систолическое давление", )
    blood_pressure_diastolic_before = forms.IntegerField(label="Диастолическое давление",) 
    normal_blood_pressure_systolic = forms.IntegerField(label="Систолическое давление", )
    normal_blood_pressure_diastolic = forms.IntegerField(label="Диастолическое давление", )
    blood_glucose_before = forms.FloatField(label="Сахар крови")    
    dry_skin = forms.ChoiceField(label="Кожные покровы", choices=[("Сухие", "Сухие"), 
                                                               ("Влажные", "Влажные")], 
                                                               )
    color_skin = forms.ChoiceField(label="Цвет", choices=[("Обычной окраски", "Обычные"), 
                                                       ("Бледные", "Бледные"), 
                                                       ("Гиперемированные", "Гиперемированные"), 
                                                       ("Цианоз", "Цианоз")], 
                                                       )
    jaundice = forms.CharField(label="Желтушность",)
    rash = forms.ChoiceField(label="Сыпь", choices=[("Нет", "Нет"), 
                                                 ("Петехиальная", "Петехиальная"), 
                                                 ("Пустулёзная", "Пустулёзная"), 
                                                 ("Везикулярная", "Везикулярная"), 
                                                 ("Узелковая", "Узелковая"), 
                                                 ("Другое", "Другое")], 
                                                 )
    throat = forms.ChoiceField(label="Зев", choices=[("Спокоен", "Спокоен"), 
                                                  ("Гиперемирован", "Гиперемирован")], 
                                                  )
    tonsils = forms.CharField(label="Миндалины")
    lymph_nodes = forms.CharField(label="Лимфоузлы",)
    swelling = forms.ChoiceField(label="Отеки", choices=[("Нет", "Нет"), 
                                                      ("Голени", "Голени"), 
                                                      ("Лицо", "Лицо"), 
                                                      ("Туловище", "Туловище"), 
                                                      ("Руки", "Руки")], 
                                                      )
    
    #breathing system
    respiratory_type = forms.ChoiceField(label="Тип дыхания", choices=[("Везикулярное", "Везикулярное"), 
                                                                    ("Жёсткое", "Жёсткое"), 
                                                                    ("Бронхиальное", "Бронхиальное"), 
                                                                    ("Пуэриальное", "Пуэрильное"), 
                                                                    ("Ослабленное", "Ослабленное"), 
                                                                    ("Отсутствует", "Отсутствует")], 
                                                                    )
    wheezing = forms.ChoiceField(label="Хрипы", choices=[("Нет", "Нет"), 
                                                      ("Влажные", "Влажные"), 
                                                      ("Сухие", "Сухие")], 
                                                      )
    wheezing_localisation = forms.CharField(label="Локализация хрипов")
    dyspnea = forms.ChoiceField(label="Одышка", choices=[("Нет", "Нет"), 
                                                      ("Инспираторная", "Инспираторная"), 
                                                      ("Экспираторная", "Экспираторная"), 
                                                      ("Смешанная", "Смешанная")], 
                                                      )
    
    #cardiovascular system
    """ heart_sounds = forms.ChoiceField("Тоны сердца", choices=[("Ритмичные", "Ритмичные"), ("Аритмичные", "Аритмичные")], итмичные", "Ритмичные")) """
    tone_of_heart = forms.ChoiceField(label="Тоны сердца", choices=[("Ясные", "Ясные"), 
                                                                 ("Глухие", "Глухие"), 
                                                                 ("Приглушены", "Приглушены"), 
                                                                 ("Отсутствуют", "Отсутствуют")], 
                                                                 )
    murmur = forms.ChoiceField(label="Шум", choices=[("Нет", "Нет"), 
                                                  ("Систолический", "Систолический"),
                                                  ("Диастолический", "Диастолический"), 
                                                  ("Трения перикарда", "Трения перикарда"), 
                                                  ("Другое", "Другое")])
    rhythmic_tone = forms.ChoiceField(label="Ритм тона", choices=[("Ритмичный", "Ритмичный"), 
                                                               ("Аритмичный", "Аритмичный")], 
                                                               )
    rhythmic_pulse = forms.ChoiceField(label="Ритм пульса", choices=[("Ритмичный", "Ритмичный"), 
                                                                  ("Аритмичный", "Аритмичный")], 
                                                                  )
    characteristic_pulse = forms.ChoiceField(label="Пульс", choices=[("Нормальный", "Нормальный"),
                                                                  ("Слабого наполнения", "Слабого наполнения"), 
                                                                  ("Напряжённый", "Напряжённый"), 
                                                                  ("Нитевидный", "Нитевидный"), 
                                                                  ("Отсутствует", "Отсутствует")], 
                                                                  )
    heart_rate_deficit = forms.BooleanField(label="Дефицит пульса",)
    heart_tone_accent = forms.CharField(label="Акцент тона",)
    
    
    #abdominal
    pain_stomach = forms.ChoiceField(label="Живот", choices=[("Безболезненный", "Безболезненный"), 
                                                          ("Болезненный", "Болезненный")], 
                                                          )
    characteristic_stomach = forms.ChoiceField(label="Живот", choices=[("Мягкий", "Мягкий"), 
                                                                    ("Напряжён", "Напряжён"), 
                                                                    ("Вздут", "Вздут")], 
                                                                    )
    involved_in_the_act_of_breathing = forms.BooleanField(label="Участвует в акте дыхания")
    is_shchetkin_blumberg = forms.BooleanField(label="Щёткина-Блюмберга")
    is_voskresensky = forms.BooleanField(label="Воскресенского")
    is_ortner = forms.BooleanField(label="Ортнера")
    is_rovzinga = forms.BooleanField(label="Ровзинга")
    is_pasternatsky = forms.BooleanField(label="Пастернацкого")
    is_sitkovsky = forms.BooleanField(label="Ситковкого")
    is_obraztsova = forms.BooleanField(label="Образцова")
    is_murphy = forms.BooleanField(label="Мёрфи")
    """ other_perritonial_symptoms = forms.CharField(label="Другие симптомы", ет")) """
    liver = forms.CharField(label="Печень")
    formed_type_stool = forms.ChoiceField(label="Стул", choices=[("Оформлен", "Оформлен"), 
                                                              ("Разжижен", "Разжижен"), 
                                                              ("Жидкий", "Жидкий"), 
                                                              ("Отсутсвует", "Отсутствует")], 
                                                              )
    regular_stool = forms.ChoiceField(label="Реглярность", choices=[("Регулярный", "Регулярный"), 
                                                                 ("Нерегулярный", "Нерегулярный"), 
                                                                 ("отсутствует", "Отсутствует")], 
                                                                 )
    rate_stool = forms.IntegerField(label="Частота стула",)    
    #nervous system
    behaviour = forms.ChoiceField(label="Поведение", choices=[("Спокойное", "Спокойное"), 
                                                           ("Возбуждённое", "Возбуждённое"), 
                                                           ("Агрессивное", "Агрессивное"), 
                                                           ("Депрессивное", "Депрессивное")], 
                                                           )
    none_symptoms = forms.BooleanField(label="Нет менингиальных симптомов:")
    nuchal_rigidity = forms.BooleanField(label="Ригидность затылочных мыщц:",)
    is_kernig_symptom = forms.BooleanField(label="Синдром Кернинга:", )
    is_brudzinski_symptom = forms.BooleanField(label="Синдром Брудзинского:",) 
    reaction_to_light = forms.BooleanField(label="Реакция на свет:",)
    pupils_of_the_eyes = forms.ChoiceField(label="Зрачки", choices=[("Нормальные", "Нормальные"), 
                                                                 ("Широкие", "Широкие"), 
                                                                 ("Узкие", "Узкие")], 
                                                                 )
    anisocoria = forms.BooleanField(label="Анизокория:", )
    nystagmus = forms.BooleanField(label="Нистагм:", )
    focal_signs =  forms.BooleanField(label="Очаговые симптомы:", )
    speech = forms.ChoiceField(label="Речь", choices=[("Внятная", "Внятная"), 
                                                   ("Афазия", "Афазия"), 
                                                   ("Дизартрия", "Дизартрия")], 
                                                   )
    paralysis = forms.ChoiceField(label="Параличи, парезы", choices=[("Нет", "Нет"), 
                                                                  ("Справа", "Справа"), 
                                                                  ("Слева", "Слева")], 
                                                                  )
    sensitive = forms.ChoiceField(label="Чувствительность", choices=[("Сохранена", "Сохранена"), 
                                                                  ("Отсутствует", "Отсутствует"), 
                                                                  ("Снижена", "Снижена"), 
                                                                  ("Слева", "Слева"), 
                                                                  ("Справа", "Справа")], 
                                                                  )
    
    #urogenital system
    painless_urination = forms.ChoiceField(label="Мочеимспускание:", choices=[("Безболезненное", "Безболезненное"), 
                                                                           ("Болезненное", "Болезненное")], 
                                                                           )
    characteristic_urination =  forms.ChoiceField(label="Мочеиспускание", choices=[("Свободное", "Свободное"), 
                                                                                ("Затруднено", "Затруднено"), 
                                                                                ("Отсутствует", "Отсутствует")], 
                                                                                )
    kidney_punch = forms.ChoiceField(label="Симптом поколачивания", choices=[("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"), 
                                                                          ("Положительный слева", "Положительный слева"), 
                                                                          ("Положительный справа", "Положительный справа"), 
                                                                          ("Положительный с обеих сторон", "Положительный с обеих сторон"), 
                                                                          ("Слабоположительный слева", "Слабоположительный слева"), 
                                                                          ("Слабоположительный справа", "Слабоположительный справа"), 
                                                                          ("Слабоположительный с обеих сторон", "Слабоположительный с обеих сторон")], 
                                                                          )
    characteristic_urine = forms.ChoiceField(label="Моча", choices=[("Светло-жёлтая", "Светло-жёлтая"), 
                                                                 ("Мутная", "Мутная"), 
                                                                 ("С включениями", "С включениями"), 
                                                                 ("С осадком", "С осадком")], 
                                                                 )
    
    #local status
    status_localis = forms.CharField(label="Локальный статус", widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Локальный статус..."}))

    #aid
    ecg_before =  forms.CharField(label="ЭКГ до оказания помощи", widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "ЭКГ до оказания помощи..."}))
    ecg_after =  forms.CharField(label="ЭКГ после оказания помощи", widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "ЭКГ после оказания помощи..."}))
    aid = forms.CharField(label="Оказанная помощь", widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Оказанная помощь..."}))
    temperature_after = forms.FloatField(label="Температура тела",)
    respiratory_rate_after = forms.IntegerField(label="ЧДД",)    
    saturation_after = forms.IntegerField(label="SpO2",)    
    heartbite_after = forms.IntegerField(label="ЧСС", )    
    pulse_after = forms.IntegerField(label="Пульс",)     
    blood_pressure_systolic_after = forms.IntegerField(label="Систолическое давление", )
    blood_pressure_diastolic_after = forms.IntegerField(label="Диастолическое давление",) 
    blood_glucose_after = forms.FloatField(label="Сахар крови",)
    #diagnosis
    diagnosis = forms.CharField(label="Диагноз", widget=forms.Textarea(attrs={"class": "form-control", "placeholder" : "Диагноз..."}))
    