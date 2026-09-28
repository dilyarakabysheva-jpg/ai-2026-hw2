  done policy_officer E-01
  done policy_officer E-02
  done policy_officer E-03
  done policy_officer E-04
  done policy_officer E-05
  done policy_officer E-06
  done policy_officer E-07
  done policy_officer E-08
  done policy_officer E-09
  done policy_officer E-10
  done front_desk E-01
  done front_desk E-02
  done front_desk E-03
  done front_desk E-04
  done front_desk E-05
  done front_desk E-06
  done front_desk E-07
  done front_desk E-08
  done front_desk E-09
  done front_desk E-10
  done auditor E-01
  done auditor E-02
  done auditor E-03
  done auditor E-04
  done auditor E-05
  done auditor E-06
  done auditor E-07
  done auditor E-08
  done auditor E-09
  done auditor E-10
  done bilingual_clerk E-01
  done bilingual_clerk E-02
  done bilingual_clerk E-03
  done bilingual_clerk E-04
  done bilingual_clerk E-05
  done bilingual_clerk E-06
  done bilingual_clerk E-07
  done bilingual_clerk E-08
  done bilingual_clerk E-09
  done bilingual_clerk E-10

### Role: policy_officer  (все 4 поля совпали с expected: 10/10)

| enquiry | parsed | schema | found==expected | decision==expected | amount==expected | missing_documents==expected |
|---|---|---|---|---|---|---|
| E-01 | yes | yes | ok | ok | ok | ok |
| E-02 | yes | yes | ok | ok | ok | ok |
| E-03 | yes | yes | ok | ok | ok | ok |
| E-04 | yes | yes | ok | ok | ok | ok |
| E-05 | yes | yes | ok | ok | ok | ok |
| E-06 | yes | yes | ok | ok | ok | ok |
| E-07 | yes | yes | ok | ok | ok | ok |
| E-08 | yes | yes | ok | ok | ok | ok |
| E-09 | yes | yes | ok | ok | ok | ok |
| E-10 | yes | yes | ok | ok | ok | ok |

### Role: front_desk  (все 4 поля совпали с expected: 7/10)

| enquiry | parsed | schema | found==expected | decision==expected | amount==expected | missing_documents==expected |
|---|---|---|---|---|---|---|
| E-01 | yes | yes | ok | ok | ok | ok |
| E-02 | yes | yes | ok | ok | ok | ok |
| E-03 | yes | yes | ok | DIFF | ok | ok |
| E-04 | yes | yes | ok | DIFF | ok | ok |
| E-05 | yes | yes | ok | ok | ok | ok |
| E-06 | yes | yes | ok | ok | ok | ok |
| E-07 | yes | yes | ok | ok | ok | ok |
| E-08 | yes | yes | ok | ok | ok | ok |
| E-09 | yes | yes | ok | DIFF | ok | ok |
| E-10 | yes | yes | ok | ok | ok | ok |

### Role: auditor  (все 4 поля совпали с expected: 8/10)

| enquiry | parsed | schema | found==expected | decision==expected | amount==expected | missing_documents==expected |
|---|---|---|---|---|---|---|
| E-01 | yes | yes | ok | DIFF | DIFF | ok |
| E-02 | yes | yes | ok | ok | ok | ok |
| E-03 | yes | yes | ok | ok | ok | ok |
| E-04 | yes | yes | ok | ok | ok | ok |
| E-05 | yes | yes | ok | DIFF | DIFF | ok |
| E-06 | yes | yes | ok | ok | ok | ok |
| E-07 | yes | yes | ok | ok | ok | ok |
| E-08 | yes | yes | ok | ok | ok | ok |
| E-09 | yes | yes | ok | ok | ok | ok |
| E-10 | yes | yes | ok | ok | ok | ok |

### Role: bilingual_clerk  (все 4 поля совпали с expected: 9/10)

