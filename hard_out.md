  extracted story-01
  extracted story-02
  extracted story-03
  extracted story-04
  extracted story-05
  extracted story-06

### Part 1: extraction per story

| story | parsed | validated | null fields | contradictions | unpublished | evidence not verbatim |
|---|---|---|---|---|---|---|
| story-01 | yes | yes | - | 0 | 0 | candidate_id |
| story-02 | yes | yes | graduation_year, gpa_4_scale | 0 | 0 | - |
| story-03 | yes | yes | - | 0 | 1 | candidate_id |
| story-04 | yes | yes | - | 0 | 3 | candidate_id |
| story-05 | yes | yes | - | 0 | 1 | - |
| story-06 | yes | yes | graduation_year, gpa_4_scale | 2 | 1 | candidate_id |

Полные записи (по ним заполняешь trap table: GPA-шкала, submitted/in press, противоречия и т.д.):

story-01 {
 "candidate_id": "story-01",
 "full_name": "Aziza Bekova",
 "degree": "BSc in Computer Science",
 "graduation_year": 2025,
 "gpa_4_scale": 3.8,
 "gpa_original": {
  "value": 3.8,
  "scale": "4.0 scale"
 },
 "languages": [
  "Kazakh",
  "Russian",
  "English"
 ],
 "published_outputs": 2,
 "unpublished_outputs": [],
 "experience_months": 8,
 "experience_notes": "October 2023 to May 2024 = eight months; no overlapping relevant periods stated.",
 "contradictions": [],
 "evidence": {
  "candidate_id": "candidate_id: story-01",
  "full_name": "Aziza Bekova",
  "degree": "I completed my BSc in Computer Science in June 2025.",
  "graduation_year": "I completed my BSc in Computer Science in June 2025.",
  "gpa_4_scale": "My final GPA was 3.8 on a 4.0 scale.",
  "gpa_original": "My final GPA was 3.8 on a 4.0 scale.",
  "languages": "I speak Kazakh and Russian fluently and my English is at C1.",
  "published_outputs": "The first is a paper on retrieval quality that appeared in a peer-reviewed workshop proceedings in 2025 — this is published and I can send the DOI. The second is a short paper on evaluation methods that was published in a regional journal in early 2026. Both are peer-reviewed publications.",
  "experience_months": "Between my second and fourth years I worked part-time for a data team as a junior analyst, from October 2023 to May 2024, eight months in total.",
  "experience_notes": "from October 2023 to May 2024, eight months in total"
 }
}
story-02 {
 "candidate_id": "story-02",
 "full_name": "Dias Yerzhanov",
 "degree": "Bachelor's in Information Systems",
 "graduation_year": null,
 "gpa_4_scale": null,
 "gpa_original": {
  "value": null,
  "scale": null
 },
 "languages": [
  "Kazakh",
  "Russian",
  "English (B2)"
 ],
 "published_outputs": 1,
 "unpublished_outputs": [],
 "experience_months": 36,
 "experience_notes": "One continuous employment period: three years × 12 months = 36 months.",
 "contradictions": [],
 "evidence": {
  "full_name": "# scholarship application - Dias Yerzhanov",
  "degree": "I finished my bachelor's in Information Systems last year with a diploma with distinction.",
  "languages": "Languages: Kazakh, Russian, English (B2).",
  "published_outputs": "On the research side I have one published paper, in a student conference proceedings, about the scheduling tool.",
  "experience_months": "I have been employed continuously for three years. That is thirty-six months as a backend developer at a logistics company, starting the month after my third year ended and continuing today."
 }
}
story-03 {
 "candidate_id": "story-03",
 "full_name": "Lyazzat Omarova",
 "degree": "BSc in Applied Mathematics",
 "graduation_year": 2025,
 "gpa_4_scale": 3.68,
 "gpa_original": {
  "value": 4.6,
  "scale": "5.0"
 },
 "languages": [
  "Kazakh",
  "Russian",
  "English"
 ],
 "published_outputs": 1,
 "unpublished_outputs": [
  {
   "description": "Second paper",
   "status": "under review"
  }
 ],
 "experience_months": 14,
 "experience_notes": "9 + 5 = 14 months; the internships did not overlap.",
 "contradictions": [],
 "evidence": {
  "candidate_id": "candidate_id: story-03",
  "full_name": "# Lyazzat Omarova — application notes",
  "degree": "**Degree.** BSc in Applied Mathematics, completed 2025.",
  "graduation_year": "**Degree.** BSc in Applied Mathematics, completed 2025.",
  "gpa_4_scale": "My GPA was 4.6 out of 5.0.",
  "gpa_original": "My GPA was 4.6 out of 5.0.",
  "languages": "**Languages.** Kazakh, Russian, English.",
  "published_outputs": "One paper published in 2024 in a peer-reviewed conference proceedings (graph theory, a small result, entirely mine).",
  "unpublished_outputs": "A second paper is under review at a journal since March 2026 — I am listing it for completeness and I understand it does not count as published.",
  "experience_months": "The first, nine months, at a risk department building spreadsheet models. The second, five months, at a research institute working on graph tooling. They did not overlap: the first ran from June 2023 to February 2024, the second from March 2024 to July 2024.",
  "experience_notes": "The first, nine months, at a risk department building spreadsheet models. The second, five months, at a research institute working on graph tooling. They did not overlap: the first ran from June 2023 to February 2024, the second from March 2024 to July 2024."
 }
}
story-04 {
 "candidate_id": "story-04",
 "full_name": "Tamerlan Saparov",
 "degree": "BSc in Computer Science",
 "graduation_year": 2026,
 "gpa_4_scale": 3.6,
 "gpa_original": {
  "value": 3.6,
  "scale": "4.0"
 },
 "languages": [
  "Kazakh",
  "Russian",
  "English",
  "Turkish (A2)"
 ],
 "published_outputs": 1,
 "unpublished_outputs": [
  {
   "description": "A survey of Kazakh NLP resources",
   "status": "under review"
  },
  {
   "description": "Tokenizers considered harmful",
   "status": "in preparation"
  },
  {
   "description": "Evaluation without annotation",
   "status": "in preparation"
  }
 ],
 "experience_months": 24,
 "experience_notes": "September 2023 to September 2025 = 24 months; the story states twenty-four months in total.",
 "contradictions": [],
 "evidence": {
  "candidate_id": "candidate_id: story-04",
  "full_name": "Tamerlan Saparov",
  "degree": "BSc in Computer Science, graduating 2026.",
  "graduation_year": "BSc in Computer Science, graduating 2026.",
  "gpa_4_scale": "GPA 3.6 on a 4.0 scale.",
  "gpa_original": "GPA 3.6 on a 4.0 scale.",
  "languages": "Kazakh, Russian, English, Turkish (A2).",
  "published_outputs": "*Sparse attention for low-resource Kazakh*, published in a peer-reviewed conference proceedings, 2024. Published.",
  "unpublished_outputs": "2. *A survey of Kazakh NLP resources*, submitted to a journal in January 2026. Under review.\n3. *Tokenizers considered harmful*, in preparation. Not submitted anywhere.\n4. *Evaluation without annotation*, in preparation. Also not submitted.",
  "experience_months": "Twenty-four months in total at a language-technology startup, from September 2023 to September 2025, full-time in the summers and part-time during term.",
  "experience_notes": "Twenty-four months in total at a language-technology startup, from September 2023 to September 2025, full-time in the summers and part-time during term."
 }
}
story-05 {
 "candidate_id": "story-05",
 "full_name": "Аиша Нұрланқызы",
 "degree": "информатика бакалавриаты",
 "graduation_year": 2025,
 "gpa_4_scale": 3.9,
 "gpa_original": {
  "value": 3.9,
  "scale": "4.0"
 },
 "languages": [
  "қазақ",
  "орыс",
  "ағылшын (C1)"
 ],
 "published_outputs": 1,
 "unpublished_outputs": [
  {
   "description": "мақала",
   "status": "in preparation"
  }
 ],
 "experience_months": 6,
 "experience_notes": "2025 жылғы қыркүйектен 2026 жылғы ақпанға дейінгі тағылымдама: 6 ай.",
 "contradictions": [],
 "evidence": {
  "full_name": "Менің атым Аиша Нұрланқызы.",
  "degree": "2025 жылы информатика бакалавриатын бітірдім.",
  "graduation_year": "2025 жылы информатика бакалавриатын бітірдім.",
  "gpa_4_scale": "GPA-м 3.9 (4.0 шкаласы бойынша) — бұл менің транскриптімде жазылған сан.",
  "gpa_original": "GPA-м 3.9 (4.0 шкаласы бойынша) — бұл менің транскриптімде жазылған сан.",
  "languages": "Тілдер: қазақ, орыс, ағылшын (C1).",
  "published_outputs": "2025 жылы рецензияланатын конференция жинағында бір мақалам жарияланды, деректер жиынтығының сапасы туралы еді.",
  "unpublished_outputs": "Тағы бір мақала жазылып жатыр, бірақ ол әлі еш жерге жіберілген жоқ.",
  "experience_months": "2025 жылдың қыркүйегінен 2026 жылдың ақпанына дейін бір компанияда алты ай тағылымдамадан өттім.",
  "experience_notes": "2025 жылдың қыркүйегінен 2026 жылдың ақпанына дейін бір компанияда алты ай тағылымдамадан өттім."
 }
}
story-06 {
 "candidate_id": "story-06",
 "full_name": "Nurzhan Abilov",
 "degree": "BSc in Statistics",
 "graduation_year": null,
 "gpa_4_scale": null,
 "gpa_original": {
  "value": null,
  "scale": null
 },
 "languages": [
  "Kazakh",
  "Russian",
  "English"
 ],
 "published_outputs": 1,
 "unpublished_outputs": [
  {
   "description": "One poster at a local event",
   "status": "not counted as a publication"
  }
 ],
 "experience_months": 40,
 "experience_notes": "Insurance analytics work since February 2023, stated as about forty months; total = 40 months. The first 8 months were part-time, followed by full-time work.",
 "contradictions": [
  {
   "field": "gpa",
   "values": [
    3.2,
    3.5
   ],
   "quotes": [
    "My GPA was 3.2. Actually I should\ndouble-check that, I think it was 3.5 — the 3.2 might be from the transcript I\nprinted in third year."
   ]
  },
  {
   "field": "graduation_year",
   "values": [
    2024,
    2026
   ],
   "quotes": [
    "I graduated in 2024 with a BSc in Statistics.",
    "I am\ncurrently a final-year student graduating in 2026"
   ]
  }
 ],
 "evidence": {
  "candidate_id": "candidate_id: story-06",
  "full_name": "# Nurzhan Abilov",
  "degree": "I graduated in 2024 with a BSc in Statistics.",
  "gpa_original": "My GPA was 3.2. Actually I should\ndouble-check that, I think it was 3.5 — the 3.2 might be from the transcript I\nprinted in third year.",
  "languages": "Languages: Kazakh, Russian, English.",
  "published_outputs": "Research: one paper published, in a peer-reviewed proceedings, on survey\nweighting.",
  "unpublished_outputs": "One poster at a local event, which I do not think counts.",
  "experience_months": "I have been at an insurance analytics team since February 2023, which is\nabout forty months. I was part-time for the first eight of those while I was\nstill studying, then full-time.",
  "experience_notes": "I have been at an insurance analytics team since February 2023, which is\nabout forty months. I was part-time for the first eight of those while I was\nstill studying, then full-time."
 }
}

