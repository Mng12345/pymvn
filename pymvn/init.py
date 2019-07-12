# 初始化项目
import os

from loguru import logger

from pymvn.parsepybuild import get_root_path


def init():
    root_path = os.getcwd()
    pybuild_path = f"{root_path}/.pymvn"
    if not os.path.exists(pybuild_path):
        with open(pybuild_path, mode="w", encoding="utf-8") as f:
            f.write("main_func = \n")
            f.write("site_packages_path = \n")
