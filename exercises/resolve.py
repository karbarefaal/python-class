# parse func  input  string url   dict output
# deparse func input dict  out string url

# input set adad abd 1 adad


def my_find(myset: set, myNum: int):
    for i in myset:
        if myNum == i:
            return f"we have {myNum}"
    else:
        return f"we do not have {myNum}"

print(my_find((1,2,3,4), 5))
            
        
        
        