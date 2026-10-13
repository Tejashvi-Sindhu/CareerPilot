# AI-Powered Job Intelligence & Career Recommendation System

A final-year AI/ML project built with FastAPI, React, TypeScript, SQLite, scikit-learn, PyMuPDF, and python-docx. It runs locally without a paid API key.

## Features
- Upload PDF/DOCX resumes and extract text.
- Extract skills using an editable skill taxonomy.
- Search saved listings and sync current jobs from Arbeitnow public job-board API.
- Explainable job matching using TF-IDF/cosine similarity and skill coverage.
- Skill-gap analysis and career recommendations.
- Learning roadmap and role/skill-based interview-question generation.
- Optional AI question-answering endpoint through an OpenAI-compatible provider; API keys stay on the backend.
- Dataset-based job-market analytics.
- SQLite persistence for synced and imported jobs; no fabricated jobs are inserted automatically.
- Backend tests and frontend production build scripts.

> Live listings depend on the external source being reachable and may expire or change. Always verify the original listing before applying. Match scores are compatibility estimates, not hiring probabilities. Results depend on extracted text and the configured skill taxonomy.

## Requirements
- Python 3.11 or 3.12 recommended
- Node.js 20 LTS or later
- VS Code

No GPU, Docker, or local LLM is required. Live listings need internet access. The general-purpose AI question-answering feature requires a provider API key; ordinary resume matching, job analytics, and practice-question generation work without it.

## Windows PowerShell setup

Open the `ai-job-intelligence` folder in VS Code. Open **two terminal windows**.

### 1. Backend (Terminal 1)
```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
# Optional: edit backend/.env and set OPENAI_API_KEY, OPENAI_MODEL, and OPENAI_BASE_URL for general AI Q&A.
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
If `py -3.11` is unavailable, use `py -3` if it points to Python 3.11+.

Backend docs: http://127.0.0.1:8000/docs  
Health check: http://127.0.0.1:8000/health

### 2. Frontend (Terminal 2)
From the project root:
```powershell
cd frontend
npm.cmd install
Copy-Item .env.example .env
npm.cmd run dev
```
Open the local URL printed by Vite (normally http://localhost:5173).

If PowerShell blocks `npm`, use `npm.cmd` as shown; do not weaken system-wide execution policy.

## Run tests
Backend (from `backend`):
```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
Frontend (from `frontend`):
```powershell
npm.cmd run build
```

## Load current job listings
The database starts empty. Open **Explore Jobs** and click **Refresh live listings**. The backend requests current listings from Arbeitnow's public job-board API and stores their title, company, location, description, detected skills, source attribution, and original URL in SQLite. Internet access is required. If the source is down or blocks the request, the app reports an error rather than inventing listings. This source may not cover every country or role, and listings should be verified on their original pages.

To import your own data instead, call `POST /jobs/import-csv` with multipart form field `file`. Expected columns include `title`, `company`, `description`, and optional `location`, `experience_level`, `employment_type`, `skills` (comma-separated), `source`, `source_url`. Use the Swagger UI at `/docs`.

## API endpoints
- `GET /health`
- `GET /jobs`
- `GET /jobs/{job_id}`
- `POST /jobs/sync/live` (fetch current Arbeitnow listings)
- `POST /jobs/import-csv`
- `POST /resume/analyze` (multipart `file`)
- `POST /match` (JSON: `resume_text`, optional `job_ids`)
- `POST /career/recommend`
- `POST /roadmap`
- `POST /interview/questions`
- `GET /analytics/market`
- `GET /skills/taxonomy`

## Privacy and limitations
- Uploaded resume files are processed in memory and are not saved as files by this app.
- Resume text is not persisted by the backend.
- This is a student project intended for local use; it is not a production multi-user service.
- Scanned PDFs need OCR, which is not included. The API returns a useful error if no text is extractable.
- Job listings are retrieved from a third-party source; availability, location coverage, and freshness depend on that source. Skill extraction is taxonomy-based and may miss synonyms. Validate recommendations yourself.
- For real deployment, add authentication, rate limiting, stronger privacy controls, monitoring, and a properly licensed up-to-date job source.

## GitHub
Before publishing, inspect `.env` and ensure no secrets or private resumes are committed. `.gitignore` excludes virtual environments, local databases, node modules, build outputs, and environment files.


## AI question-answering setup (optional)

The Interview Prep page includes a question search box. To answer arbitrary questions using a language model, configure an OpenAI-compatible API in `backend/.env`:

```env
OPENAI_API_KEY=your_private_api_key
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

Keep the key only in `backend/.env`; never commit it or place it in `frontend/.env`. API usage may incur charges. Restart FastAPI after changing `.env`. Without a key, the endpoint returns a setup message rather than pretending to answer. AI responses can be wrong, so verify important claims.

## Real data behavior

The app no longer ships with fabricated sample job listings. The job database starts empty until you refresh the live connector or import a CSV. Startup removes legacy rows marked `Clearly labeled demo dataset` from older local databases. Analytics reflect the jobs currently stored locally, not the entire labor market.


### Troubleshooting: AI assistant configuration

The backend loads `backend/.env` using a path relative to the backend source, so it works even when Uvicorn is started from a different working directory. After editing `backend/.env`, restart the backend. Keep `OPENAI_API_KEY` private and never commit `.env`. A valid key, available model, and API account billing may be required.

### Job search behavior

Explore Jobs searches loaded listings by individual query terms across title, company, description, and listed skills. It cannot return jobs that have not been loaded; use **Refresh live listings** first.
