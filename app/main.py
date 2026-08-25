import yaml

with open("examples/candidate.example.yaml", "r", encoding="utf-8") as file:
    candidate_data = yaml.safe_load(file)

with open("examples/job.example.yaml", "r", encoding="utf-8") as file:
    job_data = yaml.safe_load(file)

candidate = candidate_data["candidate"]
job = job_data["job"]

print("Candidate:", candidate["name"])
print("Experience years:", candidate["experience_years"])
print("Job title:", job["title"])
print("Required experience years:", job["minimum_experience_years"])

experience_match = (
    candidate["experience_years"] >= job["minimum_experience_years"]
)

print("Experience match:", experience_match)

language_levels = {
    "beginner": 1,
    "intermediate": 2,
    "business": 3,
    "fluent": 4,
    "native": 5,
}

candidate_english = candidate["languages"]["english"]["speaking"]
required_english = job["required_languages"]["english_speaking"]

english_match = (
    language_levels[candidate_english] >= language_levels[required_english]
)

print("English speaking match:", english_match)

required_claims = job["required_claims"]
verified_claims = candidate["verified_claims"]

claims_match = all(
    claim in verified_claims for claim in required_claims
)

overall_match = experience_match and english_match and claims_match

print("Verified claims match:", claims_match)

if overall_match:
    print("Recommendation: Apply")
else:
    print("Recommendation: Do not apply yet")