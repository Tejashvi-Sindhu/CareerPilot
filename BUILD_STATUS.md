# Build and verification status

- Backend Python syntax check: passed.
- Backend automated tests: 11 passed in the available environment.
- Resume analysis returns the full extracted text for matching and interview generation, while retaining a short preview field.
- Selecting a new resume clears previous resume-dependent results before processing the new file.
- Interview practice provides sample-answer guidance and varies the local fallback set; a configured AI provider can generate resume-aware questions.
- Market analytics explicitly states that loaded-record counts are not representative of the entire job market.
- ZIP archive integrity: verify after packaging.
- Frontend production build: not verified in this environment because npm registry installation timed out. Verify locally with `cd frontend`, `npm.cmd install`, then `npm.cmd run build`.
- Live job connector: requires internet access and the external Arbeitnow API to be reachable.
- General question-answering and AI-generated interview sets require an OpenAI-compatible API key in `backend/.env`. Do not commit the key or put it in the frontend environment. API billing/access is separate from a ChatGPT subscription.

A successful backend test run does not prove the external job source or third-party AI provider will always be available.