### Part 2: scores (model) and weighted total (code), 0-5 scale

weights: {'academic': 0.5, 'research': 0.3, 'experience': 0.2}
| candidate | academic | research | experience | total |
|---|---|---|---|---|
| story-01 | 5 | 5 | 2 | 4.4 |
| story-04 | 4 | 3 | 5 | 3.9 |
| story-05 | 5 | 3 | 1 | 3.6 |
| story-03 | 4 | 3 | 3 | 3.5 |
| story-02 | 3 | 3 | 5 | 3.4 |
| story-06 | 2 | 3 | 5 | 2.9 |

COMPUTED WINNER: story-01 (4.4)
Gap top-2: 0.5

Notes от модели:
  story-01: {"academic": "Completed a BSc in Computer Science with a final GPA of 3.8 on a 4.0 scale.", "research": "Has two published peer-reviewed outputs: one in 2025 workshop proceedings and one in a regional journal in early 2026.", "experience": "Has eight months of directly relevant junior data analyst experience from October 2023 to May 2024."}
  story-02: {"academic": "A bachelor's degree in Information Systems with a diploma with distinction is stated, but no GPA or grading scale is provided.", "research": "One published paper in student conference proceedings is stated, which is below the two published peer-reviewed outputs required for a top score.", "experience": "Thirty-six continuous months as a backend developer at a logistics company are stated, meeting the two-year relevant-experience threshold."}
  story-03: {"academic": "BSc in Applied Mathematics with a clearly stated GPA of 4.6/5.0, equivalent to 3.68/4.0, just below the 3.7 threshold for a 5.", "research": "One peer-reviewed conference proceeding is published, while the second paper is under review and does not count.", "experience": "Fourteen non-overlapping months of relevant experience are stated: nine months in risk modeling and five months in graph tooling at a research institute."}
  story-04: {"academic": "BSc in Computer Science with a clearly stated GPA of 3.6 on a 4.0 scale, which is strong but below the 3.7 threshold for a 5.", "research": "One peer-reviewed conference publication is stated as published; the other outputs are under review or in preparation and therefore do not count as published.", "experience": "The story states 24 months of relevant full-time and part-time experience at a language-technology startup from September 2023 to September 2025."}
  story-05: {"academic": "Информатика бакалавриаты және 3.9/4.0 GPA анық көрсетілген, бұл өте күшті академиялық көрсеткіш.", "research": "Рецензияланатын конференция жинағында бір мақала жарияланған; екінші мақала әлі дайындалу үстінде және есепке алынбайды.", "experience": "2025 жылғы қыркүйек пен 2026 жылғы ақпан аралығында алты айлық тағылымдама көрсетілген, бұл тікелей релевантты тәжірибенің алты айы."}
  story-06: {"academic": "BSc in Statistics is stated, but the GPA is contradictory (3.2 versus 3.5), so no reliable GPA can be used.", "research": "One peer-reviewed proceedings paper is stated as published; the local poster is not counted as a publication.", "experience": "Insurance analytics experience is stated as 40 months, including eight months part-time and subsequent full-time work."}

