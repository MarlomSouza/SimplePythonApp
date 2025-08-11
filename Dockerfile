# Build image para SimplePythonApp
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_HOME=/app

WORKDIR $APP_HOME

# Dependências do sistema (opcional mínimo)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro para leverage de cache
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar código
COPY app ./app

# Expor porta
EXPOSE 8000

# Usuário não root (opcional)
RUN useradd -m appuser && chown -R appuser:appuser $APP_HOME
USER appuser

# Comando de execução
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
