import re
import threading
from tkinter import Button, Tk, messagebox, simpledialog


from face_detect import detect_face
from face_trainer import FaceTrainer
from window_switcher import WindowSwitcher


class MolcomMainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Molcom")
        self.geometry("300x300")
        self.resizable(width=False, height=False)

        self.__init_ui()

    def __init_ui(self):
        face_reg_button = Button(
            self,
            text="얼굴 등록",
            command=self.__face_reg_button_clicked,
        )

        start_button = Button(
            self,
            text="시작",
            command=self.__start_button_clicked,
        )

        face_reg_button.grid(row=1, column=0)
        start_button.grid(row=1, column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def __face_reg_button_clicked(self):
        name = simpledialog.askstring("이름 입력", "이름을 영어로 입력해주세요.")

        if name is None:
            return

        if not re.match(r"[a-zA-Z]", name):
            messagebox.showinfo("잠시만요!", "이름은 알파벳 문자로만 입력할 수 있어요.\n다시 입력해주세요.")
            return

        try:
            trainer = FaceTrainer(name=name)
            trainer.train_with_camera()
        except Exception as error:
            messagebox.showerror("오류!", str(error))
        else:
            messagebox.showinfo("성공!", "얼굴 등록에 성공했어요.")

    def __start_button_clicked(self):
        switcher = WindowSwitcher()
        evt = threading.Event()

        det_face_thread = threading.Thread(target=detect_face, args=(evt,))
        det_face_thread.start()


if __name__ == "__main__":
    window = MolcomMainWindow()
    window.mainloop()