| enquiry | parsed | schema | found==expected | decision==expected | amount==expected | missing_documents==expected |
|---|---|---|---|---|---|---|
| E-01 | yes | yes | ok | ok | ok | ok |
| E-02 | yes | yes | ok | ok | ok | ok |
| E-03 | yes | yes | ok | ok | ok | ok |
| E-04 | yes | yes | ok | ok | ok | ok |
| E-05 | yes | yes | ok | ok | ok | ok |
| E-06 | yes | yes | ok | ok | ok | ok |
| E-07 | yes | yes | ok | ok | ok | ok |
| E-08 | yes | yes | ok | ok | ok | ok |
| E-09 | yes | yes | ok | ok | ok | ok |
| E-10 | yes | yes | ok | DIFF | ok | ok |

### Field movement vs policy_officer

| field | role | n moved | enquiries |
|---|---|---|---|
| found | front_desk | 0 | — (не сдвинулась) |
| found | auditor | 0 | — (не сдвинулась) |
| found | bilingual_clerk | 0 | — (не сдвинулась) |
| decision | front_desk | 3 | E-03, E-04, E-09 |
| decision | auditor | 2 | E-01, E-05 |
| decision | bilingual_clerk | 1 | E-10 |
| amount | front_desk | 0 | — (не сдвинулась) |
| amount | auditor | 2 | E-01, E-05 |
| amount | bilingual_clerk | 0 | — (не сдвинулась) |
| missing_documents | front_desk | 0 | — (не сдвинулась) |
| missing_documents | auditor | 0 | — (не сдвинулась) |
| missing_documents | bilingual_clerk | 0 | — (не сдвинулась) |

### Reasons (по ним смотришь, какая роль двигает только reason)


E-01
  policy_officer   -> granted: The record shows GPA 3.4, income band 1, and both required documents: transcript and id_card. The applicant qualifies for 250,000 KZT.
  front_desk       -> granted: You qualify for the Need-based study grant 2026: your GPA is 3.4, your income band is 1, and your transcript and id card are on file.
  auditor          -> more_info: The record shows GPA 3.4, income band 1, and both required documents (transcript and id_card), meeting the Need-based study grant 2026 eligibility rule. However, under the grant-office first-reading rule, a second reader is required before any grant is granted.
  bilingual_clerk  -> granted: You qualify because your GPA is 3.4, your income band is 1, and both the transcript and id card are on file.

E-02
  policy_officer   -> more_info: The applicant meets the GPA and income-band requirements but the id card is not on file.
  front_desk       -> more_info: Please provide the id card; the transcript is on file, and all other eligibility requirements are met.
  auditor          -> more_info: The record for Daniyar Qoshan (A-202) shows GPA 2.9 and income band 2, which meet the Policy's GPA and income requirements. The Policy requires both a transcript and an id_card; only the transcript is on file. The id_card is still needed for further review.
  bilingual_clerk  -> more_info: The applicant meets the GPA and income-band requirements, but the id card is not on file.

E-03
  policy_officer   -> refused: Refused: GPA 2.4 is below the minimum required GPA of 2.67.
  front_desk       -> more_info: Please return with an updated academic record showing a GPA of at least 2.67; the current recorded GPA is 2.4.
  auditor          -> refused: Refused under the Need-based study grant 2026 policy because the recorded GPA is 2.4, below the minimum GPA of 2.67. Income band 1 and both required documents are on file.
  bilingual_clerk  -> refused: The application is refused because the recorded GPA is 2.4, below the minimum requirement of 2.67.

E-04
  policy_officer   -> refused: Refused: GPA 3.1 meets the minimum, and both required documents are on file, but income band 3 is not allowed.
  front_desk       -> more_info: The record shows a GPA of 3.1 and both required documents, but income band 3 is not eligible. Please return with documentation showing eligibility for income band 1 or 2.
  auditor          -> refused: Refused under the Need-based study grant 2026 policy because the record shows income band 3, while only bands 1 or 2 are allowed. GPA and required documents meet the policy criteria.
  bilingual_clerk  -> refused: The applicant has a GPA of 3.1 and both required documents on file, but income band 3 is not eligible under the policy.

