# FROM nginx:stable-alpine

# # Копируем созданную вами ПАПКУ (проверьте имя: build или dist)
# COPY build/ /usr/share/nginx/html/

# # Копируем конфиг (обсудим его ниже)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

# Этап 1: Сборка React-приложения
FROM node:18-alpine AS builder

WORKDIR /frontend

# Копируем package.json и package-lock.json (или yarn.lock)
COPY package*.json ./
# Если используете yarn, добавьте COPY yarn.lock ./

# Устанавливаем зависимости
RUN npm ci --only=production
# Или если нужны devDependencies для сборки: RUN npm ci

# Копируем исходники
COPY . .

# Устанавливаем PUBLIC_URL в корень (или в нужный путь, но без /static/is/)

# Собираем приложение
RUN npm run build

# Этап 2: Сервер Nginx для раздачи статики
FROM nginx:alpine3.18-slim

# Копируем собранные файлы из первого этапа
COPY --from=builder /frontend/build /usr/share/nginx/html

# Копируем конфиг Nginx (если нужен кастомный)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]