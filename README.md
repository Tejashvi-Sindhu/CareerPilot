# CareerPilot
### AI-Powered Job Intelligence & Career Recommendation Platform

CareerPilot is a full-stack career-support application designed to help job seekers explore opportunities, understand resume-to-role alignment, and prepare for the next step in their careers.

## Features

- **Resume analysis** — upload a PDF or DOCX resume for text extraction and analysis.
- **Job matching** — TF-IDF-based text matching and skill-coverage signals to rank relevant listings.
- **Career guidance** — recommendations and learning-roadmap support based on a candidate's profile.
- **Interview preparation** — practice questions and AI-assisted guidance where provider access is configured.
- **Job-market analytics** — explore job titles, skill frequencies, and locations in the currently loaded dataset.
- **Live listing source support** — job data can be sourced from external listings; analytics describe the loaded dataset, not the entire job market.

## Tech stack

- **Frontend:** React, TypeScript, Vite
- **Backend:** Python, FastAPI, Uvicorn
- **Machine learning:** scikit-learn, TF-IDF
- **Data and documents:** SQLite, PDF/DOCX text extraction
- **Optional AI provider:** OpenAI-compatible API configuration

## Repository structure

```text
CareerPilot/
├── backend/       # FastAPI API, matching and document processing
├── frontend/      # React + TypeScript user interface
├── docs/          # Architecture, data sources and evaluation notes
├── scripts/       # Project verification utilities
├── README.md
└── .gitignore
```

## Run locally

Use Python and Node.js versions compatible with the dependency files.

### 1. Backend

Open a terminal in the repository root:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

API health endpoint (when running): http://127.0.0.1:8000/health

### 2. Frontend

Open a second terminal in the repository root:

```powershell
cd frontend
npm install
npm run build
npm run dev
```

Open the local URL printed by Vite (typically http://localhost:5173).

## Optional AI configuration

Create `backend/.env` from the provided example file if present, and configure your own API credentials:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

Never commit `.env`, API keys, personal resumes, or other private information. An API key requires separate provider access and available quota. Local fallback guidance does not restore provider quota.

## Analytics and model limitations

- Resume-specific metrics should be interpreted only after a resume has been analyzed.
- Job-market charts summarize the records currently loaded by the app. They are not representative of the entire market unless the dataset and sampling method support that conclusion.
- TF-IDF is a lexical similarity baseline, not a guarantee of job suitability or hiring outcomes.
- AI-generated answers and recommendations may be incomplete and should be reviewed.

## Development status

This is an educational portfolio project. Validate dependency installation, backend startup, frontend production build, and key user flows in your own environment before relying on it or deploying it publicly.

## License

Add or retain a license file that matches how you intend others to use this project. Unless a license is included, normal copyright restrictions apply.
