# Data dictionary

## 2-data/derived/file_index.csv
- `anon_id`: anonymized identifier for a PDF file (e.g., AI01, CH001)
- `filename`: PDF filename within the package
- `source`: `raw_ai_log` (retained GenAI transcripts) or `student_change_log` (individual change reports)

## 2-data/derived/ratings_tidy_template.csv
Template for rubric ratings or coded items.
- `unit_id`: unique identifier of the rated/coded unit (you define the convention)
- `source_id`: link to `anon_id` (e.g., AI01) or other source key
- `rater`: rater ID (e.g., instructor, TA1, TA2)
- `dimension`: rating/coding dimension (e.g., clarity/completeness/correctness, actionability, recipience-function)
- `score`: numeric or categorical value
- `notes`: optional free-text justification

## Raw PDFs
- `2-data/raw/ai-logs/AI##.pdf`: retained GenAI interaction logs (may include follow-up turns).
- `2-data/raw/student-change-logs/CH###.pdf`: individual student change reports describing modifications made after GenAI feedback.
