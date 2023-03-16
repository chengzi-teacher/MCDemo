import mcpi.minecraft as minecraft
import time,random

mc = minecraft.Minecraft.create()
r = int(input("请输入海洋池范围半径： "))
air = 0
while 1:
    pos = mc.player.getTilePos()
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            for z in range(-r,r+1):
                if x**2+y**2 +z**2<= 3**2:
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,air)
                elif x**2 + y**2 + z**2 <= r**2:
                    glass,color =95,random.randint(0,15)
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,glass,color)
    time.sleep(0.5)

