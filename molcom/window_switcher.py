import platform
import time
from enum import Enum
from threading import Event


import pyautogui


class OS(Enum):
    WINDOWS = "windows"
    MAC = "mac"


class WindowSwitcher:
    def __init__(self, evt: Event) -> None:
        self.os = self.__os()
        self.event = evt

    def __os(self) -> OS:
        if platform.system() == "Windows":
            return OS.WINDOWS

        elif platform.system() == "Darwin":
            return OS.MAC

        else:
            raise Exception("알 수 없는 OS입니다!")

    def switch_window(self):
        if self.os == OS.WINDOWS:
            pyautogui.hotkey("alt", "tab")

        elif self.os == OS.MAC:
            pyautogui.hotkey("command", "tab", interval=0.1)

    def run(self):
        while True:
            self.event.wait()
            self.event.clear()

            self.switch_window()
            time.sleep(1)
