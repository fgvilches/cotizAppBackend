import os, time, subprocess, signal

print("**script**: starting web")
time.sleep(1)
os.system('flask run &')
print("**script**: flask server running")
