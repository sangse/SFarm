import dht
from machine import Pin,ADC
import utime
import network
import urequests

# 피코를 와이파이와 연결
SSID = 'Your WiFi ID'
Password = 'Password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, Password)

while not wlan.isconnected():
    print('연결중')
    pass
print('Wi-Fi 연결 성공')

# Firebase의 Realtime Database와 연결하기 위한 URL을 설정합니다
url = "your firebase Realtime database url."

# 현재 시간을 초 단위로 얻어오기
# current_time을 사용하여 현재 날짜 및 시간을 출력하려면 다음과 같이 변환

current_time = utime.time()
current_datetime = utime.localtime(current_time)
year, month, day, hour, minute, second, _, _ = current_datetime
formatted_datetime = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
print("피코 시작 -> 현재 날짜와 시간:", formatted_datetime)

d = dht.DHT11(Pin(17))  # 17번 GPIO 핀을 사용
l = ADC(28)             # 28번 Analog Pin을 사용해서 조도센서 값 읽어오기.
LED = Pin(16,Pin.OUT)   # 16번 핀은 LED on/off

t_count = 0
while True:
    # 측정시간
    current_time = utime.time()
    current_datetime = utime.localtime(current_time)
    year, month, day, hour, minute, second, _, _ = current_datetime
    formatted_datetime = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
  
    # 측정값
    light_t = l.read_u16()
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    
    print(f'온도: {temperature}°C, 습도: {humidity}%')
    print(light_t)
    with open('data.txt','a') as file:
        file.write(formatted_datetime+' '+str(temperature)+','+str(humidity)+','+str(light_t)+'\n')
    
    if t_count == 120:
        #firebase에서 데이터 읽어와서 써주기 10분마다 데이터 업데이트.
        exsiting_data = urequests.get(url+'/data.json').json()
        new_data = {formatted_datetime:{'temperature':temperature,'humidity':humidity,'lux':light_t}}
        exsiting_data.update(new_data)
        urequests.put(url+'/data.json', json = exsiting_data).json()
        print('데이터 업데이트')
        t_count = 0
        
    
    t_count += 1
    utime.sleep(1)
    
    response = urequests.get(url+"/led.json").json()
    
    print("led:", response['led'])

    # firebase에서 참조한 LED 키 상태를 활용해서 LED를 켜주고 꺼준다.
    if (response['led'] == 1) :
        LED.value(1)
    else :
        LED.value(0)
    
    

    
    
    
    
    
