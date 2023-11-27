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


# 현재 시간을 초 단위로 얻어오기 current_time을 사용하여 현재 날짜 및 시간을 출력하려면 다음과 같이 변환.
current_time = utime.time()
current_datetime = utime.localtime(current_time)
year, month, day, hour, minute, second, _, _ = current_datetime
formatted_datetime = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
print("피코 시작 -> 현재 날짜와 시간:", formatted_datetime)


# PICO에서 입출력 설정 값. -> 모터와 같은 통신선을 사용하면 etime error이 높은 확률로 나타남
d = dht.DHT11(Pin(17))  # 17번 GPIO 핀을 사용 I2C0_SCL
l = ADC(28)				# 28번 GPIO 핀을 사용 
LED = Pin(16,Pin.OUT)	# 16번 GPIO 핀을 사용 I2C0_SDA
motor = Pin(15,Pin.OUT) # 15번 GPIO 핀을 사용 I2C1_SCL


while True:
    # 측정시간
    try:
        
        current_time = utime.time()
        
        current_datetime = utime.localtime(current_time)
        
        year, month, day, hour, minute, second, _, _ = current_datetime
        

        
        #firebase에 5분마다 데이터 전송하고 모터작동하여 양액 순환.
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
    # 가끔 온습도 센서에서 오류가나서 프로그램 멈춤현상 오류 패스.    
    except Exception as e:
        utime.sleep(1)
        print(e)
        pass
    

    
    
    
    
    
