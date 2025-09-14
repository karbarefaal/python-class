try:
    # کدی که احتمال خطا دارد
    x = int("hello")  # اینجا خطا رخ میده
except:
    # کدی که در صورت بروز خطا اجرا میشه
    print("خطایی رخ داد!")

#=================================================================

try:
    num = int(input("یک عدد وارد کن: "))
    print(10 / num)
except ValueError:
    print("ورودی باید عدد باشد!")
except ZeroDivisionError:
    print("تقسیم بر صفر مجاز نیست!")

#=================================================================

try:
    f = open("data.txt", "r", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("فایل پیدا نشد!")
finally:
    print("برنامه به پایان رسید.")

#=================================================================

try:
    x = int(input("یک عدد وارد کن: "))
except ValueError:
    print("ورودی معتبر نیست!")
else:
    print("عدد معتبر است:", x)

#=================================================================

def set_age(age):
    if age < 0:
        raise ValueError("سن نمی‌تواند منفی باشد!")
    print("سن ذخیره شد:", age)

set_age(-5)

#==================================================================

# try:
#     print(2 / 0) #ZeroDivisionError
# except ZeroDivisionError:
#     print("ZeroDivisionError is ok for me")
# my_list = [10,20,30,40,50]
# try:
#     print(my_list[5]) #IndexError
# except IndexError: 
#     print("IndexError is ok for me")