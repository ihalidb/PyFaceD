import pathlib
import cv2
from PIL import ImageFont, ImageDraw, Image

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
        text = ("{} Yuz Tespit Edildi".format(len(faces)))
        cv2.putText(frame, str(text), (10, 470), font, 1, (255, 255, 255), 1, cv2.FILLED)
    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
