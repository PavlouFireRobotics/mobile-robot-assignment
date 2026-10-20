# Perception Task — Person Detection and 3D Location Estimation

## Objective

Build a ROS 2 Humble pipeline that detects people in recorded camera images and estimates their approximate 3D locations relative to the robot using LiDAR measurements.

The task covers camera calibration, ROS 2 integration, neural-network inference, and combining camera and LiDAR data. Use a pretrained YOLO model; model training is not required.

## Dataset setup

The `data/` folder is not included in the GitHub repository. Before starting the assignment, download the dataset from [Google Drive](https://drive.google.com/drive/folders/1KTmbN1Ou_jriH-Uyqbd1o_9NuQ03Fl80?usp=drive_link) and manually place it in `src/perception/data/`.

Ensure the calibration images are in `src/perception/data/calibration_images/` and the ROS bag is in `src/perception/data/rosbag/`. Extract any downloaded archives before placing the files.

Unless otherwise stated, paths below are relative to the `src/perception/` directory containing this README.

## Supplied inputs

| Input | Location | Description |
| --- | --- | --- |
| Calibration images | `data/calibration_images/` | Chessboard images captured with the recording camera. |
| ROS 2 bag | `data/rosbag/` | `/m20/camera/front/image_raw`: 370 RGB images, 1280×720.<br>`/LIDAR/POINTS`: 371 clouds in `lidar_link`.<br>Recording duration: 41.2 seconds. |
| Sensor URDF | `front_camera_info/urdf/front_sensors.urdf` | Fixed transforms connecting `lidar_link` to the camera optical frame, `front_wide_angle_camera_frame`, through `base_link_custom` and `front_camera_link`. |


## Part 0 | Docker environment

Use the single repository-level Dockerfile required by the [root assignment README](../../README.md). It must contain ROS 2 Humble and all dependencies needed to build and run both assignment solutions.

- Document the shared Docker image build and run commands in your solution documentation.
- Mount the dataset into the container rather than copying it into the image.
- Save calibration and demonstration outputs to a mounted directory so they remain available after the container exits.
- If you use multiple containers, provide a `compose.yaml` or `docker-compose.yml` at the repository root. Compose is optional when using a single container.

Expected outputs:

- The shared `Dockerfile` at the repository root
- `compose.yaml` or `docker-compose.yml` if the solution requires multiple containers
- Candidate solution documentation with instructions for building the Docker image and ROS 2 packages, performing camera calibration, playing back the ROS bag, and running the complete solution

## Part 1 | Camera calibration

Implement a script to perform offline camera calibration using the supplied chessboard images which are located in `data/calibration_images/`.

The chessboard used for calibration is a 9x7 grid of internal corners. With this configuration, there are 9 corners along the width and 7 corners along the height of the chessboard. Each square on the chessboard is of equal size of 20mm.

The tool must:

- Detect chessboard corners and identify images that cannot be used.
- Estimate camera intrinsics and lens distortion coefficients.
- Save the calibration to `front_camera_info/config/camera_calibration.yaml`, including image dimensions and distortion model.
- Report the overall RMS reprojection error in pixels.

Include a visual example of the detected corners or calibration validation in `results/`. Explain any images you excluded and why.
Use a fisheye camera model. Hint: use `cv2.fisheye.calibrate`.

Expected outputs:
- `scripts/camera_calibration.py`
- `front_camera_info/config/camera_calibration.yaml`
- Visual examples in `results/`

## Part 2 | Camera information and TF publisher

Create a ROS 2 node inside the `front_camera_info` package that:

- Loads the camera’s intrinsic parameters and distortion coefficients from a YAML configuration file.
- Publishes the calibration as `sensor_msgs/msg/CameraInfo` on `/m20/camera/front/camera_info`.

Create a launch file that starts the camera information node and a `robot_state_publisher` node to publish the TF transforms defined in `front_camera_info/urdf/front_sensors.urdf`.

## Part 3 | Person detection


Use a pretrained neural network model to detect humans in the recorded images.

- Publish annotated images on `/m20/camera/front/human/image_annotated` using `sensor_msgs/msg/Image`.
- Publish Detection2DArray on `/m20/camera/front/human/detections` using `vision_msgs/msg/Detection2DArray`.

Using existing inference libraries is encouraged. For example, you may use Ultralytics with a pretrained model such as `yolo26n.pt`.

Real-time processing is not expected for this assignment. You can set the playback speed of the ROS bag to a slower rate if needed.

Expected outputs:

- A ROS 2 package named `human_detection_node` containing the person detection node.
- The two output topics listed above.

## Part 4 | Human location estimation

Use the detected person bounding boxes and the LiDAR data provided in the ROS bag to estimate each detected person's approximate 3D location relative to the robot. Publish the estimated location as a 3D point on a ROS topic. Tracking and persistent person IDs are not required.

Choose any suitable approach.


## Output topics and message contract

| Topic | Message type | Content |
| --- | --- | --- |
| `/m20/camera/front/camera_info` | `sensor_msgs/msg/CameraInfo` | Calibration with the corresponding image header. |
| `/m20/camera/front/human/image_annotated` | `sensor_msgs/msg/Image` | Person bounding boxes and confidence. |
| `/m20/camera/front/human/detections` | `vision_msgs/msg/Detection2DArray` | Person detections for each processed image. |
| `/human/location` | `geometry_msgs/msg/PointStamped` | One 3D point per available person location estimate, in metres, with its timestamp and coordinate frame. |

## Launch requirements

Provide a ROS 2 launch file that starts all nodes needed for the complete perception pipeline. It may include the camera information and TF launch description required in Part 2. ROS bag playback may either be included in this launch system or documented as a separate command.

## Submission

Submit this solution as part of the private GitHub repository described in the [root assignment README](../../README.md).

## Assessment

The assessment will include an interview to discuss your implementation, design choices, and understanding of the perception pipeline. Be prepared to explain your approach to camera calibration, person detection, and 3D position estimation, including any challenges you encountered and how you addressed them.

Internet access and AI assistance are allowed and expected during implementation. However, you must be able to explain and modify any external code or AI-generated content you use during the interview.