### Prose answer (separate call)

Using the rubric’s three criteria, I would rank the candidates as follows. I have treated one published output as a score of 3 for research, two published outputs as 5, and mapped experience approximately from the stated month totals, with 24 months or more receiving 5.

1. **Aziza Bekova — winner**  
   Academic record: **5/5** — BSc in Computer Science and GPA 3.8/4.0.  
   Research output: **5/5** — two peer-reviewed publications, both explicitly published.  
   Relevant experience: **2/5** — eight months of relevant data-team work.  
   Weighted total: **4.40/5**.  
   Aziza is the strongest overall candidate because she is the only applicant with both an excellent GPA and two qualifying publications. Her shorter experience is outweighed by her academic and research strength.

2. **Tamerlan Saparov**  
   Academic record: **4/5** — GPA 3.6/4.0, clearly reported but below the rubric’s 3.7 benchmark for the top score.  
   Research output: **3/5** — one published peer-reviewed paper; the other items are under review or in preparation and do not count.  
   Relevant experience: **5/5** — 24 months in language technology.  
   Weighted total: **3.90/5**.

3. **Lyazzat Omarova**  
   Academic record: **4/5** — GPA 4.6/5.0, converted in the record to 3.68/4.0; strong, though just below the 3.7 benchmark.  
   Research output: **3/5** — one published peer-reviewed paper. The second paper is under review and is excluded.  
   Relevant experience: **3/5** — 14 non-overlapping months.  
   Weighted total: **3.50/5**.

