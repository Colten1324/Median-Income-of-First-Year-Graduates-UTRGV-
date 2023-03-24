# Open the input file and read its contents
with open("input.txt", "r") as f:
    lines = f.readlines()

keywords = {
    "engineering": "Engineering",
    "business": "Business",
    "art": "Arts",
    "music": "Arts",
    "science": "Science",
    "medical": "Medical",
    "law": "Law",
}

college_categories = {}

for line in lines:
    category = "Unknown"
    for keyword, category_name in keywords.items():
        if keyword in line.lower():
            category = category_name
            break
    college_categories.setdefault(category, []).append(line.strip())

with open("output.txt", "w") as f:
    for category, colleges in college_categories.items():
        f.write(category + ":\n")
        for college in colleges:
            f.write("  " + college + "\n")
        f.write("\n")
