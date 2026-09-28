# The Unofficial Guide

<!-- Ariella Efraim, Corpus: campus_life -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This project uses the campus_life corpus, which contains documents about student life, courses, housing, transportation, campus services, and other university topics. The system takes in a student's questions and searches documents for relevant information using similarity-based retrieval and embeddings. If the information retrieved is relevant to a certain corpus the system generates a short answer using only the document retrieved and naming the source document. If a question is asked outside the scope of campus life, the question is refused by the relevance gate in order to prevent random non-factual replies.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 50-character threshold for combining short paragraphs
**Overlap:** 0 Characters

After opening and reading a few of the documents associated with the campus_life corpus, I noticed that the text was typically short and contained small paragraphs that often represented separate thoughts. At first, I attempted strictly splitting the paragraphs with zero overlap. This resulted in 92 chunks under the 50 character limit I set as a criterion, so I chose to combine short paragraphs with neighboring content. This then produced 179 chunks with an average length of 154 characters, shortest of 57 characters, and longest of 397 characters. I chose this combination of small paragraphs in order to keep complete thoughts together while creating chunks that are not extremely large or small.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->


## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents` 

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_340_exams.txt#1` — produced by: `chunker.py::split_documents`

```
Start the term project in week three, not week eight; everyone learns this the hard way.
```

**Chunk 3** — source: `course_phys_130_workload.txt#1` — produced by: `chunker.py::split_documents`

```
It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `health_center.txt#0` — produced by: `chunker.py::split_documents`

```
The health centre

Walk-in hours are 8am to 11am; everything after that is by appointment and appointments run about a week out. If something is urgent, go at 8am and wait rather than booking.
```

**Chunk 5** — source: `housing_morrow_house.txt#1` — produced by: `chunker.py::split_documents`

```
The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** Do financial aid packages for study abroad generally cover a student's trip?

**Answer:** Yes, the financial aid package travels with you on the study abroad program.

**Source:** `admin_study_abroad.txt`


**My relevance cutoff:**
I kept my relevance cutoff at 0.60. I tested five questions covered by my campus_life documents and five other out-of-scope questions. For the five in-scope questions, the best distances ranged from 0.3193 to 0.4727. For the five out-of-scope questions, the best distances ranged from 0.7873 to 0.9228. Seeing as though there is a large gap between the two groups of questions from 0.4727 to 0.7873, I found that 0.6 falls within the gap. At this cutoff the five in-scope questions passed the relevance gate while the five out-of-scope questions were refused.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|Do financial aid packages for study abroad generally cover a student's trip?|Yes|0.3213|
|What do students say about the time it takes to get around campus?|Yes|0.4586|
|What is the cost of the cheapest on-campus housing?|Yes|0.3890|
|How late is the library open during the spring term?|Yes|0.3193|
|Which course is known for having a heavy workload?|Yes|0.4727|
|What is the capital of Mongolia?|No|0.7873|
|How do I change the oil in a diesel engine?|No|0.9228|
|Who won the 1994 World Cup?|No|0.8474|
|What is the recommended dosage of ibuprofen for a headache?|No|0.8243|
|How do I write a for loop in Rust?|No|0.8768|

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked AI to help me think through a chunking strategy for the campus_life documents. I am unfamiliar with chunking and so I read through suggestions Claude and ChatGPT had given me. Before taking all suggestions given I first read through a few documents to see what the average size of the documents were. From this I tested out different ways to split the paragraphs and if I should have included any overlap. I wrote out some pseudo code and asked ChatGPT to refine it for me and I ended up tweaking it a bit.

**2.** I asked Claude to explain the milestones in greater specifics for me, especially milestone number 3 and 4. I found myself mixing up my commands for milestone four so I asked Claude to write out a base of commands I would be using for the milestone. After doing this I was able to organize my terminal code and test my questions efficiently. I also inquired about the cutoff although I was told to experiment with .5 I decided to keep the cutoff at .6 because it clearly separated my in-scope and out-of-scope questions.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Retrieved chunk is between 50 and 400 characters | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. System produces an answer in under 8 seconds | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
**Source:** `run_2026-09-23_1952_before.md`
- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-23 19:52
## Real output
<!-- Criterion 1: Chunk Contains an Answer -->
### Which course is known for having a heavy workload? — run 1

- Best distance: 0.4727 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_workload.txt, course_cs_210_workload.txt, course_engl_205_workload.txt, money_textbooks.txt

```
BIOL 160 Cell Biology is known by reputation as the heaviest first-year course (from `course_biol_160_workload.txt` and `course_biol_160.txt`).
```
**Source:** `run_2026-09-23_1952_before.md`
<!-- Criterion 2: Source is Named -->
### Do financial aid packages for study abroad generally cover a student's trip? — run 2

- Best distance: 0.3213 (passed the gate)
- Sources retrieved: admin_campus_jobs_and_financial_aid.txt, admin_graduation_requirements.txt, admin_printing_quota.txt, admin_study_abroad.txt, money_textbooks.txt

```
Yes, the financial aid package travels with you on the study abroad program. 

