
# MathOps Service

Acesta este un microserviciu, având ca scop expunerea unui API REST pentru operații matematice fundamentale și persistarea cererilor într-o bază de date SQLite.

## Caracteristici principale

- **Operații suportate**:
  - Exponențiere (`/pow`)
  - Numărul n‑lea din seria Fibonacci (`/fibonacci`)
  - Factorialul unui număr (`/factorial`)
- **Persistență**: toate cererile și rezultatele sunt salvate în `app/operations.db`
- **Framework**: FastAPI (Python)
- **Bază de date**: SQLite (fișier local)
- **Mod de lucru**: dezvoltare locală, cu reîncărcare automată a codului (`--reload`)

## Structura proiectului

```
<project-root>/
├── app/
│   ├── api.py           # Definirea API-ului și a endpoint-urilor
│   ├── calculator.py    # Logica de calcul pentru pow, fib, factorial
│   ├── db.py            # Funcții pentru inițializarea și interacțiunea cu SQLite
│   ├── models.py        # Scheme Pydantic pentru validarea cererilor și răspunsurilor
│   └── operations.db    # Baza SQLite cu tabela "operations"
├── cli.py               # Interfață CLI pentru apeluri locale
├── requirements.txt     # Dependențe Python
├── Dockerfile           # Fișier pentru containerizarea cu Docker
└── README.md            # Documentația curentă
```

## Instalare și configurare (fără Docker)

1. Clonează acest repository:
   ```bash
   git clone <url-repo>
   cd <project-root>
   ```

2. Creează și activează un mediu virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scriptsctivate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. Instalează dependențele:
   ```bash
   pip install -r requirements.txt
   ```

## Rulare locală

Pentru a porni serverul FastAPI cu reîncărcare automată:

```bash
python -m uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
```

După pornire, vei găsi documentația Swagger la:

```
http://localhost:8000/docs
```

## Exemple de cereri

### `pow` (2 la puterea 5)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/pow" `
    -Method Post `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{ "x": 2, "y": 5 }'
```

### `fibonacci` (al 10-lea număr)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/fibonacci" `
    -Method Post `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{ "n": 10 }'
```

### `factorial` (5!)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/factorial" `
    -Method Post `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{ "n": 5 }'
```

## Persistență

Toate cererile sunt salvate în baza de date SQLite `app/operations.db`, în tabela `operations`, cu coloanele:

- `id` (INTEGER, PK)
- `op_type` (TEXT)
- `params` (TEXT)
- `result` (TEXT)
- `timestamp` (TEXT, ISO 8601 UTC)

## Extensibilitate și bune practici

- Codul este organizat pe layere: **models**, **calculator**, **db**, **api**.
- Se poate adăuga rapid un nou endpoint în `api.py` și `calculator.py`.
- Pentru medii de producție, se recomandă:
  -  Logging structurat (implementat)
  -  Caching local (implementat)
  -  Containerizare Docker
  -  Monitorizare cu Prometheus/Grafana
  -  Autentificare JWT
  -  Integrare cu Kafka, RabbitMQ

---

## Rulare în Docker

Această aplicație poate fi rulată complet izolat, containerizat, folosind Docker.

###  Build imaginea Docker

```bash
docker build -t mathops-app .
```

###  Rulează containerul

```bash
docker run -p 8000:8000 mathops-app
```

Accesează interfața Swagger:
```
http://localhost:8000/docs
```

###  Test rapid (PowerShell)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/pow" `
    -Method Post `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{ "x": 2, "y": 5 }'
```

Dacă folosești Git Bash sau WSL:

```bash
curl -X POST http://localhost:8000/pow -H "Content-Type: application/json" -d "{"x":2,"y":5}"
```

---

## Funcționalități opționale implementate

Pe lângă cerințele de bază, proiectul include mai multe îmbunătățiri care îl aduc mai aproape de un microserviciu real, production-ready:

###  Caching (`@lru_cache`)
Funcția `fibonacci(n)` este optimizată cu `functools.lru_cache(maxsize=128)`, pentru a evita recalcularea acelorași valori. Acest mecanism de caching îmbunătățește semnificativ performanța în cazul apelurilor frecvente sau valorilor mari.

###  Logging structurat
Aplicația folosește modulul `logging` din Python pentru a loga toate cererile API într-un format standardizat, care include timestamp, nivel și detalii despre operație:

```
2025-08-08 13:12:44,123 [INFO] FIBONACCI called with n=10 -> result=55
```

Logurile pot fi extinse către fișiere, aplicații externe sau soluții precum ELK stack, Prometheus etc.

###  Containerizare (Docker)
Proiectul poate fi rulat într-un container Docker, fiind pregătit pentru deploy în orice mediu (local, cloud, Rancher, Kubernetes).

###  Interfață CLI
Aplicația oferă și un script CLI (`cli.py`) construit cu `click`, care permite rularea locală rapidă a operațiilor matematice fără apel direct la API.

---

## Funcționalități avansate (recomandate, dar neimplementate)

-  Autentificare JWT
-  Monitorizare Prometheus + Grafana
-  Mesagerie (Kafka, RabbitMQ)
-  Deploy cloud/serverless (GCP, AWS, Azure)
-  Testare automată (`pytest`, `httpx`)

---

## Autori
Olaru Ariana Casandra si Bogodae Stefan George
