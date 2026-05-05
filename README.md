# Autonomous Vehicle Perception

자율이동체시스템 과제 수행을 위해 KITTI 데이터셋을 활용하여 차량 주행 환경에서의 객체 탐지와 차선 검출을 구현한 프로젝트입니다.

본 프로젝트는 자율주행 인식(Perception) 과정에서 중요한 두 가지 요소인 객체 탐지(Object Detection)와 차선 검출(Lane Detection)을 중심으로 구성되어 있습니다.

## Project Structure

```bash
.
├── README.md
├── .gitignore
├── object_detection/
│   ├── README.md
│   ├── object_detection.py
│   └── compare_frame.py
│
└── lane_detection/
    ├── README.md
    ├── lane_detection.ipynb
    └── requirements.txt