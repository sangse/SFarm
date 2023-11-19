# SFarm Project.

스마트 농장에 관심이 생겨서 기본적인 프로젝트를 구성해보았다
평소에 즐겨 찾아 먹던 바질을 기본적으로 생산을 해보려고 한다.
기본적으

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
![KakaoTalk_20231115_201613432_06](https://github.com/sangse/SFarm/assets/145996429/4affb6f1-d1ac-4ec2-885c-65a54d264697)
https://github.com/sangse/SFarm/assets/145996429/4affb6f1-d1ac-4ec2-885c-65a54d264697

3. **수경재배 옮겨주기**

---
# Micropython
1. **코드설명**

# Firebase

# Web설정(JavaScript,html..)





