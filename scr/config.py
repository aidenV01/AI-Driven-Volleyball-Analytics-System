import cv2

#MODELS_PARAMS
BALL_MODEL_PATH = "model/ball.onnx"
CAT_BOOST_MODEL_PATH = "model/catboost_ball_model.cbm"

INPUT_W = 512
INPUT_H = 288
HEATMAP_TRASH = 0.5
SEQ_LEN = 9

Probability = 0.8

#VIDEO_PARAMS
INPUT_VIDEO_PATH = "all_video/video_name.mp4"
OUTPUT_VIDEO_PATH = "all_video/result_traks_and_videos/video_name.mp4"

cap = cv2.VideoCapture(INPUT_VIDEO_PATH)

FPS = cap.get(cv2.CAP_PROP_FPS)
VIDEO_WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
VIDEO_HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#TRACKER_PARAMS
GAP_WITH_CONFIRMED = 30
GAP_WITHOUT_CONFIRMED = 5
LEN_MAX_TRACK = 15

#JSON_PARAMS
JSON_SAVE_TRACK_PATH = "all_video/result_traks_and_videos/json_name.json"