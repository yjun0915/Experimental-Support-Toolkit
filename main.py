import requests
import json

# 1. 공공기관용 API 기본 주소
BASE_URL = "https://kist.gov-dooray.com"

# 2. 발급받은 API 토큰 (권한이 제한된 토큰)
API_TOKEN = "m1olidaukdr7:7fHvvZqyTH-1Z9i-FvBPYw"

# 3. HTTP 요청 헤더 설정
headers = {
    "Authorization": f"dooray-api {API_TOKEN}",
    "Content-Type": "application/json"
}

try:
    # 4. API 호출 (봇 자신의 정보 조회 엔드포인트)
    # '대화방 생성'이 아닌 '내 정보 조회'를 시도합니다.
    response = requests.get(
        f"{BASE_URL}/messenger/v1/bots/me",  # 'me'는 토큰의 주인(봇)을 가리킴
        headers=headers
    )

    # 응답 상태 코드 확인
    if response.status_code == 200:
        print("✅ 봇 정보 조회 성공!")
        bot_info = response.json()

        # 보기 편하도록 JSON을 정렬하여 출력
        print(json.dumps(bot_info, indent=2, ensure_ascii=False))

        # 가장 중요한 'scopes'(권한) 정보가 있는지 확인
        if 'scopes' in bot_info:
            print("\n--- ⭐️ 현재 보유한 권한 (Scopes) ---")
            print(bot_info['scopes'])
        else:
            print("\n--- 'scopes' 항목을 찾을 수 없습니다. ---")

    else:
        # 이 요청마저 401이 뜬다면 토큰 자체가 잘못된 것일 수 있습니다.
        print(f"❌ 봇 정보 조회 실패: {response.status_code}")
        print(f"오류 내용: {response.text}")

except Exception as e:
    print(f"API 호출 중 오류 발생: {e}")
