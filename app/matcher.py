LANGUAGE_LEVELS = {
    "beginner": 1,
    "intermediate": 2,
    "business": 3,
    "fluent": 4,
    "native": 5,
}


def evaluate_match(candidate, job, preferences):
    """Evaluate a candidate against a job without inventing qualifications."""
    experience_match = (
        candidate["experience_years"] >= job["minimum_experience_years"]
    )

    candidate_english = candidate["languages"]["english"]["speaking"]
    required_english = job["required_languages"]["english_speaking"]
    english_match = (
        LANGUAGE_LEVELS[candidate_english] >= LANGUAGE_LEVELS[required_english]
    )

    claims_match = all(
        claim in candidate["verified_claims"] for claim in job["required_claims"]
    )
    work_mode_match = job["work_mode"] in preferences["work_modes"]
    role_allowed = job["role_category"] not in preferences["excluded_roles"]

    checks = {
        "experience_match": experience_match,
        "english_match": english_match,
        "claims_match": claims_match,
        "work_mode_match": work_mode_match,
        "role_allowed": role_allowed,
    }

    reason_by_check = {
        "experience_match": "Not enough years of experience",
        "english_match": "English speaking level is below the requirement",
        "claims_match": "Required experience is not verified",
        "work_mode_match": "Work mode is outside the candidate's preferences",
        "role_allowed": "Role category is excluded by the candidate",
    }

    failed_reasons = [
        reason_by_check[name] for name, passed in checks.items() if not passed
    ]

    return {
        **checks,
        "overall_match": all(checks.values()),
        "failed_reasons": failed_reasons,
    }
