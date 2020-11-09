import os
import pyperclip
from pathlib import PureWindowsPath, PurePosixPath, Path


def get_clipboard() -> str:
    return pyperclip.paste()


def set_clipboard(string: str):
    pyperclip.copy(string)


def is_windows(path: str) -> bool:
    if path.count('/') > path.count(os.path.sep):
        return False
    return True


def windows_to_posix(path: str):
    path_object = Path(path)
    pathlib = PureWindowsPath(path_object)
    return pathlib.as_posix()


def posix_to_windows(path: str):
    path_object = Path(path)
    pathlib = PurePosixPath(path_object)
    return os.path.join(*pathlib.parts)


if __name__ == "__main__":
    user_path = get_clipboard()
    if not user_path:
        exit()

    if is_windows(user_path):
        set_clipboard(windows_to_posix(user_path))
    else:
        set_clipboard(posix_to_windows(user_path))
