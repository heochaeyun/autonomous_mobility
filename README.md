# Autonomous Mobility

KITTI 데이터셋을 기반으로 차량 주행 환경에서의 객체 탐지(Object Detection)와 차선 검출(Lane Detection)을 구현한 프로젝트입니다.

본 프로젝트는 자율주행 인식(Perception) 과정에서 중요한 두 가지 요소를 중심으로 구성되어 있습니다.

- 객체 탐지: 주행 환경에서 차량, 보행자 등 주요 객체 인식

- 차선 검출: 도로 구조 및 차선 위치 인식

각 기능에 대한 상세 구현 및 결과는 하위 디렉토리의 README에서 확인할 수 있습니다.


## Project Structure

```bash
.
├── .gitignore                     # Git에서 제외할 파일 및 폴더 목록
├── README.md                      # 프로젝트 전체 설명
├── requirements.txt               # 필요한 Python 패키지 목록
├── object_detection/
│   ├── README.md                  # 객체 탐지 파트 설명
│   ├── assets                     # README 및 문서용 이미지
│   ├── object_detection.py        # YOLOv8 객체 탐지 코드
│   ├── compare_frame.py           # 좌/우 카메라 비교 코드
│   ├── yolov8n.pt                 # YOLO 모델 (ignored)
│   ├── YOLO_left.mp4              # 결과 영상 (ignored)
│   ├── YOLO_right.mp4             # 결과 영상 (ignored)
│   ├── left_frames/               # 추출된 프레임 이미지 (ignored)
│   ├── right_frames/              # 추출된 프레임 이미지 (ignored)
│   └── compare_frames/            # 비교 프레임 이미지 (ignored)
│
├── lane_detection/
│   ├── README.md                  # 차선 검출 파트 설명
│   ├── assets                     # README 및 문서용 이미지
│   ├── lane_detection.ipynb       # 차선 검출 실험 ipynb
│   ├── Ultra-Fast-Lane-Detection/ # 외부 차선 검출 저장소 (ignored)
│   └── outputs/                   # Bayesian/UFLD 결과 폴더 (ignored)
│
└── auto_env/                      # Python 가상환경 폴더 (ignored)
```

---

## Results

### Object Detection
![object](object_detection/assets/000007.png)

### Lane Detection
![lane](lane_detection/assets/ufld_000015.png)