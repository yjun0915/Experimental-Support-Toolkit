import requests # 웹 요청에 필수적인 라이브러리
from config import auth # 가상의 설정 파일에서 URI를 가져옵니다.

# 1. URI 가져오기
# PowerShell의 변수 할당 방식 대신 Python의 직접 접근 방식을 사용합니다.
uri = auth.uri
print(f"INFO: 대상 URI: {uri}")

# 2. Body 데이터 (Python Dictionary)
# PowerShell의 해시 테이블(@{...}) 대신 Python의 딕셔너리를 사용합니다.
body_dict = {
    "botName": "MyBot",
    "botIconImage": "https://static.dooray.com/static_images/dooray-bot.png",
    "text": "Dooray! (Python 딕셔너리를 JSON으로 변환하여 전송)"
}

# 3. 요청 전송
try:
    # requests는 json=body_dict 인수를 받으면
    # 딕셔너리를 JSON 문자열로 자동 변환하고 Content-Type: application/json 헤더를 설정합니다.
    response = requests.post(
        uri,
        json=body_dict
    )

    # 응답 확인
    if response.status_code == 200:
        print("SUCCESS: 메시지가 성공적으로 전송되었습니다.")
    else:
        print(f"ERROR: 요청 실패. HTTP 상태 코드: {response.status_code}")
        print(f"응답 본문: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"FATAL ERROR: 요청 중 오류 발생 - {e}")