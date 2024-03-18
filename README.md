# CV 07조 BIG-I 👁️
![image](https://github.com/boostcampaitech6/level2-cv-datacentric-cv-07/assets/146207162/19d21e2a-2a30-40a7-879e-ea1833aa3374)
- 프로젝트 명 : 글자 검출 프로젝트
- 프로젝트 전체 기간 (2주) : 2024.01.24 ~ 2024.02.01 19:00
---
# 프로젝트 개요
- OCR (Optimal Character Recognition)은 이미지 속의 문자를 컴퓨터가 인식 할 수 있도록 하는 컴퓨터 비전 분야의 대표적인 기술인데, 본 프로젝트에서는 글자 검출 task를 다루게 됨
- 진료비 영수증 이미지 파일로 구성된 데이터셋에 대하여 글자의 영역을 정확하게 탐지할 수 있는 모델을 구성하는 것을 목표로 함. 다만 Data Centric이라는 주제의 취지에 따라 베이스라인 코드에서 주어진 모델을 그대로 활용해야 한다는 제약이 있음
- 이번 대회에서는 구성한 모델로부터 생성된 UFO 형식의 output.csv 파일을 제출하여 평가를 진행. 해당 파일에는 글자 영역으로 감지된 부분인 bounding box의 좌표정보가 포함되어 있으며, DetEval 방식으로 평가가 이루어짐
- 베이스라인은 작은 글씨를 좀 더 잘 찾기위해 튜닝된 EAST(An Efficient and Accurate Scene Text Detector) 모델을 활용
---
# 평가 방식
- DetEval 방식으로 평가
- 모든 정답/예측박스들에 대해서 Area Recall, Area Precision을 미리 계산
![image](https://github.com/boostcampaitech6/level2-cv-datacentric-cv-07/assets/146207162/94a2f1a2-7352-4d98-b632-97f9291cbc05)
- 모든 정답 박스와 예측 박스를 순회하면서, 매칭이 되었는지 판단하여 박스 레벨로 정답 여부를 측정
- Area Recall, Area Precision이 0 이상일 경우 매칭 여부를 판단하게 되고, 박스의 정답 여부는 Area Recall 0.8 이상, Area Precision 0.4 이상을 기준으로 하고 있음
---
# 팀 구성원 및 역할

  |<a href="https://github.com/kimhankyu">김한규 </a>| <a href="https://github.com/haeun1">민하은 </a> | <a href="https://github.com/HayeonLee88">이하연 </a> | <a href="https://github.com/DorianYellow"> 심유승 </a>| <a href="https://github.com/chyeon01">안채연 </a>| <a href="https://github.com/KANG-dg">강동기 </a>| 
  | :-: | :-: | :-: | :-: | :-: | :-: |
  | <img width="100" src="https://avatars.githubusercontent.com/u/32727723?v=4"> | <img width="100" src="https://avatars.githubusercontent.com/u/87661039?v=4"> | <img width="100" src="https://avatars.githubusercontent.com/u/83398511?v=4"> | <img width="100" src="https://avatars.githubusercontent.com/u/146207162?v=4"> | <img width="100" src="https://avatars.githubusercontent.com/u/86558738?v=4"> | <img width="100" src="https://avatars.githubusercontent.com/u/121837927?v=4"> |

- **강동기**: json파일 작성, Data Labeling, EDA
- **김한규**: 베이스라인 모델 분석, EDA, Data Labeling 
- **민하은**: Data Labeling, EDA, Dataset 비교실험 수행
- **심유승**: 가설설정 및 실험 설계, Dataset 제작, Data Labeling
- **안채연**: Dataset 비교실험 수행, Data Labeling, EDA
- **이하연**: Data Labeling, 서버 환경 설정, EDA, 재학습 코드작성
---
# 프로젝트 수행절차 및 결과
1. 베이스라인 모델 분석
   - 약 16%의 이미지에서 얼룩과 같은 노이즈를 글씨로 잘못 인식
   - 약 33%의 이미지에서 상단 제목 부분을 글씨로 잘못 인식
   - 약 20%의 이미지에서 QR코드의 일부를 글씨로 잘못 인식
   - 약 19%의 이미지에서 QR코드 옆의 세로방향 글씨를 잘 인식하지 못함

![image](https://github.com/boostcampaitech6/level2-cv-datacentric-cv-07/assets/146207162/9a4bb78a-86de-4c95-ace5-e04125fe1812)

2. 가설 설정
   - train 데이터셋에 노이즈가 없기 때문에 모델이 노이즈에 대한 학습을 제대로 하지 못하였음
   - 문서의 상단제목, QR코드 주변 부분과 관련하여, 문서에서 차지하는 비중이 매우 적은 부분이라는 점에 착안하였음 (대부분의 annotation은 표 안에 쓰여진 작은 글씨들에 대한 것임)
3. Train Dataset 제작
   - Dataset A : 노이즈가 추가된 이미지 50장과 노이즈가 없는 이미지 50장, 총 100장으로 구성
   - Dataset B : 문서 상단 제목부분과 QR코드의 비중을 늘린 이미지를 총 60장 제작하였고, 여기에 Dataset A를 0장, 40장, 60장, 80장, 100장을 각각 추가한 5가지 서브 데이터셋으로 구성하였음
5. 실험 수행 및 결과

![image](https://github.com/boostcampaitech6/level2-cv-datacentric-cv-07/assets/146207162/552d7dd8-c608-4809-8415-201afa161376)

![image](https://github.com/boostcampaitech6/level2-cv-datacentric-cv-07/assets/146207162/8ec02c2d-0c92-4f34-9c1f-a5f3a172d09f)

