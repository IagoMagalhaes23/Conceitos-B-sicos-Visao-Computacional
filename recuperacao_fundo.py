import numpy as np
import cv2

video = cv2.VideoCapture(r'busy.mp4')

TIMES = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=1000)

frames = []

for frameOI in TIMES:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    check, frame = video.read()
    frames.append(frame)

recuperacaoFundo = np.median(frames, axis=0).astype(dyte=np.uint8)
cv2.imwrite("fundo.jpg", recuperacaoFundo)
cv2.imshow(recuperacaoFundo)