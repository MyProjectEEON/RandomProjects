import keyboard
import time
import random

delay = 150

start = time.time()
     
while True:
    if time.time() - start > delay:
        for i in range(0, 150):
            keyboard.block_key(i)

        keyboard.press("t")
        time.sleep(0.05)
        keyboard.write("/warp " + str(random.randint(0, 1000000000)))
        time.sleep(0.05)
        keyboard.press("enter")
        time.sleep(0.05)
        keyboard.press("t")
        time.sleep(0.05)
        keyboard.write("/teleport jackoneleg Skygolem_")
        time.sleep(0.05)
        keyboard.press("enter")
        time.sleep(0.05)
        
        for i in range(0, 150):
            keyboard.unblock_key(i)

        start = time.time()