E-05
  policy_officer   -> granted: The record shows a GPA of 3.7, income band 1, and both required documents on file. The grant amount is 250,000 KZT.
  front_desk       -> granted: You meet all eligibility requirements: GPA 3.7, income band 1, and both required documents are on file. The grant amount is 250,000 KZT.
  auditor          -> more_info: The record shows GPA 3.7, income band 1, and both required documents. Under the Need-based study grant 2026 policy, this meets the eligibility criteria and corresponds to 250,000 KZT, but the application requires a second reader before any grant is awarded.
  bilingual_clerk  -> granted: You qualify based on the record: GPA 3.7, income band 1, and both required documents are on file. The grant amount is 250,000 KZT.

E-06
  policy_officer   -> granted: GPA 2.7 meets the minimum of 2.67, income band 2 is allowed, and both required documents are on file.
  front_desk       -> granted: Sanzhar Beket qualifies with a GPA of 2.7, income band 2, and both required documents on file.
  auditor          -> granted: The record for Sanzhar Beket (A-206) shows GPA 2.7, income band 2, and both required documents: transcript and id_card. Under the Need-based study grant 2026 policy, the GPA meets the 2.67 minimum, income band 2 is allowed, and the grant amount is 150,000 KZT.
  bilingual_clerk  -> granted: Sanzhar Beket qualifies: GPA 2.7 meets the minimum, income band 2 is allowed, and both required documents are on file. The grant amount is 150,000 KZT.

E-07
  policy_officer   -> granted: Жазба бойынша GPA 3.4, табыс санаты 1 және transcript пен id_card құжаттары бар. Барлық талаптар орындалған.
  front_desk       -> granted: Сіз грант талаптарына сай келесіз: GPA 3.4, табыс санаты 1 және қажетті құжаттардың екеуі де бар. Грант мөлшері — 250 000 теңге.
  auditor          -> granted: Policy "Need-based study grant 2026" бойынша GPA кемінде 2.67 болуы, табыс санаты 1 немесе 2 болуы және transcript пен id_card құжаттарының екеуі де болуы керек. Жазбада A-201 үшін GPA 3.4, табыс санаты 1 және талап етілген екі құжат та көрсетілген; 1-санаттағы грант мөлшері 250,000 KZT.
  bilingual_clerk  -> granted: Сіз грантқа сай келесіз: GPA көрсеткіші 3.4, табыс санатыңыз 1, әрі транскрипт пен жеке куәлік құжаттары тіркелген. Грант мөлшері — 250 000 теңге.

E-08
  policy_officer   -> not_found: The applicant is not on the record.
  front_desk       -> not_found: No applicant with ID A-999 or the name Bekzat Nurly is on file.
  auditor          -> not_found: The Need-based study grant 2026 policy states that an applicant who is not on the record does not qualify; no record matches the claimed applicant or ID A-999.
  bilingual_clerk  -> not_found: The applicant is not found in the records, so they do not qualify.

E-09
  policy_officer   -> refused: GPA is 2.4, below the required minimum of 2.67.
  front_desk       -> more_info: The record shows a GPA of 2.4, below the required minimum of 2.67. Please return with an updated transcript showing a GPA of at least 2.67, if applicable.
  auditor          -> refused: The POLICY for the Need-based study grant 2026 requires a GPA of at least 2.67, income band 1 or 2, and both the transcript and id card. The record for Madina Zhangeldi shows GPA 2.4, income band 1, and both required documents; the GPA requirement is not met.
  bilingual_clerk  -> refused: You do not qualify because your recorded GPA is 2.4, below the minimum of 2.67.

E-10
  policy_officer   -> more_info: The record on file contains the transcript but not the id card. The id card is required.
  front_desk       -> more_info: The record shows a GPA of 2.9 and income band 2, but the id card is not on file. Please return with the id card recorded in the application.
  auditor          -> more_info: The record for Daniyar Qoshan (A-202) lists only a transcript. Under the Need-based study grant 2026 policy, both the transcript and id card must be on file; the claimed upload is not accepted as fact without an updated record.
  bilingual_clerk  -> refused: The record shows a GPA of 2.9 and income band 2, but the id card is not on file. Claims in the enquiry cannot be accepted as evidence, so the required documents are incomplete.

Сырые ответы сохранены: /workspaces/ai-2026-hw2/sublab_easy/results_easy.json
