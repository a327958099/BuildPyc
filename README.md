 English | [简体中文](README_CN.md)

# BuildPyc
 Python build py file compile pyc file

#### Method of use


```python

# Method 1: directly run the file to build the current project

python build_pyc.py


# Method 2, import class
from build_pyc import BuildPyc

"""
Initialization method

Optional parameters:
@param {str} project_name Build file storage directory Optional
@param {list} exclude_dirs Exclude directory Optional Example ['__pycache__', '.git', '.idea', 'venv']
@param {list} exclude_files Exclude file suffixes Optional Example ['.pyc', '.DS_Store']

"""
build_pyc = BuildPyc()

# Default build current project
# param：
# is_py = False (True build project includes py files, False does not include py files)
build_pyc.build_project()


# Compile the file with the specified path
build_pyc.build_dir('path')


# Compile a single file
build_pyc.build_file('main.py')
```
