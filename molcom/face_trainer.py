import os
import pickle

import cv2
import numpy as np
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
        self._id = self.__get_face_id()

    def __get_face_id(self) -> int:
        """
        얼굴의 ID를 반환합니다.

        Returns
        -------
        int
            얼굴의 ID. 이 ID는 학습된 모델에 저장됩니다.

        Raises
        ------
        Exception
            동일한 이름이 이미 모델에 등록되어 있을 경우 발생합니다.
        """

        with open("face_id.pickle", "rb") as f:
            faces: dict[int, str] = pickle.load(f)

        if self.name in faces.values():
            raise Exception("이미 등록된 이름입니다!")

        return len(faces) + 1

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
        self.__train()

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
                cv2.imwrite(
                    f"image/{self.name}_{self._id}_{cnt}.jpg",
                    frame[y : y + h, x : x + w],
                )

            if cv2.waitKey(1) & 0xFF == ord("q") or cnt == 100:
                break

        cap.release()
        cv2.destroyAllWindows()

    def __train(self) -> None:
        """
        저장된 얼굴 이미지들을 이용해 얼굴을 학습합니다.
        학습된 모델은 model 폴더에 저장됩니다.
        """
        detector = cv2.CascadeClassifier(
            "./cascade/haarcascade_frontalface_default.xml"
        )

        self.__capture_face()

        images = [
            os.path.join("image", x)
            for x in os.listdir("image")
            if x.startswith(self.name)
        ]

        face_samples = []
        _ids = []

        for image in images:
            gray_img = Image.open(image).convert("L")  # grayscale
            img_numpy = np.array(gray_img, "uint8")

            _id = int(os.path.split(image)[-1].split("_")[1])

            for (x, y, w, h) in detector.detectMultiScale(img_numpy):
                face_samples.append(img_numpy[y : y + h, x : x + w])
                _ids.append(_id)

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(face_samples, np.array(_ids))

        recognizer.write(f"model/face_model.yml")

        with open("face_id.pickle", "wb") as f:
            faces: dict[int, str] = pickle.load(f)

            faces[self._id] = self.name
            pickle.dump(faces, f)
