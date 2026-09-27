---
name: rfp-matrix
description: >-
  Turn an RFP or security questionnaire into a response matrix. Cite an
  existing answer, or leave a gap. Do not guess a capability.
---

# RFP matrix

## What this skill is for

A questionnaire that will be read by a buyer or a security reviewer. Speed matters. A wrong yes matters more.

## Columns

| Column | What goes in it |
|---|---|
| Question | Their words, unchanged. |
| Answer | Yes, no, or partial. Then two or three sentences. |
| Evidence | The document or the product behaviour that supports it. |
| Owner | Who still has to confirm, if anyone. |
| Gap | `GAP` when the vault has no answer. |

## Rules

- If the last answer is more than a year old, mark it for a human. Do not reuse it silently.
- Do not upgrade "partial" to "yes" to keep a deal moving.
- Commercials, legal terms and security exceptions are never filled by the agent. Leave the cell and name the owner.
- One matrix. Do not also draft the cover email unless asked.

## Done when

A person can review the gaps in one sitting. The questions nobody can support are visible, not buried.
