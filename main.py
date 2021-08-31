import os, time, subprocess, signal

print("**script**: starting web")
time.sleep(1)
print("**script**: flask server running")
time.sleep(1)
print("**script**: starting ngrok tcp")
os.system('ngrok tcp -region us 5000 &')