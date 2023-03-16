import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc=minecraft.Minecraft.create(address="192.168.0.117")
pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

for a in range(0,10):
    c1=random.randint(0,15)
    c2=random.randint(0,15)
    mc.setBlocks(x + 1, y, z + 1, x + 5, y + 3, z + 5, 35, c1)
    mc.setBlocks(x - 1, y, z - 5, x + 5, y + 3, z - 9, 35, c2)
    x+=6
