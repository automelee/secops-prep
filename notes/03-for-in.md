## 6/14/2026 노트

for-in 하고 딕셔너리 만드는 법 완료


<details>
<summary>위는 요약이고 디텓은 여기</summary>

좀 이해가 안가긴 하는데 
for-in 스테이트먼트를 쓴느 법을 배웠고
하드코딩을 줄이고 다 배리아블 밸류를 만들면 코딩할때 덜 적는 법을 배웠고 딕셔너리를 만드는게 

얼추

딕셔너리이름 = {
    "아이템이름1": "아이탬밸류1",
    "아이템이름2": "아이템밸류2",
    "아이템이름3": "아이탬벨류3"
}

이런식으로 쓰고 딕셔너리 여러게 한번에 기록해놓고 for-in 쓴느게 가능해 보이지만 아래 코드에서

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

파트를 연속으로 for sevname, sevlevel in SEVERITY.items():
에서 컨디션 if log_count in forwarders.item() == 0
sevlevel = CRITICAL

같은 코딩이 가능할까? 햇갈리네 ㅅㅄㅂ



</details>

