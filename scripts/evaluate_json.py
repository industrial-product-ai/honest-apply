import argparse
import json
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT))

from app.matcher import evaluate_match  # noqa: E402
from app.validation import (  # noqa: E402
    InputValidationError,
    validate_candidate,
    validate_job,
    validate_preferences,
)


def load_section(path, section):
    """Load one required top-level section from a JSON file."""
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise InputValidationError(f"File not found: {path}") from error
    except json.JSONDecodeError as error:
        raise InputValidationError(f"Invalid JSON in {path}: {error}") from error

    if not isinstance(data, dict) or section not in data:
        raise InputValidationError(
            f"{path} must contain a top-level '{section}' section"
        )
    return data[section]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evaluate private HonestApply JSON inputs."
    )
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--job", required=True)
    parser.add_argument("--preferences", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        candidate = load_section(args.candidate, "candidate")
        job = load_section(args.job, "job")
        preferences = load_section(args.preferences, "preferences")

        validate_candidate(candidate)
        validate_job(job)
        validate_preferences(preferences)
        result = evaluate_match(candidate, job, preferences)
    except InputValidationError as error:
        raise SystemExit(f"Input error: {error}") from error

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
