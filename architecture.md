# Architecture

- React + TypeScript + Vite provides the browser UI.
- FastAPI exposes JSON and multipart endpoints.
- SQLAlchemy stores the job dataset in SQLite by default.
- PyMuPDF and python-docx extract text from supported resume formats in memory.
- The matching service combines explicit skill coverage with TF-IDF similarity. Optional Sentence Transformers embeddings can replace TF-IDF similarity when enabled.
- Career suggestions and roadmap generation use transparent rule-based heuristics; they are not trained hiring or aptitude predictors.
- Market analytics summarize only the currently loaded records.

The default configuration is local-first and does not require external APIs.
