
# SFarm Project.

스마트 농장에 관심이 생겨서 기본적인 프로젝트를 구성해보았다.
평소에 즐겨 찾아 먹던 바질과 청상추를 주 작물로 재배할 예정이다.
농장을 구성하는 모든 과정을 업데이트 할 예정이다. 프로젝트 도중 실패하는 경우도 같이 업로드 하면서 성공적인 재배를 할때 까지 업데이트 하겠다.

---
# 개요 (Summary):
현재의 대한민국은 스마트팜이 가지는 중요성은 여러 측면에서 나타난다고 생각한다. 스마트팜은 정보기술 및 센서 기술을 활용하여 농업 생산성을 향상시키고 지속 가능성을 증진하는데 기여하고 있다. 

1. **효율적인 농업 관리:**
   - 스마트팜은 농부들이 작물, 토양, 기상 조건 등의 데이터를 실시간으로 수집하고 분석할 수 있게 해줍니다. 이를 통해 농부들은 효율적인 농업 관리를 할 수 있고, 생산성을 향상시킬 수 있습니다.

2. **자동화 및 원격 모니터링:**
   - 스마트팜은 센서, 자동화 장치 및 원격 제어 기술을 통해 농경지의 여러 작업을 자동화하고 원격에서 모니터링할 수 있습니다. 이는 인력 절감과 생산성 향상을 가져옵니다.

3. **정밀농업 및 자원 최적화:**
   - 스마트팜은 정밀농업 기술을 적용하여 농작물의 성장과 수확 예측, 비료 및 물 사용의 최적화를 가능케 합니다. 이로써 자원 소비를 줄이고 환경에 미치는 영향을 최소화할 수 있습니다.

4. **데이터 기반 의사결정:**
   - 스마트팜은 다량의 데이터를 수집하고 분석함으로써 농부들이 더 정확한 의사결정을 내릴 수 있게 해줍니다. 작물 생산, 재고 관리, 가격 예측 등에 대한 데이터 기반의 의사결정은 농업 경영의 효율성을 높입니다.

5. **식량 안정성 및 식량 안전성 강화:**
   - 스마트팜의 기술은 작물의 안정적인 생산을 촉진하고 작물의 품질을 향상시켜 식량 안전성을 강화합니다. 또한 감시 시스템을 통해 유해한 물질이나 질병의 조기 발견이 가능해져 식량 안전성이 향상됩니다.

6. **농촌 지역 활성화:**
   - 스마트팜의 도입은 농촌 지역의 경제와 삶의 질을 향상시킬 수 있습니다. 새로운 기술 도입과 혁신은 농촌에서 일하는 노동력의 기술 수준을 향상시키고, 새로운 일자리 창출에도 기여할 수 있습니다.
  
이 프로젝트의 목적은 현재 스마트팜에 대해서 기술적인 지원을 어떻게 할 수 있는지 이해하고, 미래에 무엇을 할 수 있는가에대해서 알기 위한 기반을 다짐이다. 

# 프로젝트 구성요소 (Archtiecture)

