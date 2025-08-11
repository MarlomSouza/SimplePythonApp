# SimplePythonApp

Aplicação Python simples usando FastAPI.

## Endpoints

- GET / -> { "status": "ok" }
- GET /env -> Dicionário com variáveis de ambiente.
- GET /time -> Hora atual em UTC em ISO 8601.

## Executar localmente

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Acessar: http://127.0.0.1:8000

Documentação automática (Swagger UI): http://127.0.0.1:8000/docs

## Docker

Build manual:
```bash
docker build -t simplepythonapp .
docker run --rm -p 8000:8000 --env APP_MESSAGE=Hello simplepythonapp
```

## Docker Compose

Copiar .env.example para .env (opcional):
```bash
cp .env.example .env
```

Subir stack:
```bash
docker compose up --build
```

Acessar: http://localhost:8000

Parar:
```bash
docker compose down
```

## Testes

```bash
pytest -q
```

## Observações

O endpoint `/env` retorna todas as variáveis disponíveis no processo. Evite expor esse endpoint em produção sem filtragem/autenticação.