import requests
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timedelta

# 도시명과 좌표 매핑 딕셔너리 
city_to_coords = {
    '서울': (60, 127),
    '부산': (98, 76),
    '대구': (89, 90),
    '인천': (55, 124),
    '광주': (58, 74),
    '대전': (67, 100),
    '울산': (102, 84),
    '세종': (66, 103),
    # 필요한 다른 도시 추가
}
def get_weather(request):
    api_key = settings.DATA_GO_KR_API_KEY
    city = request.GET.get('city', '서울')  # 기본값으로 서울
    base_date = datetime.now().strftime('%Y%m%d')  # API에서 요구하는 날짜 형식
    base_time = '0600'  # API에서 요구하는 기본 시간
    
    coords = city_to_coords.get(city, (60, 127))  # 기본값으로 서울의 좌표
    nx, ny = coords

    # API URL 구성
    url = (
        'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
        f'?serviceKey={api_key}&numOfRows=10&pageNo=1&dataType=JSON'
        f'&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}'
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['response']['header']['resultCode'] == '00':
        items = data['response']['body']['items']['item']
        weather_data = {
            'city': city,
            'forecasts': items
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Could not retrieve weather data'}, status=response.status_code)
