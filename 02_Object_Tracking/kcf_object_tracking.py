# KCF (Kernelized Correlation Filter)
import cv2

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture('Videos/race.mp4')

# FPS of the video
# fps = video.get(cv2.CAP_PROP_FPS) # 30
# delay = int(1000 / fps)

# Static delay
delay = 15

ok, frame = video.read()
bbox = cv2.selectROI("Tracking", frame, False)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()

    if not ok:
        break

    ok, bbox = tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
        cv2.putText(frame, 'Object', (x, y + h + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    else:
        cv2.putText(frame, 'Error', (110, 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)

    if cv2.waitKey(delay) & 0XFF == 27:  # Escape
        break
