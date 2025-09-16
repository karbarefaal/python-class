


# ===========================second session=================================
try:
    print(2/ 0)
except ZeroDivisionError:
    print('you can\'t')
except:
    print('hi there')
else:
    print('else')
finally:
    print('finally')

#==========================exercise===========================================

def valueChecker(age):
    if age >= 18:
        print("dige got shodi.")
    elif (age >= 0): 
        print("sen shoma kafi nemibashad.")

def negativeChecker(value):
    if value < 0:
        return True

def getNumber():
    while(True):
        age = input('lotfan sen khod ra vared konid: ')

        try:
            age = int(age)
        except ValueError:
            print('please enter a number.')
            continue
        if negativeChecker(age):
            print('please do not enter a neg num.')
        valueChecker(age)
        if(age == 1000):
            print("Done!")
            break


if __name__ == "__main__":
    getNumber()

#========================first session========================================

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