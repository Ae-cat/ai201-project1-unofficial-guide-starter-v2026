import time

import config
import questions as qs
import gate
from store import search
from generate import answer_from_chunks


for run in range(1, 4):
    print(f"\n=== Timing Run {run} ===")

    for item in qs.QUESTIONS:
        question = item["question"]

        start_time = time.perf_counter()

        results = search(
            question,
            top_k=config.TOP_K,
            corpus=config.CORPUS,
            variant="default"
        )

        decision = gate.check(results, threshold=config.THRESHOLD)

        if decision.passed:
            answer = answer_from_chunks(
                question,
                results,
                cache=False
            )
        else:
            answer = "I don't have enough information about that"

        elapsed_time = time.perf_counter() - start_time

        print(f"{elapsed_time:.3f} seconds | {question}")