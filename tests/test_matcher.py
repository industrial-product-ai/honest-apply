import copy
import unittest

from app.matcher import evaluate_match


CANDIDATE = {
    "experience_years": 5,
    "languages": {"english": {"speaking": "intermediate"}},
    "verified_claims": ["Built a B2B content program"],
}

JOB = {
    "role_category": "content_marketing",
    "work_mode": "remote",
    "minimum_experience_years": 3,
    "required_languages": {"english_speaking": "intermediate"},
    "required_claims": ["Built a B2B content program"],
}

PREFERENCES = {
    "excluded_roles": [],
    "work_modes": ["remote", "local_onsite"],
}


class MatchEvaluationTests(unittest.TestCase):
    def test_matching_candidate_is_recommended(self):
        result = evaluate_match(CANDIDATE, JOB, PREFERENCES)

        self.assertTrue(result["overall_match"])
        self.assertEqual(result["failed_reasons"], [])

    def test_insufficient_experience_is_rejected(self):
        job = copy.deepcopy(JOB)
        job["minimum_experience_years"] = 8

        result = evaluate_match(CANDIDATE, job, PREFERENCES)

        self.assertFalse(result["overall_match"])
        self.assertIn("Not enough years of experience", result["failed_reasons"])

    def test_excluded_role_is_rejected(self):
        preferences = copy.deepcopy(PREFERENCES)
        preferences["excluded_roles"] = ["content_marketing"]

        result = evaluate_match(CANDIDATE, JOB, preferences)

        self.assertFalse(result["overall_match"])
        self.assertIn(
            "Role category is excluded by the candidate",
            result["failed_reasons"],
        )


if __name__ == "__main__":
    unittest.main()
