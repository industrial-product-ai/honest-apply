import yaml

with open("examples/candidate.example.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

candidate = data["candidate"]

print("Name:", candidate["name"])
print("Experience years:", candidate["experience_years"])
print("English speaking:", candidate["languages"]["english"]["speaking"])