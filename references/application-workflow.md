# HonestApply application workflow

Read this reference only when the user asks to prepare, fill, send, or submit an
application, or asks the agent to search for roles and apply.

## Supported destinations

Route by the actual application destination rather than the site where the job
was discovered:

- LinkedIn and LinkedIn Easy Apply
- Greenhouse
- Lever
- Ashby
- Workday
- Employer career sites and other ATS forms
- Recruitment email

Use any other destination on a best-effort basis when browser access is available.
If login, site restrictions, missing tools, or an unsupported form block progress,
prepare the application packet and hand off the smallest necessary step to the
user. Do not bypass access controls or website safety barriers.

## Discovery and screening

1. Search only within the user's confirmed constraints. Re-check unstable details
   such as whether the posting is open, location, remote status, compensation,
   work authorization, and application destination.
2. Deduplicate the same role across aggregators and employer sites. Prefer the
   employer's official application destination when available.
3. Run the deterministic matcher before preparing an application. Do not apply
   when a confirmed hard requirement fails unless the user explicitly decides to
   proceed after seeing the exact mismatch.
4. Do not treat preferred qualifications as mandatory unless the posting does.

For a platform-scoped campaign, maintain a private working table with:

```text
Platform | Company | Role | Location | Work mode | Fit | Status | Source URL
```

Use these status values consistently: `shortlisted`, `preparing`,
`awaiting confirmation`, `submitted`, `skipped`, `blocked`, and `duplicate`.
State how many result pages or listings were actually reviewed. Do not describe a
partial sample as the whole platform.

## Truthful tailoring

1. Build every resume bullet, cover-letter statement, and form answer from
   `verified_claims` or other explicit source facts.
2. Tailor emphasis and wording, not facts. Do not invent employers, titles,
   dates, metrics, ownership, tools, language levels, degrees, certificates,
   salary history, work authorization, or location.
3. Keep restricted claims out of generated materials. If the posting asks for a
   restricted or unknown fact, ask the user or record the mismatch.
4. Preserve a short change summary so the user can see what was emphasized,
   removed, or left unverified.
5. Never overwrite the candidate's master resume. Create a separate file for each
   application, preferably named `Candidate_Company_Role.pdf` or `.docx`, using
   available document tools. Verify the generated file before upload. If document
   generation is unavailable, provide the tailored text and clearly say that no
   application-ready file was created.
6. Choose the resume language from the user's instruction first. Otherwise match
   the language of the posting and application form. Use Chinese for a
   Chinese-language domestic recruitment flow, English for an English-language
   flow, and create separate bilingual versions only when both are useful or
   requested. Preserve official company, product, certificate, and tool names
   when translating.

## Form filling

1. Open the verified application destination in an available browser. Use an
   existing signed-in session; never ask the user to send a password, cookie,
   verification code, or browser profile.
2. Fill fields supported by confirmed candidate data. Pause for questions whose
   answers are missing, ambiguous, legally significant, or candidate-specific,
   including work authorization, sponsorship, compensation, relocation,
   demographic disclosures, background checks, and binding declarations.
3. Before uploading a resume, cover letter, portfolio, or other personal file,
   tell the user the exact file and destination and obtain the confirmation
   required for transmitting personal data.
4. Never solve or bypass a CAPTCHA. Hand that step to the user.
5. Do not accept optional marketing communications unless the user asks.

## Submission gate

Immediately before the final submit action, present a compact manifest:

```text
Company:
Role:
Application URL or email recipient:
Resume/version being sent:
Other attachments:
Material form answers or declarations:
Known mismatches or unverified items:
```

Ask for explicit confirmation to submit this specific application. Only after
confirmation, perform the final click or send action. A prior instruction to
"auto apply" does not remove this action-time confirmation gate.

Keep the confirmation brief, for example:

```text
Ready to submit: Company — Role, using Candidate_Company_Role.pdf.
Known mismatch: none. Confirm this submission?
```

## Tracking and stopping conditions

After a successful submission, record the company, role, source URL, destination,
date, resume version, status, and any follow-up date in a private local record.
Never commit this record to a public repository.

Stop and report the blocker when:

- the posting is closed, materially different, or cannot be verified;
- a mandatory answer is unknown;
- the user has not approved transmitting personal data or final submission;
- the site requires a CAPTCHA, unavailable login, or unsupported interaction;
- the application would require a false or restricted claim;
- the destination, company, or role cannot be confidently identified.
