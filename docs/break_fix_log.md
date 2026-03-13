Scenario A — Semantic index mismatch

Break:
Changed embedding model from all-MiniLM-L6-v2 to all-MiniLM-L12-v2.

Result:
Vector embeddings dimension mismatch occurred.

Fix:
Rebuilt the vector index using the new embedding model.

Scenario B — Database schema migration

Break:
Added new column query_length to database schema.

Result:
API failed when inserting logs.

Fix:
Updated schema and insertion logic.

Scenario C — Hybrid scoring bug

Break:
Removed epsilon from normalization formula.

Result:
Divide-by-zero error occurred when all scores were equal.

Fix:
Added epsilon (1e-9) to denominator.