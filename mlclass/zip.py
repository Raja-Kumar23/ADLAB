import zipfile

files_to_zip = [
    "kmeans1.py",
    "kmeans2.py",
    "input.png",
    "output1.png",
    "output2.png"
]

with zipfile.ZipFile("submission.zip", "w") as zipf:
    for file in files_to_zip:
        zipf.write(file)

print("submission.zip created successfully!")
