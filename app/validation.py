VALID_LANGUAGE_LEVELS = {
    "beginner",
    "intermediate",
    "business",
    "fluent",
    "native",
}


class InputValidationError(ValueError):
    """Raised when an input file is readable but its data is invalid."""


def require(mapping, key, context):
    """Return a required value or raise a readable validation error."""
    if not isinstance(mapping, dict):
        raise InputValidationError(f"{context} must be a YAML mapping")
    if key not in mapping:
        raise InputValidationError(f"{context} is missing required field: {key}")
    return mapping[key]


def validate_candidate(candidate):
    """Validate fields required by the matching engine."""
    require(candidate, "name", "candidate")
    experience_years = require(candidate, "experience_years", "candidate")
    languages = require(candidate, "languages", "candidate")
    english = require(languages, "english", "candidate.languages")
    speaking = require(english, "speaking", "candidate.languages.english")
    verified_claims = require(candidate, "verified_claims", "candidate")
    restricted_claims = require(candidate, "restricted_claims", "candidate")

    if not isinstance(experience_years, int) or experience_years < 0:
        raise InputValidationError(
            "candidate.experience_years must be a non-negative whole number"
        )
    if speaking not in VALID_LANGUAGE_LEVELS:
        allowed = ", ".join(sorted(VALID_LANGUAGE_LEVELS))
        raise InputValidationError(
            f"candidate English speaking level must be one of: {allowed}"
        )
    if not isinstance(verified_claims, list):
        raise InputValidationError("candidate.verified_claims must be a list")
    if not isinstance(restricted_claims, list):
        raise InputValidationError("candidate.restricted_claims must be a list")
    overlapping_claims = set(verified_claims) & set(restricted_claims)
    if overlapping_claims:
        raise InputValidationError(
            "the same claim cannot be both verified and restricted"
        )


def validate_job(job):
    """Validate job fields required by the matching engine."""
    require(job, "title", "job")
    require(job, "role_category", "job")
    require(job, "work_mode", "job")
    minimum_years = require(job, "minimum_experience_years", "job")
    required_languages = require(job, "required_languages", "job")
    required_level = require(
        required_languages,
        "english_speaking",
        "job.required_languages",
    )
    required_claims = require(job, "required_claims", "job")

    if not isinstance(minimum_years, int) or minimum_years < 0:
        raise InputValidationError(
            "job.minimum_experience_years must be a non-negative whole number"
        )
    if required_level not in VALID_LANGUAGE_LEVELS:
        allowed = ", ".join(sorted(VALID_LANGUAGE_LEVELS))
        raise InputValidationError(
            f"job English speaking level must be one of: {allowed}"
        )
    if not isinstance(required_claims, list):
        raise InputValidationError("job.required_claims must be a list")


def validate_preferences(preferences):
    """Validate preference fields required by the matching engine."""
    excluded_roles = require(preferences, "excluded_roles", "preferences")
    work_modes = require(preferences, "work_modes", "preferences")

    if not isinstance(excluded_roles, list):
        raise InputValidationError("preferences.excluded_roles must be a list")
    if not isinstance(work_modes, list):
        raise InputValidationError("preferences.work_modes must be a list")
