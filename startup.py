import sys
import os


current_path = sys.path[0]
os.popen("cd " + current_path)
os.popen("venv\\Scripts\\activate.bat")
for line in os.popen("py.test -v --html=test_result\\login.html"):
    print(line, end='')
