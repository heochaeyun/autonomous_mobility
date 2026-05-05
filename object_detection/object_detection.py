import os
# import cv2
import numpy as np
import matplotlib.pyplot as plt
# from ultralytics import YOLO


############################################
# 1. Trajectory 3D plot
############################################
def plot_trajectory(pose_file):

    poses = []

    with open(pose_file, "r") as f:
        for line in f:
            vals = list(map(float, line.split()))
            T = np.array(vals).reshape(3,4)
            poses.append(T)

    xs, ys, zs = [], [], []

    for T in poses:
        xs.append(T[0,3])
        ys.append(T[1,3])
        zs.append(T[2,3])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(xs, ys, zs)

    ax.set_title("Sequence 04 Trajectory")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.savefig("trajectory_04.png")
    plt.show()


############################################
# 2. YOLO detection
############################################
# model = YOLO("yolov8n.pt")

# target_classes = {
#     0: "person",
#     1: "bicycle",
#     2: "car",
#     7: "truck"
# }

# def process_images(input_dir, output_dir):

#     os.makedirs(output_dir, exist_ok=True)

#     files = sorted([f for f in os.listdir(input_dir) if f.lower().endswith(".png") and not f.startswith(".")])

#     for f in files:

#         img_path = os.path.join(input_dir, f)
#         img = cv2.imread(img_path)

#         results = model(img, classes=[0, 1, 2, 7], verbose=False)

#         for r in results:

#             for box in r.boxes:

#                 cls = int(box.cls[0])
#                 conf = float(box.conf[0])

#                 if cls not in target_classes:
#                     continue

#                 x1,y1,x2,y2 = map(int, box.xyxy[0])

#                 label = f"{cls}:{target_classes[cls]} {conf:.2f}"

#                 cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

#                 cv2.putText(img,label,(x1,y1-10),
#                             cv2.FONT_HERSHEY_SIMPLEX,
#                             0.5,(0,255,0),2)

#         cv2.imwrite(os.path.join(output_dir,f),img)


############################################
# 3. frames → video
############################################
# def make_video(frame_dir, output):

#     files = sorted(os.listdir(frame_dir))

#     first = cv2.imread(os.path.join(frame_dir,files[0]))
#     h,w,_ = first.shape

#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output,fourcc,10,(w,h))

#     for f in files:

#         img = cv2.imread(os.path.join(frame_dir,f))
#         out.write(img)

#     out.release()

############################################
# 실행
############################################

if __name__ == "__main__":

    plot_trajectory("/Volumes/Data/dataset/data_odometry_pose/poses/04.txt")

    # process_images("/Volumes/Data/dataset/data_odometry_gray/sequences/08/image_0", "left_frames")
    # process_images("/Volumes/Data/dataset/data_odometry_gray/sequences/08/image_1", "right_frames")

    # make_video("left_frames", "YOLO_left.mp4")
    # make_video("right_frames", "YOLO_right.mp4")
