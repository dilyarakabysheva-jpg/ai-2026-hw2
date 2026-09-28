=== RUN A: uncompressed ===
-- <compress> skipped
=== RUN B: compressed ===
-- compressed. summary call sent 1447 tokens; turns thrown away; state is now sent instead.

### Tokens sent per call

| call | uncompressed | compressed |
|---|---|---|
| turn 1 | 742 | 742 |
| turn 2 | 854 | 880 |
| turn 3 | 975 | 1032 |
| turn 4 | 1102 | 1157 |
| turn 5 | 1214 | 1254 |
| turn 6 | 1356 | 1367 |
| turn 7 | 1495 | 1495 |
| turn 8 | 1629 | 1619 |
| turn 9 | 1757 | 1738 |
| compress (summary call, не считается в peak) | - | 1447 |
| turn 10 | 1881 | 952 |
| turn 11 | 2005 | 1057 |
| probe 1 | 2109 | 1147 |
| probe 2 | 2107 | 1145 |
| probe 3 | 2112 | 1150 |
| probe 4 | 2110 | 1148 |
| probe 5 | 2107 | 1145 |

### Peak tokens sent in one call

| run | peak |
|---|---|
| uncompressed | 2112 |
| compressed | 1738 |

### Probes (проверь ответы глазами: автосовпадение — подстрока, перефраз он не поймёт)

| probe | question | uncompressed hit | compressed hit |
|---|---|---|---|
| 1 | Which applicant am I, and what is my number? | None | None |
| 2 | Which document is still missing from my file? | None | None |
| 3 | What is my income band, and what amount does that come to? | None | None |
| 4 | Which day of the week can I come to the office? | None | None |
| 5 | What did I ask you about my employer? | None | None |

retrieved: uncompressed 0/5, compressed 0/5

P1: Which applicant am I, and what is my number?
  A: {"applicant_id":"A-202","found":true,"decision":"refused","amount":0,"missing_documents":["id_card"],"reason":"You are Daniyar Qoshan, applicant A-202. Your transcript is on file, but your id_card is still missing. Your current decision is refused, with a potential grant amount of 150,000 KZT once the id_card is submitted and recorded."}
  B: {"applicant_id":"A-202","found":true,"decision":"more_info","amount":0,"missing_documents":["id_card"],"reason":"You are recorded as Daniyar Qoshan, applicant number A-202. Your id card is still missing from the file."}

P2: Which document is still missing from my file?
  A: {"applicant_id":"A-202","found":true,"decision":"refused","amount":0,"missing_documents":["id_card"],"reason":"The id_card is still missing from Daniyar Qoshan’s file. The transcript is on record."}
  B: {"applicant_id":"A-202","found":true,"decision":"more_info","amount":0,"missing_documents":["id_card"],"reason":"The id card is still missing from your file. It must be submitted and recorded before your grant can be considered."}

P3: What is my income band, and what amount does that come to?
  A: {"applicant_id":"A-202","found":true,"decision":"refused","amount":0,"missing_documents":["id_card"],"reason":"Your recorded income band is 2. The grant amount for income band 2 is 150,000 KZT, but your current granted amount is 0 KZT because the id_card is still missing from your file."}
  B: {"applicant_id":"A-202","found":true,"decision":"more_info","amount":150000,"missing_documents":["id_card"],"reason":"Your recorded income band is 2, which corresponds to a grant amount of 150,000 KZT. The grant cannot be considered until your id card is submitted and recorded."}

P4: Which day of the week can I come to the office?
  A: {"applicant_id":"A-202","found":true,"decision":"refused","amount":0,"missing_documents":["id_card"],"reason":"You stated that you can come to the office on Thursdays. The record does not specify office hours or appointment availability. Your id_card remains missing, so the current decision is refused; the potential grant amount is 150,000 KZT once it is submitted and recorded."}
  B: {"applicant_id":"A-202","found":true,"decision":"more_info","amount":0,"missing_documents":["id_card"],"reason":"You can come to the office on Thursdays. Your id card is still missing and must be submitted and recorded before the grant can be considered."}

P5: What did I ask you about my employer?
  A: {"applicant_id":"A-202","found":true,"decision":"refused","amount":0,"missing_documents":["id_card"],"reason":"You asked whether a scanned letter from your employer would count or whether the original was required. The policy does not specify this, and an employer letter does not replace the missing id_card."}
  B: {"applicant_id":"A-202","found":true,"decision":"more_info","amount":150000,"missing_documents":["id_card"],"reason":"You asked whether a scanned employer letter might be relevant to your application and whether a scanned copy would be accepted or the original would be required. The employer letter is not listed as a required document in the grant policy."}

### State object (compressed run)

{
  "applicant_id": "A-202",
  "topic": "Study grant application",
  "facts": [
    "Applicant stated that their name is Daniyar Qoshan.",
    "Applicant stated that they sent their transcript last week.",
    "Applicant stated that their income band is 2 and that their family certificate says so.",
    "Applicant stated that they could not upload their id card because their home scanner broke.",
    "Applicant stated that their sister Aruzhan applied last year and is on file.",
    "Applicant stated that a scanned employer letter may be relevant to the application."
  ],
  "decisions": [],
  "constraints": [
    "Applicant can only come to the office on Thursdays because they have lab all week otherwise.",
    "The id_card must be submitted and recorded before the grant can be considered."
  ],
  "open_questions": [
    "Whether a scanned employer letter is accepted or the original is required.",
    "Whether the decision will be made on the same day if the applicant brings the id_card on Thursday."
  ],
  "language": "English and Kazakh"
}
