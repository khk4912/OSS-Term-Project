import platform
from enum import Enum

import pyautogui


class OS(Enum):
    WINDOWS = "windows"
    MAC = "mac"


class WindowSwitcher:
    def __init__(self) -> None:
        self.os = self.__os()

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
