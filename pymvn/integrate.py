# 将源码和依赖包打包至.zip
import os
import shutil


# 压缩文件

from pymvn.parsepybuild import get_root_path, get_site_packages_path, get_main_func_path


def zipdir(dirpath: str, filename: str, format: str):
    shutil.make_archive(filename, format=format, root_dir=dirpath)


# 将根目录下的所有文件及文件夹及site-packages文件夹打包在一个文件夹里
# project_name
#     src
#     site_packages
#     other_dir
def package():
    root_path = os.getcwd()
    prj_name = os.path.split(root_path)[1]
    objs = os.listdir(root_path)
    root_path_copy = f"{root_path}/{prj_name}"
    if os.path.exists(f"{root_path}/{prj_name}"):
        os.remove(f"{root_path}/{prj_name}")
    os.mkdir(f"{root_path}/{prj_name}")
    for obj in objs:
        if obj == prj_name:
            continue
        final_path = f"{root_path}/{obj}"
        final_path_copy = f"{root_path_copy}/{obj}"
        if os.path.isdir(final_path):
            if obj != "venv":
                shutil.copytree(final_path, final_path_copy)
            else:
                # 将site_packages复制到prj_name下
                final_path = f"{final_path}/Lib/site-packages"
                final_path_copy = f"{final_path_copy}/site-packages"
                shutil.copytree(final_path, final_path_copy)
        elif os.path.isfile(final_path):
            shutil.copyfile(final_path, final_path_copy)
    generate_mainpy(prj_name)
    zipdir(f"{root_path}/{prj_name}", prj_name, "zip")
    # 删除prj_name
    # os.remove(f"{root_path}/{prj_name}")


def generate_mainpy(prj_name: str):
    module_path = os.path.split(__file__)[0]
    # 解析__main_.py-tpl
    mainpy_path = f"{os.getcwd()}/{prj_name}/__main__.py"
    if os.path.exists(mainpy_path):
        os.remove(mainpy_path)
    with open(mainpy_path, mode="w", encoding="utf-8") as f:
        pass
    with open(mainpy_path, mode="w", encoding="utf-8") as fw:
        with open(f"{module_path}/__main__tpl.py", mode="r", encoding="utf-8") as f:
            for line in f:
                if not line or '"""' in line:
                    continue
                if "{{site_packages_path}}" in line:
                    line = line.replace("{{site_packages_path}}", get_site_packages_path())
                if "{{main_func_path}}" in line:
                    line = line.replace("{{main_func_path}}", get_main_func_path())
                fw.write(line)

