# 🌤️Wheather App
 
날씨 앱 데모  

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/weather_app_demo.gif" />

<br>

## 개발 환경

  - 언어: 🐍파이썬
  - API: [Airnow](#airnow)
  - 모듈: `requests`, `tkinter`, `Image`, `json`
  - 기타 모듈: `os`, `re`, `time`,

## 특징

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/01%20start.png" width=550 />

  - 시작 화면. 집코드와 반경 거리를 입력해 원하는 지역의 대기질 정보를 확인할 수 있습니다. 

<img src="https://github.com/vonAltmann/weather-app/blob/main/images/02%20test1.png" width=550 />
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/03%20test2.png" width=550 />

  - 자료 제공 API에서 대기질을 총 6단계(좋음, 보통, 민감군에게 안 좋음, 안 좋음, 나쁨, 위험함)로 구분합니다. 
  - 날짜, 도시, 대기질, 분류, 위경도 등 5가지의 정보를 실시간으로 확인할 수 있습니다.
  - 대기질에 따른 6단계 분류에 따라 색깔도 같이 변화합니다(AirNow의 색깔 코드를 따름).
 
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/04%20teaser1.png" width=550 />
<img src="https://github.com/vonAltmann/weather-app/blob/main/images/04%20teaser2.png" width=550 />

  - 개발자의 조크
  - 안내창/경고창 시험용으로 만들었습니다.
  - 대기질이 위험(Hazardous)일 때는 최대한 빨리 안전한 지역으로 피신하세요. 

<br>

<span id="airnow">참고: Airnow</span>
미국 환경보호청(EPA), 나사(NASA) 등의 기관의 협력으로 설립한 데이터센터로 미국 전역의 날씨 정보를 API로 제공 
https://docs.airnowapi.org/CurrentObservationsByZip/query