Source: admin_study_abroad.txt
```
**Source:** `run_2026-09-23_1952_before.md`
<!-- Criterion 3: Out-of-Corpus Questions Stopped -->
## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.787 | refused |
| How do I change the oil in a diesel engine? | 0.923 | refused |
| Who won the 1994 World Cup? | 0.847 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.824 | refused |
| How do I write a for loop in Rust? | 0.877 | refused |

**Source:** `results/run_2026-09-27_criteria45_before.md`
<!-- Criterion 4 -->
## Retrieved chunk between 50 and 400 characters

Produced by `chunker.py::split_documents`, summarised by `chunker.py::describe`:

```
179 chunks, 154 characters on average (shortest 57, longest 397), produced by chunker.py::split_documents
```

Shortest 57, longest 397, against a range of 50 to 400. Every chunk in the
index is in range, so every retrieved chunk is necessarily in range: 5 of 5.
This criterion cannot fail. See Diagnoses below.

**Source:** `results/run_2026-09-27_criteria45_before.md`
<!-- Criterion 5 -->
## Answer in under 8 seconds

Produced by `measure_timing.py`, timing `store.py::search` → `gate.py::check` →
`generate.py::answer_from_chunks`, caching off.

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
first question of the first run — that one includes loading the embedding
model. Every answer after it came back in about a second.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | **MET** | 4 of 5 questions had the answer in a retrieved chunk, meeting the target of at least 4 of 5. `scorer.py` reported 5 of 5, but I read the chunks myself, question 3 asks the cost of the cheapest housing and no document in my corpus states a rent figure, only that Morrow House is cheaper by about $900 a year. |
| 2 | Every answer names a source | **MET** | Across the 3 runs, all 15 answers named at least one source file. |
| 3 | Gate stops out-of-corpus questions | **MET** | 5 of 5 refused, the threshold was 0.6 and the distances ranged from 0.787-0.923. |
| 4 | Retrieved chunk is between 50 and 400 characters | **MET** | 5 of 5 affirmed, all test chunks were between 50 and 400 characters. Revision: original was "the retrieved chunk" but top-k is 5, so it now refers to all 5.|
| 5 | System produces an answer in under 8 seconds | **MET** | 5 of 5 affirmed, the slowest answer was 2.607 seconds, way below the 8 second limit. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

**I missed nothing.** All five criteria were MET on all three runs.

### My targets were set low
- **Criterion 4 cannot fail.** `chunker.py::split_documents` produces 179 chunks, shortest 57 and longest 397. My range is 50 to 400, so every chunk is already inside it before retrieval runs. I could break retrieval completely and still score 5 of 5.
- **Criterion 5 cleared by about eight times.** Slowest answer 2.607s against an 8-second target, and that one included loading the embedding model. Everything after it came back in about a second. I picked 8 seconds to allow time for embedding and processing without measuring how much time it would take first.
- **Criterion 3 never tested the gate near its cutoff.** Distances ran 0.787 to 0.923 against a cutoff of 0.6, so nothing came within 0.18 of the boundary. I proved the gate rejects questions about Mongolia, which was never in doubt.

### Question 3 — the one question that failed
**Stage: loading. Mechanism: the fact never entered the pipeline.**
Question 3 asks the cost of the cheapest housing. The nearest chunk, `housing_morrow_house.txt#1`, says *"cheapest housing tier by about $900 a year"* which is a difference between tiers, not a price. All 19 dollar amounts in my corpus are laundry, meals, transcripts or printing. None is a rent.

