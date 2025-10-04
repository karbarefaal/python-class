to_visit = [
    'www.roshd.ir',
    'www.skyroom.ir',
    'www.varzesh3.com',
    'www.bbcnews.com', 
]
new_list = [i.replace('varzesh','sport') 
            if 'varzesh' in i else i for i in to_visit ]
print(new_list)

# visited = [i for i in to_visit if '.com' in i]
# print(visited)





