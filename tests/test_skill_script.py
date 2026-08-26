import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "evaluate_json.py"


class SkillScriptTests(unittest.TestCase):
    def test_json_entrypoint_returns_match_result(self):
        candidate = {
            "candidate": {
                "name": "Example Candidate",
                "experience_years": 5,
                "languages": {"english": {"speaking": "intermediate"}},
                "verified_claims": ["Built a B2B content program"],
                "restricted_claims": [],
            }
        }
        job = {
            "job": {
                "title": "B2B Content Specialist",
                "role_category": "content_marketing",
                "work_mode": "remote",
                "minimum_experience_years": 3,
                "required_languages": {"english_speaking": "intermediate"},
                "required_claims": ["Built a B2B content program"],
            }
        }
        preferences = {
            "preferences": {
                "excluded_roles": [],
                "work_modes": ["remote", "local_onsite"],
            }
        }

        with tempfile.TemporaryDirectory() as directory:
            paths = {}
            for name, data in (
                ("candidate", candidate),
                ("job", job),
                ("preferences", preferences),
            ):
                path = Path(directory) / f"{name}.json"
                path.write_text(json.dumps(data), encoding="utf-8")
                paths[name] = path

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--candidate",
                    str(paths["candidate"]),
                    "--job",
                    str(paths["job"]),
                    "--preferences",
                    str(paths["preferences"]),
                ],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )

        result = json.loads(completed.stdout)
        self.assertTrue(result["overall_match"])
        self.assertEqual(result["failed_reasons"], [])


if __name__ == "__main__":
    unittest.main()
