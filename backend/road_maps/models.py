import requests
from django.http import JsonResponse
from django.conf import settings

def geocode(request):
    query = "중구 필동로1길 30"
    coordinate = "126.9986, 37.5585"
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": 'f15jusqlfi',
        "X-NCP-APIGW-API-KEY": '6hyWRpCVyocu4NUA2ncgP71XPU05zxwr0b5AOJEX',
    }
    
    params = {
        "query": query,
        "coordinate": coordinate,
    }
    
    response = requests.get("https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode", headers=headers, params=params)
    response_data = response.json()
    if response.status_code == 200:
        if response_data['status'] == 'OK':
            address_info = response_data['addresses'][0]
            print("Address:", address_info['roadAddress'])
            print("Latitude:", address_info['y'])
            print("Longitude:", address_info['x'])
        else:
            print("Error:", response_data['status'], response_data['message'])
    else:
        print("Error Code:", response.status_code)
    return JsonResponse(response_data)