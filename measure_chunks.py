"""
Criterion 4: how long are the chunks retrieval actually hands back?

Retrieval is deterministic, so this is one pass, not three — same reasoning
run_eval.py gives for the relevance gate.

    python measure_chunks.py
"""

import config
import questions as qs
from store import search

IN_RANGE_MIN = 50
IN_RANGE_MAX = 400

print(f"Corpus: {config.CORPUS} · top-k: {config.TOP_K}")
print(f"In range = {IN_RANGE_MIN}-{IN_RANGE_MAX} characters\n")

top1_in_range = 0
all_in_range = 0

for item in qs.QUESTIONS:
    question = item["question"]
    results = search(
        question,
        top_k=config.TOP_K,
        corpus=config.CORPUS,
        variant="default",
    )

    lengths = [len(r.text) for r in results]
    top1_ok = IN_RANGE_MIN <= lengths[0] <= IN_RANGE_MAX
    all_ok = all(IN_RANGE_MIN <= n <= IN_RANGE_MAX for n in lengths)

    top1_in_range += top1_ok
    all_in_range += all_ok

    print(question)
    for rank, result in enumerate(results, start=1):
        length = len(result.text)
        flag = "ok " if IN_RANGE_MIN <= length <= IN_RANGE_MAX else "OUT"
        # Would this chunk survive the cutoff on its own? gate.py only checks
        # the nearest one, so everything behind it rides along regardless.
        own = "under" if result.distance <= config.THRESHOLD else "OVER "
        print(
            f"  {rank}. {flag} {length:>4} chars  "
            f"dist {result.distance:.3f} {own} cutoff  {result.label}"
        )
    print(f"  -> top-1 in range: {top1_ok} · all {len(results)} in range: {all_ok}\n")

total = len(qs.QUESTIONS)
print(f"Top-1 chunk in range:        {top1_in_range} of {total}")
print(f"All {config.TOP_K} chunks in range:     {all_in_range} of {total}")
