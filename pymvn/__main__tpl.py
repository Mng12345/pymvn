"""
# __main__.py模板
import sys
import importlib


if __name__ == "__main__":
    # 设置site-packages
    site_packages_path = "{{site_packages_path}}"
    sys.path.append(site_packages_path)
    # main_func
    main_func_path = "{{main_func_path}}"
    items = main_func_path.split(".")
    func = items[-1]
    module = items[-2]
    path_ = ".".join(items[: -2])
    sys.path.append(path_)
    # 导入module，执行func
    if not path_:
        module_obj = importlib.import_module(module)
    else:
        module_obj = importlib.import_module(f"{path_}.{module}")
    func_obj = getattr(module_obj, func)
    func_obj()
"""
