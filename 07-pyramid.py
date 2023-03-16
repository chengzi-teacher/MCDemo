import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z

n =random.randint(20,30)
for i in range(n):
    height = random.randint(7,30)
    x=pos.x + random.randint(-100,100)
    y=pos.y
    z=pos.z + random.randint(-100,100)
    for i in range(height,-1,-1):
        mc.setBlocks(x + i, y + height - i, z + i, x - i, y + height - i, z - i, 41)
y=mc.getHeight(pos.x,pos.z)
mc.player.setTilePos(pos.x,y,pos.z)
