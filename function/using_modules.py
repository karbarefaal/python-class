import hashlib
ans = hashlib.sha256('hi'.encode())
print(ans.hexdigest())

#====================================

from hashlib import sha256

ans = sha256('hi'.encode())
print(ans.hexdigest())

#====================================

import hashlib as hl

ans = hl.sha256('hi'.encode())
print(ans.hexdigest())

#=====================================

from functions import my_func

print(my_func(80))