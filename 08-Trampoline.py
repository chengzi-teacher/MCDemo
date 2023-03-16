import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
x,y,z=mc.player.getTilePos()

side =40

mc.setBlocks(x,y-1,z,x+side,y+side,z+side,20)
mc.setBlocks(x+1,y-1,z+1,x+side-1,y+side,z+side-1,0)
mc.setBlocks(x,y-1,z,x+side,y-1,z+side,165)
mc.player.setTilePos(x+side//2,y+side//2,z+side//2)
while True:
    x2,y2,z2 = mc.player.getTilePos()
    slime = mc.getBlock(x2, y2 - 1, z2)
    if slime==165:
        mc.player.setTilePos(x2, y + 100, z2)
        time.sleep(2)
