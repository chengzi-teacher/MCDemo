from mcpi import minecraft
import time
import random

mc = minecraft.Minecraft.create()

bridge = []


def Magic_Bridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if b == 0:
        mc.setBlock(pos.x , pos.y - 1, pos.z , 20)
        coordinate = [pos.x, pos.y - 1, pos.z]
        print(coordinate)
        bridge.append(coordinate)
        mc.postToChat(bridge)
        # mc.postToChat('不安全!')
    elif b != 20:
        if len(bridge) > 0:
            coordinate = bridge.pop(0)
            mc.postToChat(bridge)
            mc.setBlock(coordinate[0] , coordinate[1], coordinate[2], 0)
            time.sleep(0.25)
            # mc.postToChat('安全!')


while True:
    time.sleep(0.25)
    # a = random.randint(1, 3)
    Magic_Bridge()

