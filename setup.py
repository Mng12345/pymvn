from setuptools import setup, find_packages


setup(
    name='pymvn',
    version="0.0.3",
    description=(
        """package python src and site-packages into *.zip, 
           then use `python *.zip` to run your program in any
           computer which has the correct python interpreter!,
           for current version,your project must use virtualenv"""
    ),
    author="zhangming",
    author_email="1570977353@qq.com",
    maintainer="zhangming",
    maintainer_email="1570977353@qq.com",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    package_data={"pymvn": [
        "*.py-tpl"
    ]},
    platforms=["all"],
    url="https://github.com/Mng12345/pymvn",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ]
)