1. **Firebase**
   - 구글에서 제공하는 Firebase Realtime Database 를 Rasberry Pi Pico W와 Web을 연동하여 응용을 계획한다. Web 또는 App과 연동할수 있는 Firebase 데이터 베이스를 구성하고, IOT장비와 연동하여 다양한 센서들의 데이터를 저장하고, 동작 할 수 있게 설계하였다.
   ![파이어베이스와 앱웹피코](https://github.com/sangse/SFarm/assets/145996429/141b0d31-60f3-455a-a890-f51991b5614e)

2. **RasberryPi Pico W:**
   - 라즈베리파이 피코w는 마이크로 컨트롤 모듈인데 와이파이를 연결 할 수 있어서 웹과의 통신을 할수있고, micropython을 이용해서 보다 쉽게 조작이 가능합니다.
   파이썬 기반이여서 다양한 센서들의 라이브러리가 있어 활용하기가 쉽습니다. 농장에 필요한 센서로는 온습도센서(DHT11), 조광센서(bh1750), 12v LED등,5v DC모터 등이 있습니다. 추후에 필요하다고 생각한 장비는 추가할 예정입니다.
   

![피코회로도](https://github.com/sangse/SFarm/assets/145996429/c7f65965-ff72-4567-82a1-b7ad29db36e1)


<!-- 두 번째와 세 번째 이미지는 아래 칸에 나눠서 배열 -->
<div align = "center"; style="display: flex; justify-content: space-between; margin-top: 20px;">
    <img src="https://github.com/sangse/SFarm/assets/145996429/5a89131b-9b61-412c-8d94-c0d25ebbbcbd" alt="이미지2" style="width: 33%;">
    <img src="https://github.com/sangse/SFarm/assets/145996429/4ab354e5-9c7c-4df8-8745-a536a5d22483" alt="이미지3" style="width: 33%;">
</div>
   
3. **수경재배 활용**
   - 집 안에서 재배 할 수 있는 작물을 선정하였습니다. 계획은 실내에서 바질을 재배하는 것이 목표였으나, 바질의 성장이 꽤나 오랜시간이 들이게 되서 빠르게 수경재배 시스템을 구현해 보고자 상추류도 같이 재배작물에 포함하게 되었습니다. 이 두 가지 작물 모두 수경재배(양액재배)를 활용 할 수 있어서 실내에서 재배를 할 수 있습니다. 그리고 야외에서 재배하는 방법보다 온습도 조절이 용이하다는 장점이 있습니다. 인터넷에서 쉽게 수중재배기계를 살수있지만 작물들의 생장 데이터가 필요한 것이기 떄문에 라즈베리파이를 활용한 통제가능한 상황을 만들고 싶었습니다.
   

4. **회로도**


---

# 작물 키우기
1. **발아시키기**
- 청상추와 바질 씨앗을 물티슈 위에 올려놓고 물뿌리개로 물을 적셔준다. 바질씨앗은 청상추 보다 늦게 발아를 시작하기 떄문에 구분을 나눠줘서 진행하였다. 발아 시킬때의 주의 할점은 밝은 곳에서 발아를 시키면 발아가 잘 안될수 있으므로 피하는 게좋다. 아래와 같이 호일을 씌어줘서 발아하는 것이 좋다.
<div style="display: flex; justify-content: space-between;">

  <!-- 첫 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/1fa4a3e5-fefd-480c-8fe4-8b22d836800d" alt="이미지1" width="333">

  <!-- 두 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/853c9c69-3b81-441a-9623-9aab373c5fec" alt="이미지2" width="333">

  <!-- 세 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/993e4ed1-395a-47c6-baad-210d528e5906" alt="이미지3" width="333">

</div>
- 시간이 지나서 발아한 모습이다. 뿌리의 형태가 나올떄까지는 씨앗자체 양분으로 자라난다. 그 후에 토지 역할을 해줄 스펀지로 옮겨줘야한다.


2. **양액 및 배지 설치**
- 시간이 지나서 발아시킨 씨앗에 어느정도 뿌리 형태와 잎이 나오게 되면, 땅의 역할을 해줄수 있는 스펀지에 옮겨서 심어야한다. 스펀지는 물의 흡수가 잘되고 통풍도 잘되서 땅의 역할을 대신하기에 적합하다.
<div style="display: flex; justify-content: center; align-items: center; ">
   <img src = "https://github.com/sangse/SFarm/assets/145996429/4affb6f1-d1ac-4ec2-885c-65a54d264697" alt = "배지옮" height:333;>
</div>
- 양액은 시중에서 파는 물푸레 제품을 사용하였습니다. 상추 같은 엽채류 종류의 양액비율이 나와있기 떄문에 쉽게 양액비율 조절을 할수 있습니다. 처음 뿌리가 뻗지 않은 상태에서는 500배 비율로 영양을 주고, 뿌리가 어느정도 배지에 자리를 잡으면 250배로 바꾸어줍니다.


<div style="display: flex; justify-content: center; align-items: center; ">
   <img src = "https://github.com/sangse/SFarm/assets/145996429/b98d3f21-d461-420f-86b2-c6cbece3f963" alt = "배지옮" height:333;>
</div>

3. **수경재배 옮겨주기**
- 뿌리가 어느정도 배지에 자리를 잡게되면 좀 더 큰 환경으로 옮겨 줘야한다. 그리고 실내에서 키우는 작물이다 보니 빛의 양이 부족하기 떄문에 따로 빛을 공급할 수 있는 LED를 설치하였다. LED는 12v 어뎁터와 납떔하고, 기기와 연결하여 웹에서 제어 할수 있게 하였다.
- 양액이 고여있으면 녹조 현상이 발생하여서 모터를 설치하였고, 기기와 연결해주어 주기적으로 순환할수 있도록 하였다.


<div style="display: flex; justify-content: space-between;">

  <!-- 첫 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/08805ef4-ecd8-4b43-abac-68c9cfec59e0" alt="이미지1" width="333">

  <!-- 두 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/b271c469-756e-4b1d-af6c-a9b35f9b8fd4" alt="이미지2" width="333">

  <!-- 세 번째 이미지 -->
  <img src="https://github.com/sangse/SFarm/assets/145996429/d96b6146-8d50-4180-bb70-93000c6f3cd8" alt="이미지3" width="333">

</div>


https://github.com/sangse/SFarm/assets/145996429/7ad4d091-5204-4e62-96be-8e0331fcf86e
- 수경재배를 하다보니 물이 고인물에 작물과 함께 있어서 녹조현상이 발생하게 되었다. 그래서 양액이 들어있는 물을 흐르게해서 주는 방식으로 바꾸게 되었다. 하지만 이 방법도 결국엔 작물과 함께 물이 담겨있기 때문에 구조를 변경했다.



https://github.com/sangse/SFarm/assets/145996429/33489d57-3a95-4459-a0d7-8289d6637475
- 수경재배를 목표로 했지만, 에어로포닉스 환경으로 분무수경을 시도해볼 예정이다. 분무수경은 뿌리 부분을 물에 담가 두는 것과 다르게 일정시간마다 물을 분사시켜서 키우는 것이다. 실내에서 구현만 할 수있다면 항상 물을 흘리는 것보다 더 쾌적한
  환경을 조성하는 데 도움이 될것 같다.
---
# Micropython, Firebase, Web 설정
## 1. Rasberrypi pico를 파이썬 코드로 작동할수 있는 Micropython 전용 IDE Thonny를 사용하여 코드를 작성하였다. 아래 코드는 main.py 코드이고 주석을 참고하면 이해하는데 도움이 될것같다.
 
```python

import dht
from machine import Pin,ADC
import utime
import network
import urequests

# 피코를 와이파이와 연결
SSID = 'your wifi ID'
Password = 'your wifi password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, Password)

while not wlan.isconnected():
    print('연결중')
    utime.sleep(0.5)
    pass
print('Wi-Fi 연결 성공')

# Firebase의 Realtime Database와 연결하기 위한 URL을 설정합니다.
url = "your Realtime databse url."

# 현재 시간을 초 단위로 얻어오기 current_time을 사용하여 현재 날짜 및 시간을 출력하려면 다음과 같이 변환.
current_time = utime.time()
current_datetime = utime.localtime(current_time)
year, month, day, hour, minute, second, _, _ = current_datetime
formatted_datetime = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
print("피코 시작 -> 현재 날짜와 시간:", formatted_datetime)



# PICO에서 입출력 설정 값. 모터와 DHT11 센서가 같은 통신선을 사용하면 에러날 확률이 높다.
d = dht.DHT11(Pin(17))  # 17번 GPIO 핀을 사용 I2C0_SCL
l = ADC(28)				   # 28번 GPIO 핀을 사용 
LED = Pin(16,Pin.OUT)	# 16번 GPIO 핀을 사용 I2C0_SDA
motor = Pin(15,Pin.OUT) # 15번 GPIO 핀을 사용 I2C1_SCL



while True:
    # 측정시간 
    try:  
        current_time = utime.time()
        current_datetime = utime.localtime(current_time)
        year, month, day, hour, minute, second, _, _ = current_datetime
        

        
        #firebase에 5분마다 데이터 전송하고 모터 작동하여 양액 순환시켜주기
        if minute%5 == 0:
            try:
                # 측정값
                light_t = l.read_u16()
                d.measure()
                temperature = d.temperature()
                humidity = d.humidity()
                
                print(f'온도: {temperature}°C, 습도: {humidity}%, 광도: {light_t} lux')
                date = "{:04d}-{:02d}-{:02d}".format(year,month,day)
                time = "{:02d}:{:02d}:{:02d}".format(hour,minute,second)
                
                new_data = {time:{'temperature':temperature,'humidity':humidity,'lux':light_t}}
                urequests.patch(url+'/date_time/'+date+'.json', json = new_data).json()
                print('데이터 업데이트',time)
                utime.sleep(10)
                motor.value(1)
                utime.sleep(80)
                motor.value(0)

            except Exception as e:
                print("업데이트 에러 다시 시도합니다. 아무키를 눌러주세요.",e)
                pass
            
            
        #firebase에서 LED 신호 읽어오기 -> 1이면 켜지는 신호, 0이면 꺼지는 신호.
        try:
            response = urequests.get(url+"/led.json").json()
            print("led:", response['led'])
            # 가져온 데이터에 따라서 LED 핀의 출력 값을 변경합니다
            if (response['led'] == 1) :
                LED.value(1)
            else :
                LED.value(0)
        except:
            print("LED json파일 불러오기 실패 다시시도. 아무키를 눌러주세요.")
            pass
        
        utime.sleep(3)
    # 온습도 센서에서 오류가나서 프로그램 멈춤현상 오류 패스.    
    except Exception as e:
        utime.sleep(1)
        print(e)
        pass
     
```
## 2. Firebase을 통해서 센서들이 읽어오는 실시간 데이터를 저장하고, pico에 신호를 보내서 LED 동작을 제어할수있다.
   - 처음으로 Firebase를 사용할 떄 Realtimebase에서 사용권한을 설정해준다. 테스트환경이라서 모든 사람들이 url주소만 알고 있다면 읽고 쓰는게 가능하게 설정하였다.
     ![스크린샷 2023-11-27 120936](https://github.com/sangse/SFarm/assets/145996429/84c4390e-f638-4120-b840-b712309c966c)

   - 온습도,광도를 저장하는 데이터 구조이다. 날짜와 시간에흐름에따라서 저장을한다. 현재는 10분마다 데이터를 저장하고 있다. 이렇게 저장된 데이터는 나중에 머신러닝을 이용해서 학습데이터로도 이용할 계획이다.
      ![스크린샷 2023-11-27 120859](https://github.com/sangse/SFarm/assets/145996429/0ef2fd91-2ec0-452e-91c4-7325b125823b)
   - LED 제어 전용 Key값을 만들어준다. Web이랑 Micropython이 firebase의 LED key값을 참조하여 제어가 가능해진다.
      ![스크린샷 2023-11-27 121106](https://github.com/sangse/SFarm/assets/145996429/e98d5ee5-aea9-4342-a2d0-bd0d64363515)

## 3. Web상에서 그래프로 온습도, 광도 제어값을 체크하고 LED크고,켜기
   - HTML코드를 작성해서 그래프를 공간과 LED 버튼을 구현해주었고, 자바스크립트를 통해 Firebase에서 LED key값과 데이터들이 업데이트 될떄마다 실시간으로 업데이트 해주도록 하였다.
   ![스크린샷 2023-11-27 175616](https://github.com/sangse/SFarm/assets/145996429/e928e3ed-7014-412e-bcec-db91b9731cb9)

   https://github.com/sangse/SFarm/assets/145996429/15d8e00b-5b33-4558-8233-a422a3fd1996


---
# 업데이트 예정
- 1. 통풍을 위한 모터모듈 추가.
  2. 생장 데이터를 위한 카메라 센서 추가.
  3. Web에서 원하는 기간 만큼의 데이터 볼수있게 구축.
  4. Firebase에서 권한 나누어서 보안설정.
  5. 분무수경재배 구조로 바꾸기.


