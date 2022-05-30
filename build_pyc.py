import os
import sys
import shutil
import compileall


# Build py file compile classes of PyC file
class BuildPyc(object):
    def __init__(self, project_name='build_pyc', exclude_dirs=[], exclude_files=[]):
        self.project_name = project_name
        # System type windows=win32 linux=linux mac=darwin
        self.platform = sys.platform
        # Exclude directory
        self.exclude_dirs = ['__pycache__', '.git', '.idea', 'venv', self.project_name]
        for val in exclude_dirs:
            self.exclude_dirs.append(val)
        # Exclude file suffixes
        self.exclude_files = ['.pyc', '.DS_Store']
        for val in exclude_files:
            self.exclude_files.append(val)
        self.construct_file = os.path.realpath(__file__).split('/')
        if sys.platform == 'win32':
            self.construct_file = os.path.realpath(__file__).split('\\')
        self.construct_file = self.construct_file[len(self.construct_file) - 1]

    # Build compile entire project
    # is_py: Keep py file
    def build_project(self, is_py=False):
        # Get current directory
        cur_path = os.getcwd()
        # Build file save directory
        save_path = os.path.join(cur_path, self.project_name)
        # Delete directory
        if os.path.exists(save_path):
            shutil.rmtree(save_path)

        # Create file save directory
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for root, dirs, files in os.walk(cur_path):
            # Exclude directory
            inp = root[len(cur_path):len(root)]
            if inp:
                is_exclude = False
                for exclude_dir in self.exclude_dirs:
                    if inp[1:len(inp)][0:len(exclude_dir)] == exclude_dir:
                        is_exclude = True
                        break
                if is_exclude:
                    continue
            # Create directory
            if not os.path.exists(save_path + root[len(cur_path):len(root)]):
                os.mkdir(save_path + root[len(cur_path):len(root)])

            for file in files:
                if file == self.construct_file:
                    continue
                # Exclude file
                if file in self.exclude_files:
                    continue
                if os.path.splitext(file)[1] in self.exclude_files:
                    continue
                # Build file path
                file_path = os.path.join(root, file)
                # Build PyC file path
                pyc_path = os.path.join(save_path + inp, str(file))
                # Judge whether it is Py file
                if file.endswith('.py'):
                    pass
                    shutil.copyfile(file_path, pyc_path)
                    compileall.compile_file(pyc_path, ddir=pyc_path, force=True, legacy=True)
                    if not is_py:
                        os.remove(pyc_path)
                else:
                    shutil.copyfile(file_path, pyc_path)

        print('All Done!')

    # Compile all py files in the path
    def build_dir(self, dir_path=None):
        if dir_path:
            compileall.compile_dir(dir_path, ddir=dir_path, force=True, legacy=True)
        print('All Done!')

    # Compile a single file
    def build_file(self, file_path=None):
        if file_path and file_path.endswith('.py'):
            compileall.compile_file(file_path, ddir=file_path, force=True, legacy=True)
        print('Done!')


if __name__ == '__main__':
    pass
    build_pyc = BuildPyc()
    # Default build current project
    build_pyc.build_project()