4. **Аиша Нұрланқызы**  
   Academic record: **5/5** — GPA 3.9/4.0 and a completed bachelor’s degree.  
   Research output: **3/5** — one published peer-reviewed conference paper; the second paper is still in preparation.  
   Relevant experience: **1/5** — six months of internship experience.  
   Weighted total: **3.40/5**.  
   Aisha has an excellent academic record, but her limited experience keeps her below Tamerlan and Lyazzat.

5. **Dias Yerzhanov**  
   Academic record: **0/5** — the degree and distinction are stated, but no GPA is provided. Under the rubric, a story without a GPA scores zero academically.  
   Research output: **3/5** — one published paper.  
   Relevant experience: **5/5** — 36 months of continuous backend-development work.  
   Weighted total: **2.40/5**.

6. **Nurzhan Abilov**  
   Academic record: **0/5** — the story contradicts itself about both GPA and graduation status. I would not resolve or average the GPA, so no reliable academic score can be awarded.  
   Research output: **3/5** — one published peer-reviewed paper; the poster does not count.  
   Relevant experience: **5/5** — approximately 40 months in insurance analytics.  
   Weighted total: **2.40/5**.

Dias and Nurzhan are tied under this conservative treatment. The scholarship should go to **Aziza Bekova**, whose combination of a 3.8/4.0 GPA and two qualifying publications gives her a clear lead despite having only eight months of relevant experience.
