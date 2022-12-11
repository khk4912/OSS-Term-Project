import os

import cv2
from PIL import Image


class FaceTrainer:
    def __init__(self, name: str) -> None:
        """
        얼굴 학습 클래스

        Parameters
        ----------
        name : str
            얼굴 대상의 이름. 이 이름은 얼굴 인식 결과에 표시됩니다.
        """

        self.name = name

    def train_with_images(self, images: list[str]):
        """
        이미지들을 이용해 얼굴을 학습하는 메소드입니다.

        Parameters
        ----------
        images : list[str]
            학습에 사용할 이미지들의 경로 리스트입니다.
        """

    def train_with_camera(self):
        """
        카메라를 이용해 얼굴을 학습하는 메소드입니다.
        """

        self.__capture_face()

    def __capture_face(self):
        """
        카메라를 이용해 얼굴을 인식하고, 저장합니다.
        100장이 저장되거나 인식 중 q를 누르면 종료됩니다.

        Raises
        ------
        Exception
            카메라에 엑세스 할 수 없을 때 발생합니다.
        """
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(
            "./cascade/haarcascade_frontalface_default.xml"
        )

        while True:
            ret, frame = cap.read()

            if not ret:
                raise Exception("카메라를 열 수 없습니다!")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30),
            )

            cnt = 0

            for (x, y, w, h) in faces:
                cnt += 1

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # 얼굴 이미지를 저장
                cv2.imwrite(f"image/{self.name}_{cnt}.jpg", frame[y : y + h, x : x + w])

            if cv2.waitKey(1) & 0xFF == ord("q") or cnt == 100:
                break

        cap.release()
        cv2.destroyAllWindows()
