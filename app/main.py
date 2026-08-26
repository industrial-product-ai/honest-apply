import argparse

import yaml

from matcher import evaluate_match


def load_yaml(path):
    """Load structured data from a YAML file."""
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def parse_args():
    """Read optional file paths from the command line."""
    parser = argparse.ArgumentParser(
        description="Evaluate a truthful candidate profile against a job."
    )
    parser.add_argument(
        "--candidate",
        default="examples/candidate.example.yaml",
        help="Path to the candidate YAML file",
    )
    parser.add_argument(
        "--job",
        default="examples/job.example.yaml",
        help="Path to the job YAML file",
    )
    parser.add_argument(
        "--preferences",
        default="examples/preferences.example.yaml",
        help="Path to the preferences YAML file",
    )
    return parser.parse_args()


def main():
    """Load inputs, evaluate the match, and print a readable report."""
    args = parse_args()
    candidate = load_yaml(args.candidate)["candidate"]
    job = load_yaml(args.job)["job"]
    preferences = load_yaml(args.preferences)["preferences"]

    result = evaluate_match(candidate, job, preferences)

    print("Candidate:", candidate["name"])
    print("Experience years:", candidate["experience_years"])
    print("Job title:", job["title"])
    print("Required experience years:", job["minimum_experience_years"])
    print("Experience match:", result["experience_match"])
    print("English speaking match:", result["english_match"])
    print("Verified claims match:", result["claims_match"])
    print("Work mode match:", result["work_mode_match"])
    print("Role allowed:", result["role_allowed"])

    if result["overall_match"]:
        print("Recommendation: Apply")
    else:
        print("Recommendation: Do not apply yet")
        print("Reasons:")
        for reason in result["failed_reasons"]:
            print("-", reason)


if __name__ == "__main__":
    main()
