# GenAI-Powered Resource Management Co-pilot (FastAPI)

Quickstart:

1. Create a virtualenv: `python -m venv .venv && source .venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Export env vars (example):
   - `export DATABASE_URL=postgresql+asyncpg://postgres:pass@localhost:5432/genai`
   - `export SECRET_KEY=somesecret`
4. Run: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

API docs: http://localhost:8000/docs
