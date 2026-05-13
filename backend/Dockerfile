FROM python:3.12-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /backend

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


COPY pyproject.toml uv.lock* ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# RUN python manage.py collectstatic --noinput



FROM python:3.12-slim AS final

RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/list/*
    
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/backend/.venv/bin:$PATH"

WORKDIR /backend

RUN useradd -m appuser

COPY --from=builder --chown=appuser:appuser /backend /backend/


USER root
RUN chmod +x /backend/entrypoint.sh
RUN mkdir -p /backend/db_data && chown -R appuser:appuser /backend/db_data
RUN mkdir -p /backend/staticfiles && chown -R appuser:appuser /backend/staticfiles
RUN chmod -R 755 /backend/staticfiles
USER appuser

EXPOSE 8000

ENTRYPOINT [ "/backend/entrypoint.sh" ]

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "project.asgi:application"]


