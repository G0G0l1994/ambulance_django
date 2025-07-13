#!/usr/bin/env python
"""
Простой скрипт для запуска создания тестовых карт
"""

import os
import sys

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем и запускаем основной скрипт
from create_test_cards import create_test_cards

if __name__ == "__main__":
    print("🚑 Запуск создания тестовых карт...")
    create_test_cards()
    print("✅ Тестовые карты созданы успешно!") 