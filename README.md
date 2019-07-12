# pymvn
package your python code and dependices into single one zip file, then run `python *.zip` to run your project.
模仿maven的形式，利用__main__.py的特性，将python项目和依赖打包成一个zip文件，可以直接使用python *.zip运行

安装：
    pip install pymvn

使用：
    打开项目根路径
    python -m pymvn init
    在生成的.pymvn文件中输入项目main函数和依赖路径
    如：
    main_func = main.main
    site_packages_path = venv/Lib/site-packages
    然后使用命令打包
    python -m pymvn

运行实例：
python prj.zip
>> hello, pymvn
