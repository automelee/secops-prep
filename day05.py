#IN 펑션 쓸꺼임
# 포워더 이름 그리고 , 그리고 로그들 카운트

SEVERITY = {
    "CRITICAL": "[CRITICAL]",
    "WARNING": "[WARNING]",
    "OK": "[OK]"
}
forwarders = {
    "fwd-dallas-01": 0,
    "fwd-dallas-02": 5432,
    "fwd-houston-01": 98,
    "fwd-houston-02": 15000,
    "fwd-chicago-01": 0
}

threshold = 100

for name, log_count in forwarders.items():
    if log_count == 0:
        level = "CRITICAL"
    elif log_count < threshold:
        level = "WARNING"
    else:
        level = "OK"
    print(f"{SEVERITY[level]} {name}: {log_count} logs")