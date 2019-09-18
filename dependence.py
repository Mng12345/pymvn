# 获取本地文件所在的site-packages的路径
import os


def get_root_dependence_path() -> str:
    # 获取当前文件所在的绝对路径
    curr_file_path = os.path.abspath(__file__)
    # 在路径中搜索site-packages
    curr_file_path = curr_file_path.replace("\\", "/")
    items = curr_file_path.split("/")
    site_packages_index = items.index("site-packages")
    # 获取依赖路径
    root_dependence_path = "/".join(items[0: site_packages_index])
    return root_dependence_path
