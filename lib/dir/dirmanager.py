import os
import time

task_name = "python.exe"
os.system(f"taskkill /f /fi \"imagename eq {task_name}\"")

time.sleep(1)

path = os.getcwd()
os.startfile(path + "//waveloader.py")