# Criteria 4 and 5 — before

`run_eval.py` measures criteria 1, 2 and 3. Criteria 4 and 5 are mine, and it
doesn't know about them, so they get measured here.

- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Chunks from `chunker.py::split_documents`
- When: 2026-09-27

---

## Criterion 5 — answer in under 8 seconds

Produced by `measure_timing.py`. Three runs, caching off, timing the whole
path: `store.py::search` → `gate.py::check` → `generate.py::answer_from_chunks`.

```
=== Timing Run 1 ===
2.607 seconds | Do financial aid packages for study abroad generally cover a student's trip?
1.058 seconds | What do students say about the time it takes to get around campus?
0.722 seconds | What is the cost of the cheapest on-campus housing?
0.818 seconds | How late is the library open during the spring term?
0.876 seconds | Which course is known for having a heavy workload?

=== Timing Run 2 ===
0.984 seconds | Do financial aid packages for study abroad generally cover a student's trip?
1.074 seconds | What do students say about the time it takes to get around campus?
0.796 seconds | What is the cost of the cheapest on-campus housing?
1.012 seconds | How late is the library open during the spring term?
1.087 seconds | Which course is known for having a heavy workload?

=== Timing Run 3 ===
1.085 seconds | Do financial aid packages for study abroad generally cover a student's trip?
1.132 seconds | What do students say about the time it takes to get around campus?
0.915 seconds | What is the cost of the cheapest on-campus housing?
0.818 seconds | How late is the library open during the spring term?
1.360 seconds | Which course is known for having a heavy workload?
```

Under 8 seconds: 5 of 5, 5 of 5, 5 of 5. Slowest single answer 2.607s, on the
first question of the first run — that one includes loading the embedding model.
Every answer after it came back in about a second.

---

## Criterion 4 — retrieved chunk between 50 and 400 characters

Produced by `measure_chunks.py`, retrieval by `store.py::search`. One pass, not
three: retrieval is deterministic and character count is arithmetic, so the
same reasoning `run_eval.py` gives for the relevance gate applies here.

```
Corpus: campus_life · top-k: 5
In range = 50-400 characters

Do financial aid packages for study abroad generally cover a student's trip?
  1. ok   249 chars  admin_study_abroad.txt#0
  2. ok   261 chars  admin_campus_jobs_and_financial_aid.txt#0
  3. ok   282 chars  admin_graduation_requirements.txt#0
  4. ok   230 chars  admin_printing_quota.txt#0
  5. ok   235 chars  money_textbooks.txt#0
  -> top-1 in range: True · all 5 in range: True

What do students say about the time it takes to get around campus?
  1. ok   220 chars  transit_shuttle.txt#0
  2. ok   245 chars  transit_walking.txt#0
  3. ok    81 chars  housing_old_brewhouse.txt#1
  4. ok    76 chars  housing_fenwick_court.txt#2
  5. ok   313 chars  dining_verrill_street_grill.txt#0
  -> top-1 in range: True · all 5 in range: True

What is the cost of the cheapest on-campus housing?
  1. ok    90 chars  housing_tamsin_court.txt#1
  2. ok   137 chars  money_textbooks.txt#1
  3. ok    76 chars  housing_fenwick_court.txt#2
  4. ok    87 chars  housing_morrow_house.txt#1
  5. ok    93 chars  housing_innisfree_hall.txt#1
  -> top-1 in range: True · all 5 in range: True

How late is the library open during the spring term?
  1. ok   163 chars  study_library_hours.txt#0
  2. ok   143 chars  housing_tamsin_court_noise.txt#1
  3. ok   143 chars  housing_calder_annexe_noise.txt#1
  4. ok   143 chars  housing_innisfree_hall_noise.txt#1
  5. ok   143 chars  housing_aldridge_hall_noise.txt#1
  -> top-1 in range: True · all 5 in range: True

Which course is known for having a heavy workload?
  1. ok   165 chars  course_biol_160_workload.txt#0
  2. ok    74 chars  course_biol_160.txt#1
  3. ok   134 chars  course_cs_210_workload.txt#0
  4. ok   160 chars  course_engl_205_workload.txt#0
  5. ok   235 chars  money_textbooks.txt#0
  -> top-1 in range: True · all 5 in range: True

Top-1 chunk in range:        5 of 5
All 5 chunks in range:     5 of 5
```

Every one of the 25 retrieved chunks is in range. So is every chunk in the
index — `chunker.py::split_documents` produces 179 chunks, shortest 57 and
longest 397. This criterion cannot fail. See Diagnoses in the README.
