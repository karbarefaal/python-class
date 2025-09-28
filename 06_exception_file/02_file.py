#========================third session========================================

# x => just create,r => read ,w => overwrite ,a => append  /   t= text,b=binary

# open("./myFolder/mehdi.txt", "x")

# with open("./myFolder/mehdi.txt") as f:     # r
#     print(f.read())

# with open("./myFolder/mehdi.txt", "w") as f:
#     f.write("salam man mehdi ghasemi hastam.")

# with open("./myFolder/mehdi.txt", "a") as f:
#     f.write("\nsalam man mehdi ghasemi hastam.")

import os
# os.mkdir("./mehdiFolder/hi")        # mkdir
# os.rmdir("./mehdiFolder/hi")
# os.rename("mehdiFolder/helloFolder", "mehdiFolder/hi")


if os.path.exists("mehdiFolder/hi"):
    os.remove("myFolder\\kasraFile.txt")
else:
    print("nashod")

#==============================second session============================


# a append      w write         r read      x create
# t text        b binary
# f = open("D:\\ourFile.txt","a") 
# f.write("Salam Kasra jan. khubi?")
# f.close()

#========================== write file =====================

with open("myFolder\\myFile.txt", "a") as f:
    f.write("Hi there. Welcome to python class 200.\n")

#=============================read file=================================

with open("myFolder\\myFile.txt", "r") as f:
    print(f.read())

#=========================to create a file= via x mode==================

try:
    if not os.path.exists("data.txt"):
        open("data.txt", "x")
except FileNotFoundError:
    print("Please create a file as data.txt")

#================================os mudule===============================

import os

# rename remove using os module
if os.path.exists("myFolder\\myFile.txt"):
    os.remove("myFolder\\kasraFile.txt")

# os.rename()

#  create and remove folder
# os.mkdir("toDelete")
# os.rmdir("toDelete")
#==============================first session============================

f = open("myName.txt","w")
f.write("Salam man yechizi neveshtam")
f.close()

f = open("myName.txt")
print(f.read())
f.close()

#=======================================================================

# "r" → فقط خواندن

# "w" → فقط نوشتن (اگر فایل وجود داشته باشه پاک میشه)

# "a" → افزودن به انتهای فایل

# "b" → حالت باینری

# "t" → حالت متنی (پیش‌فرض)

# "x" → ایجاد فایل جدید (اگر وجود داشته باشه خطا میده)

f = open("test.txt", "w")  # ایجاد و باز کردن برای نوشتن
f.write("سلام دنیا\n")
f.close()


#====================================================================

# نوشتن
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("خط اول\nخط دوم")

# خواندن
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

#====================================================================

# read() → کل فایل رو می‌خونه

# readline() → فقط یک خط می‌خونه

# readlines() → کل خط‌ها رو به صورت لیست برمی‌گردونه

# seek(pos) → تغییر مکان در فایل

# tell() → موقعیت فعلی مکان‌نما (cursor)

with open("data.txt", "r", encoding="utf-8") as f:
    print(f.readline())  # خط اول
    print(f.tell())      # مکان‌نما بعد از خط اول
    f.seek(0)            # برگردوندن مکان‌نما به اول
    print(f.readline())  # دوباره خط اول

#=====================================================================

