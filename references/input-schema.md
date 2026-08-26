# HonestApply input schema

Read this reference when converting candidate, job, and preference source material
into structured input for `scripts/evaluate_json.py`.

## Candidate JSON

```json
{
  "candidate": {
    "name": "Example Candidate",
    "experience_years": 5,
    "languages": {"english": {"speaking": "intermediate"}},
    "verified_claims": ["Built a B2B content program"],
    "restricted_claims": ["Fluent spoken English"]
  }
}
```

Allowed English levels, from lowest to highest:

```text
beginner, intermediate, business, fluent, native
```

Use only explicitly supported facts in `verified_claims`. Put uncertain,
contradictory, exaggerated, sensitive, or prohibited statements in
`restricted_claims`. A claim must not appear in both lists.

## Job JSON

```json
{
  "job": {
    "title": "B2B Content Specialist",
    "role_category": "content_marketing",
    "work_mode": "remote",
    "minimum_experience_years": 3,
    "required_languages": {"english_speaking": "intermediate"},
    "required_claims": ["Built a B2B content program"]
  }
}
```

`required_claims` must contain concrete claims that can be checked against the
candidate ledger. Do not turn generic duties or nice-to-have language into hard
requirements unless the source presents them that way.

## Preferences JSON

```json
{
  "preferences": {
    "excluded_roles": [],
    "work_modes": ["remote", "local_onsite"]
  }
}
```

Do not infer personal preferences from a resume. Use preferences stated by the
user in the current request or previously confirmed context.

## Result JSON

The script returns booleans for each check, an `overall_match` boolean, and a
`failed_reasons` list. Treat this as a baseline. A conversational recommendation
may use `Apply after clarification` when a failure reflects missing evidence
rather than a confirmed mismatch, but it must not turn a failed hard check into
an unqualified `Apply`.
