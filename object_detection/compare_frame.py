import os
import cv2

left_dir = "left_frames"
right_dir = "right_frames"
output_dir = "compare_frames"

os.makedirs(output_dir, exist_ok=True)

left_files = sorted([f for f in os.listdir(left_dir) if f.endswith(".png")])

for f in left_files:
    
    left_path = os.path.join(left_dir, f)
    right_path = os.path.join(right_dir, f)

    # 오른쪽 이미지 없으면 skip
    if not os.path.exists(right_path):
        continue

    left_img = cv2.imread(left_path)
    right_img = cv2.imread(right_path)

    # 크기 맞추기 (혹시 다를 경우 대비)
    h = min(left_img.shape[0], right_img.shape[0])
    left_img = cv2.resize(left_img, (int(left_img.shape[1]*h/left_img.shape[0]), h))
    right_img = cv2.resize(right_img, (int(right_img.shape[1]*h/right_img.shape[0]), h))

    # 가로 붙이기
    combined = cv2.hconcat([left_img, right_img])

    # 저장
    cv2.imwrite(os.path.join(output_dir, f), combined)

print("완료: compare_frames 폴더 확인")