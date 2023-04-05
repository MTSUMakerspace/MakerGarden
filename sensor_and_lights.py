import os
import time

cmnd1 = "sudo python3 sparkle.py &"
cmnd2 = "sudo python3 sprinkle.py"

#os.system(cmnd1)

for i in range(3):
    os.system(cmnd2)
    time.sleep(3)

