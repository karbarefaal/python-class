#=============================csv=================================

import csv

# نوشتن در فایل CSV
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["نام", "نمره"])
    writer.writerow(["علی", 18])
    writer.writerow(["سارا", 20])

# خواندن از فایل CSV
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#=========================xml======================================

import xml.etree.ElementTree as ET

# ایجاد XML
root = ET.Element("students")
student = ET.SubElement(root, "student")
ET.SubElement(student, "name").text = "Ali"
ET.SubElement(student, "score").text = "18"

tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8")

# خواندن XML
tree = ET.parse("students.xml")
root = tree.getroot()
for student in root:
    print(student.find("name").text, student.find("score").text)

#===========================json====================================

import json

data = {
    "name": "Ali",
    "age": 21,
    "grades": [18, 19, 20]
}

# ذخیره در فایل JSON
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# خواندن از فایل JSON
with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
