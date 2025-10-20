#=================================================

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

#======================================================

# import csv

# name,age,city
# Alice,30,New York
# Bob,24,London

# def read_csv_example(filename='data.csv'):
#     print('----Reading CSV------')
#     with open(filename, "r", newline='', encoding="utf-8") as file:
#         reader = csv.reader(file)
    
#         # Read the header row separately
#         header = next(reader)
#         print(f"Header: {header}")

#         # Read the rest of the rows
#         for row in reader:
#             print(f"Row: {row}")

# read_csv_example()


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
import xml.etree.ElementTree as ET

# ایجاد XML
root = ET.Element("students")
student = ET.SubElement(root, "student")
name = ET.SubElement(student, "name")
name.text = "Ali"
name.attrib = {"id": "123"}
score = ET.SubElement(student,"score")
score.text = "20"
score.attrib = {"id": "A"}

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
    "grades": {"Riazi": 20, "Shimi": 18}
}

# ذخیره در فایل JSON
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# خواندن از فایل JSON
with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
