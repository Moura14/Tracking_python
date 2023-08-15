
import cv2
import sys
from random import randint

(major_ver, minor_ver, subinor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracker_type = tracker_types[6]

if int(minor_ver) < 3:
    tracker = tracker_type
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    elif tracker_type == "MIL":
        tracker = cv2.legacy.TrackerMIL_create()
    elif tracker_type == "KCF":
        tracker = cv2.legacy.TrackerKCF_create()
    elif tracker_type == "TLD":
        tracker = cv2.legacy.TrackerTLD_create()
    elif tracker_type == "MEDIANFLOW":
        tracker = cv2.legacy.TrackerMedianFlow_create()
    elif tracker_type == "MOSSE":
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('videos/video_10.mp4')

if not video.isOpened():
    print('Não foi possível carregar o vídeo')
    sys.exit()

ok, frame = video.read()
if not ok:
    print('Não foi possível ler o arquivo de vídeo')
    sys.exit()

bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)
colors = (randint(0, 255), randint(0, 255), randint(0,255 ))

frame_count = 0
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv2.getTickCount()
    ok, bbox = tracker.update(frame)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2, 1)
        recorte = frame[y:y + h, x:x + w]

        # Redimensionar a região recortada para o tamanho desejado
        width = 74
        height = 39
        recorte_resized = cv2.resize(recorte, (width, height))

        nomeFrame = 'images/frame_%d.jpg' % frame_count
        cv2.imwrite(nomeFrame, recorte_resized)
        frame_count += 1
    else:
        cv2.putText(frame, 'Falha no rastreamento', (100, 88), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255))

    cv2.putText(frame, tracker_type + ' Tracking', (100, 20), cv2.FONT_HERSHEY_COMPLEX, .75, (50, 170, 50), 2)
    cv2.putText(frame, 'FPS ' + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_COMPLEX, .75, (50, 170, 50), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
