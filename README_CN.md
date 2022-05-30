简体中文 | [English](README.md)

# BuildPyc
 Python py文件编译成pyc文件

#### 使用方法


```python

# 方法1，直接运行文件构建当前项目

python build_pyc


# 方法2，导入类
from build_pyc import BuildPyc

"""
初始化方法

可选参数:
@param {str} project_name 构建文件存放目录 可选
@param {list} exclude_dirs 排除目录 可选 示例 ['__pycache__', '.git', '.idea', 'venv']
@param {list} exclude_files 排除文件后缀 可选 示例 ['.pyc', '.DS_Store']

"""
build_pyc = BuildPyc()

# 默认构建当前项目
# 参数：
# is_py = False （True：构建项目包含py文件，False不包含py文件）
build_pyc.build_project()


# 编译指定路径的文件
build_pyc.build_dir('path')


# 编译单个文件
build_pyc.build_file('main.py')
```