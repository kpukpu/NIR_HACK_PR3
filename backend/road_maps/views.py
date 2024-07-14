import requests
import io
from PIL import Image, UnidentifiedImageError
import matplotlib.pyplot as plt

def get_coordinates(address):
    # 네이버 지도 API 설정
    client_id = 'f15jusqlfi'
    client_secret = '6hyWRpCVyocu4NUA2ncgP71XPU05zxwr0b5AOJEX'
    # 네이버 지도 API Geocoding을 이용하여 주소로부터 x, y 좌표 확인
    geocode_url = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}'
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    response = requests.get(geocode_url, headers=headers)
    data = response.json()
    if 'addresses' in data and len(data['addresses']) > 0:
        x = data['addresses'][0]['x']
        y = data['addresses'][0]['y']
        return x, y
    else:
        return None, None

def get_map_image(x, y):
    # 네이버 지도 API 설정
    client_id = '6w25fiw380'
    client_secret = 'ikbT0AjnEVVqC7FgvEFkk2GDrvwyj0K12IamIo2M'
    # 좌표 및 API 요청 설정
    endpoint = 'https://naveropenapi.apigw.ntruss.com/map-static/v2/raster'
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    params = {
        'center': f'{x},{y}',
        'level': 12,
        'w': 500,
        'h': 300,
        'maptype': "traffic",
        'format': "png",
        'scale': 2,
        'markers': f"type:d|size:mid|pos:{x} {y}|color:red",
        'lang': "ko",
        'public_transit': True,
        'dataversion': "",
    }
    # API 요청 보내기
    response = requests.get(endpoint, headers=headers, params=params)
    
    # 응답 상태 코드 확인
    if response.status_code == 200:
        try:
            image_data = io.BytesIO(response.content)
            image = Image.open(image_data)
            # 이미지 화면에 표시하기
            plt.imshow(image)
            plt.axis('off')
            plt.show()
        except UnidentifiedImageError:
            print("응답 데이터가 이미지가 아닙니다.")
    else:
        print("지도 이미지를 가져오지 못했습니다. 상태 코드:", response.status_code)
        print(response.text)

def geocode(request):
    address = input("주소를 입력하세요 (‘QUIT’를 입력하면 종료): ")
    x, y = get_coordinates(address)
    if x is not None and y is not None:
        get_map_image(x, y)
    else:
        print("주소를 확인할 수 없습니다.")
