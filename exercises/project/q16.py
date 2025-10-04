log_data = """192.168.1.1 - [10/Jul/2025:22:14:15] "GET /api/user HTTP/1.1" 200
172.16.0.5 - [10/Jul/2025:22:14:16] "POST /api/login HTTP/1.1" 401
192.168.1.1 - [10/Jul/2025:22:14:18] "GET /api/products HTTP/1.1" 200
212.5.25.10 - [10/Jul/2025:22:14:20] "GET /static/style.css HTTP/1.1" 304
192.168.1.1 - [10/Jul/2025:22:14:22] "DELETE /api/user/1 HTTP/1.1" 500
"""

def log_reader(log):

    lists = log.split("\n")
    ip = []
    date = []
    req = []
    code = []
    k = 0
    for i in lists:
        if "." not in i:
            lists.remove(i)
            continue
    for i in lists:
        endOfIP = i.find("-") - 1
        ip.append(i[:endOfIP])
        #===========ip done ===================
        startDate = i.find("[") + 1
        endDate = i.find("]")
        date.append(i[startDate:endDate])
        #============date done================
        startReq = i.find("\"") + 1
        endReq = i.find("\"",startReq)
        req.append(i[startReq:endReq])
        #===========request done ===================
        startCode = endReq + 2
        endCode = startCode + 3
        code.append(i[startCode:endCode])
        #============code done=====================
        k += 1
    # total_reqNum = 0
    # fail_reqNum = 0
    # successful_reqNum = 0
    log_dict = {}
    for i in ip:
        log_dict[i] ={
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0
        }
    c = 0
    ip_code = zip(ip, code)

    for i in ip_code:
        if i[1] == "200" or "201" or "300" or "301" or "304":
            print(i[1])
            log_dict[i[0]]["successful_requests"] += 1
        elif i[1] == "401" or "404" or "403" or "500":
            log_dict[i[0]]["failed_requests"] += 1
        log_dict[i[0]]["total_requests"] += 1
    for i in log_dict.items():
        print(i)

log_reader(log_data)