My pipeline runs in five steps: loading, chunking, embedding, retrieval, then generation. To find where a question went wrong, I started at the end and worked backwards. If the model had what it needed and did not use it, the problem would be generation. But the answer was not in any of the chunks, so something earlier had gone wrong. I then went and read the documents themselves, and the figure was not in any of them either. That puts the problem at loading, the very first step. None of the later steps can find a fact that was never there to begin with.

### What I would tighten, and to what
**Criterion 3 — plausible out-of-corpus questions instead of absurd ones.** I checked which topics my 88 documents genuinely miss rather than guessing: nothing on the gym, career services, tutoring, campus mail or scholarships.
Those questions sound like ones my corpus does answer, so they should land near 0.6 rather than above 0.78. The target stays at 4 of 5; only the test gets harder. Making the tests harder will better test if the system is learning.

**Criterion 4 — measure relevance instead of length.** Chunk length does not tell me whether a chunk is useful. A 200-character chunk about laundry is the right length but not relevant for a question about the library. What I actually care about is whether the chunks are relevant. My system already measures that for me: every chunk comes back with a distance, and a smaller distance means the chunk is closer to the question. An alternate tightened version: *for at least 4 of my 5 questions, all five retrieved chunks are within the 0.6 cutoff.* My before run scores 4 of 5 on that. Question 1 fails, because three of its chunks were at 0.662, 0.738 and 0.747 and reached the model anyway — `gate.py::check` only checks the closest chunk, so the rest ride along. Unlike my original, this is a criterion my system can fail.

## The Improvement

**What I changed:** I added `gate.py::keep_relevant`, which drops any retrieved chunk further from the question than the 0.6 cutoff, and called it in `run_eval.py::run_once` after the gate decision. `gate.py::check` is untouched, so the refuse/allow decision works exactly as before. The only thing that changed is which chunks reach the model.

**Why I picked it:** My diagnosis found that question 1 handed the model three chunks at 0.662, 0.738 and 0.747 because `gate.py::check` only tests the closest chunk, so once that one clears the cutoff the rest ride along regardless.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Retrieved chunk is between 50 and 400 characters | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. System produces an answer in under 8 seconds | 5 of 5 | 4/5 | 5/5 | 5/5 | **MISSED** |

**Did it help?**

Yes, but none of my five criteria can show it.

Before the change, question 1 sent the model five chunks and three of them were past the 0.6 cutoff. After the change it sends two chunks and both are under the cutoff. That is what I wanted the fix to do. In Diagnoses I said a better criterion would be that every chunk sent to the model is within the cutoff. My before run scores 4 of 5 on that and my after run scores 5 of 5.

Criteria 1 to 4 stayed exactly the same, which I expected before I ran anything. Criterion 1 cannot go above 4 of 5 because question 3 asks for a figure my corpus does not have. Criteria 2, 3 and 4 were already at 5 of 5, so there was no room for them to go up. Criterion 3 also could not change because I left `gate.py::check` alone on purpose.

Criterion 5 went from MET to MISSED. One answer in run 1 took 11.898 seconds, which is over my 8 second target. That time is not my system doing work. It is `time.sleep()` inside `generate.py::_wait_for_slot`, which limits requests to 30 per minute, and I had run the eval script and the timing script close together. My change makes the prompt shorter, not longer, so it cannot be the reason anything got slower. I am still recording it as MISSED, as the number is larger than 8 seconds.

Overall, my system improved, but my test could not tell.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
