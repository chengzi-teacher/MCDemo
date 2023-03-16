import mcpi.minecraft as minecraft
import time

mc=minecraft.Minecraft.create()

water=9
f_water=8
ice=79

while True:
    # pos = mc.player.getTilePos()
    # x=pos.x
    # y=pos.y
    # z=pos.z
    x,y,z=mc.player.getTilePos()

    block=mc.getBlock(x,y-1,z)
    block1 = mc.getBlock(x + 1, y - 1, z)
    block2 = mc.getBlock(x - 1, y - 1, z)
    block3 = mc.getBlock(x , y - 1, z+1)
    block4 = mc.getBlock(x, y - 1, z - 1)
    if block == 11 or block==10:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,ice)
    if block1 == water or block1==f_water:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,ice)
    if block2 == water or block2==f_water:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,ice)
    if block3 == water or block3==f_water:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,ice)
    if block4 == water or block4==f_water:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,ice)
    time.sleep(0.1)


