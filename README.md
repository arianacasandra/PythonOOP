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
├── requirements.txt     # Dependențe Python
└── README.md            # Documentația curentă
```

## Instalare și configurare

1. Clonează acest repository:
   ```bash
   git clone <url-repo>
   cd <project-root>
   ```
2. Creează și activează un mediu virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
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

- **Exponențiere** (2 la puterea 5):

  ```bash
  curl -X POST http://localhost:8000/pow \
       -H "Content-Type: application/json" \
       -d '{"x":2,"y":5}'
  ```

- **Fibonacci** (al 10‑lea element):

  ```bash
  curl -X POST http://localhost:8000/fibonacci \
       -H "Content-Type: application/json" \
       -d '{"n":10}'
  ```

- **Factorial** (5!):

  ```bash
  curl -X POST http://localhost:8000/factorial \
       -H "Content-Type: application/json" \
       -d '{"n":5}'
  ```

## Persistență

Toate cererile sunt salvate în baza de date SQLite `app/operations.db`, în tabela `operations` cu următoarele coloane:

- `id` (INTEGER, PK)
- `op_type` (TEXT)
- `params` (TEXT)
- `result` (TEXT)
- `timestamp` (TEXT, ISO 8601 UTC)

## Extensibilitate și bune practici

- Codul este organizat pe layere: **models**, **calculator**, **db**, **api**.
- Se poate adăuga rapid un nou endpoint în `api.py` și în `calculator.py`.
- Pentru medii de producție, se recomandă:
  - Containerizare Docker
  - Monitorizare cu Prometheus/Grafana
  - Caching cu Redis
  - Autentificare JWT

---

Proiect realizat de un student al AI Academy @ Endava, ca exercițiu de aplicație a conceptelor de microservicii și API design.

