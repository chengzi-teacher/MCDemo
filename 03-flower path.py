import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
# mc.postToChat("before loop")
while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat("x=" + str(x) + " y=" + str(y) + " z=" + str(z))
    flower = 51
    mc.setBlock(x,y,z,flower)
    mc.setBlock(x+1, y, z, 46)
    time.sleep(0.2)
