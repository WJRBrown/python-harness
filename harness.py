import argparse
import os
import time
import sys
import importlib
from tests import TestRunner

def command_line_args():
    parser = argparse.ArgumentParser(description='Run the Test Harness against a root directory of tests and target webpage', usage='python3 harness.py -r /path/to/tests')
    parser.add_argument("-r", action = "store", help = "Test root directory", dest = "root")
    parser.add_argument("-t", action = "store", help = "Target webpage", dest = "target", default=None)
    
    return parser.parse_args()

def find_test_list(root_path):
    file_paths = []
    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            if "test" in file:
                file_paths.append(os.path.join(subdir, file))
    return sorted(file_paths)

class Harness():
    def __init__(self, root_path, target_page):
        self.runner = TestRunner(root_path, target_page)
        self.tests = find_test_list(root_path)
        self.current_test = None
        self.root_path = root_path
        self.target_page = target_page
    
    def load_test(self):
        global Module
        global module_name
        dir_name = os.path.dirname(self.current_test)
        base_name = os.path.basename(self.current_test)
        module_name = os.path.splitext(base_name)[0]
        print(module_name)
        sys.path.append(dir_name)
        Module = importlib.import_module(module_name)
        try:
            return True
        except:
            # set error
            # report failure
            return False
        
    def execute_commands(self):
        if hasattr(Module, "Run"):
            try:
                test_result = Module.Run(self.runner)
                time.sleep(2)
                if test_result:
                    print("Pass!")
                else:
                    print("Fail!")
            except:
                print("Fail")
                return False
        else:
            print("'Run' function not found")
            return False
        return test_result
    
    def run_test(self):
        self.load_test()
        self.execute_commands()
        
    def run_all_tests(self):
        for test in self.tests:
            self.current_test = test
            self.run_test()
            if self.runner.message:
                print(self.runner.message)
            else:
                pass
        
if __name__ == "__main__":
    args = command_line_args()
    Harness = Harness(args.root, args.target)
    Harness.run_all_tests()
