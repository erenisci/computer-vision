import cv2

face_detector = cv2.CascadeClassifier(
    "Cascades/haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("Models/lbph_classifier_own.yml")

width, height = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(2)

while True:
    connected, image = camera.read()
    if not connected:
        break

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(
        image_gray, scaleFactor=1.09, minNeighbors=9, minSize=(40, 40))

    for (x, y, w, h) in detections:
        image_face = cv2.resize(image_gray[y:y + h, x:x + w], (width, height))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

        id, confidence = face_recognizer.predict(image_face)

        name = 'Ufo'
        if confidence < 65:
            if id == 1:
                name = 'Jones'
            elif id == 2:
                name = 'Gabriel'
            elif id == 3:
                name = 'Eren'

        cv2.putText(image, name, (x, y + h + 30), font, 1.2, (0, 255, 255), 1)
        cv2.putText(image, f'{confidence:.2f}',
                    (x, y + h + 60), font, 1, (0, 255, 255), 1)

    cv2.imshow("Face", image)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
