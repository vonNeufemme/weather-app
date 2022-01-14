# <span id='top'>🌤️Wheather App</span>
 
날씨 앱 데모  

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/weather_app_demo.gif" />

<br>

## 개발 환경

  - 언어: 🐍파이썬
  - API: [Airnow](#airnow)
  - 모듈: `requests`, `tkinter`, `Image`, `json`
  - 기타 모듈: `os`, `re`, `time`,

<br>

## 특징

### 시작 화면

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/01%20start.png" width=550 />

  - 집코드와 반경 거리를 입력해 원하는 지역의 대기질 정보를 확인할 수 있습니다. 

<br>

### 대기질 정보 검색

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/02%20test1.png" width=550 />
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/03%20test2.png" width=550 />

  - 자료 제공 API에서 대기질을 총 6단계(좋음, 보통, 민감군에게 안 좋음, 안 좋음, 나쁨, 위험함)로 구분합니다. 
  - 날짜, 도시, 대기질, 분류, 위경도 등 5가지의 정보를 실시간으로 확인할 수 있습니다.
  - 대기질에 따른 6단계 분류에 따라 색깔도 같이 변화합니다(AirNow의 색깔 코드를 따름).
 
<br>

### 안내/경고창 기능 시험
 
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/04%20teaser1.png" width=550 />
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/04%20teaser2.png" width=550 />

  - 개발자의 조크
  - 안내창/경고창 시험용으로 만들었습니다.
  - 미국 전지역을 뒤져봐도 거의 대부분이 청정지역으로 분류 나쁨(Hazardous) 지역 창을 시험해 볼 수가 없어서 따로 구성한 화면입니다. 
  - 비밀 코드 `00000`을 입력하면 API로 json 자료를 받아오는 것이 아니라 임의 입력된 자료를 화면에 띄웁니다. 
  - 대기질이 위험(Hazardous)일 때는 최대한 빨리 안전한 지역으로 피신하세요.
  - 달리면 호흡기🫁에 나쁘니🤢 교통수단🚗으로 이동하세요! 

<br>

### 참고

[[⬆️위로 가기]](#top)

<span id="airnow">Airnow</span>
미국 환경보호청(EPA), 나사(NASA) 등의 기관의 협력으로 설립한 데이터센터로 미국 전역의 날씨 정보를 API로 제공 
https://docs.airnowapi.org/CurrentObservationsByZip/query
