import yaml

from matcher import evaluate_match


def load_yaml(path):
    """Load structured data from a YAML file."""
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


candidate = load_yaml("examples/candidate.example.yaml")["candidate"]
job = load_yaml("examples/job.example.yaml")["job"]
preferences = load_yaml("examples/preferences.example.yaml")["preferences"]

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
