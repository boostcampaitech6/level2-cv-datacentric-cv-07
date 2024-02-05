import os
import cv2
import numpy as np
import albumentations as A
import re

# 이미지가 저장되어 있는 디렉토리 경로
image_dir = './train_crop'

# augmentation 정의
aug1 = A.GaussNoise(var_limit=(450.0, 500.0), p=1.0)
aug2 = A.RandomFog(fog_coef_lower=0.1, fog_coef_upper=0.2, alpha_coef=0.08, p=1.0)
aug3 = A.ColorJitter(brightness=1.0, contrast=0.6, saturation=0.0, hue=0.0, p=1.0)
aug4 = A.ColorJitter(brightness=0.4, contrast=0.6, saturation=0.0, hue=0.0, p=1.0)

augmentations = [aug1, aug2, aug3, aug4]

# 디렉토리 내의 모든 파일을 탐색
for filename in os.listdir(image_dir):
    # 파일이 .jpg 확장자를 가진 경우
    if filename.endswith(".jpg"): 
        # 이미지 열기
        img = cv2.imread(os.path.join(image_dir, filename))

        # 새로운 파일 이름 생성
        prefix = re.findall(r'\D+', filename)[0]
        number = int(re.findall(r'\d+', filename)[0])

        # 각 augmentation 적용
        for i, augmentation in enumerate(augmentations):
            # 이미지에 augmentation 적용
            augmented_img = augmentation(image=img)['image']
            # 새로운 파일 이름 생성
            new_number = number + (i + 1) * 100000 # 맨 앞자리 숫자를 1, 2, 3, 4 증가
            new_filename = prefix + str(new_number) + '.jpg'
            # 새로운 이미지를 디렉토리에 저장
            cv2.imwrite(os.path.join(image_dir, new_filename), augmented_img)
