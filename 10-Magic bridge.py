from mcpi import minecraft
import time
import random

mc = minecraft.Minecraft.create()

def Magic_Bridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if b == 0:
        mc.setBlocks(pos.x-5, pos.y-1, pos.z-5,pos.x+5, pos.y-1, pos.z+5, a)
        # mc.postToChat('不安全!')
    # else:
    #     mc.postToChat('安全!')

    time.sleep(0.1)

while True:
    a = random.randint(1, 4)
    Magic_Bridge()


