# Model evaluation plan

## Implemented baseline
The default matcher computes TF-IDF cosine similarity between resume text and job title/description/skills, plus normalized skill coverage. The final compatibility score is `100 * (0.55 * skill_coverage + 0.45 * text_similarity)`. This is a ranking heuristic, not a hiring probability.

## Optional semantic approach
Install `requirements-optional.txt` and set `ENABLE_SEMANTIC_MODEL=true` to use the configured Sentence Transformers model. The service falls back to TF-IDF if the optional package or model is unavailable. The first model load may require internet access.

## Evaluation protocol
Create a manually reviewed set of resume/job pairs and label each pair with a relevance grade (for example, 0 = irrelevant, 1 = partially relevant, 2 = relevant). Keep the same examples for both approaches. Measure Precision@K and Recall@K for binary relevance, and NDCG@K for graded relevance. Record the dataset source, labeling instructions, disagreements, model version, and run date.

Do not report performance metrics until this evaluation is performed. The bundled demo data is too small and synthetic to support market-wide claims.
