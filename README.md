# Autonomous Mobility

자율이동체시스템 과제 수행을 위해 KITTI 데이터셋을 활용하여 차량 주행 환경에서의 객체 탐지와 차선 검출을 구현한 프로젝트입니다.

본 프로젝트는 자율주행 인식(Perception) 과정에서 중요한 두 가지 요소인 객체 탐지(Object Detection)와 차선 검출(Lane Detection)을 중심으로 구성되어 있습니다.

## Project Structure

```bash
.
├── .gitignore
├── README.md
├── requirements.txt
├── object_detection/
│   ├── object_detection.py
│   ├── compare_frame.py
│   ├── yolov8n.pt                 # YOLO model (ignored)
│   ├── YOLO_left.mp4              # Result video (ignored)
│   ├── YOLO_right.mp4             # Result video (ignored)
│   ├── left_frames/               # Extracted frames (ignored)
│   ├── right_frames/              # Extracted frames (ignored)
│   └── compare_frames/            # Comparison frames (ignored)
│
├── lane_detection/
│   ├── lane_detection.ipynb
│   ├── Ultra-Fast-Lane-Detection/ # External lane detection repo (ignored)
│   └── outputs/                   # Lane detection results (ignored)
│
└── auto_env/                      # Python virtual environment (ignored)
```

## 설치 및 모델 준비

```bash
pip install -r requirements.txt
```

차선 검출에 사용하는 Ultra-Fast-Lane-Detection 코드는 노트북 안에서 설치하지 않고, 아래처럼 별도로 클론해서 사용합니다.

```bash
cd lane_detection
git clone https://github.com/cfzd/Ultra-Fast-Lane-Detection.git
```

클론이 끝나면 pretrained 모델 파일을 직접 다운로드해야 합니다. 모델은 Ultra-Fast-Lane-Detection README의 `Trained models` 섹션에 있는 Tusimple-18 모델 링크에서 받을 수 있습니다.

- 모델 다운로드 위치: https://github.com/cfzd/Ultra-Fast-Lane-Detection
- 사용할 모델: `Tusimple` pretrained ResNet-18 model
- 저장 파일명: `tusimple_18.pth`

다운로드한 모델은 아래 경로에 `models` 폴더를 만든 뒤 넣어줍니다.

```bash
mkdir -p lane_detection/Ultra-Fast-Lane-Detection/models
```

최종 모델 파일 위치는 다음과 같아야 합니다.

```bash
lane_detection/
└── Ultra-Fast-Lane-Detection/
    └── models/
        └── tusimple_18.pth
```

`Ultra-Fast-Lane-Detection/`, `models/`, 결과 이미지와 영상 파일은 용량이 크기 때문에 Git에는 올리지 않고 `.gitignore`로 제외합니다.
