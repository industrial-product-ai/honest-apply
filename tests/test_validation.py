import unittest

from app.validation import InputValidationError, validate_candidate, validate_job


class InputValidationTests(unittest.TestCase):
    def test_missing_job_field_has_readable_error(self):
        job = {
            "title": "Example Role",
            "work_mode": "remote",
            "minimum_experience_years": 3,
            "required_languages": {"english_speaking": "intermediate"},
            "required_claims": [],
        }

        with self.assertRaisesRegex(InputValidationError, "role_category"):
            validate_job(job)

    def test_unknown_language_level_has_readable_error(self):
        candidate = {
            "name": "Example Candidate",
            "experience_years": 5,
            "languages": {"english": {"speaking": "very good"}},
            "verified_claims": [],
            "restricted_claims": [],
        }

        with self.assertRaisesRegex(InputValidationError, "must be one of"):
            validate_candidate(candidate)


if __name__ == "__main__":
    unittest.main()
