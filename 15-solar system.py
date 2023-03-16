import mcpi.minecraft
import mcpi.minecraftstuff
import time

mc = mcpi.minecraft.Minecraft.create()
mcdrawing = mcpi.minecraftstuff.MinecraftDrawing(mc)

wool = 35
glass = 20
pos = mc.player.getTilePos()
x = pos.x
y = pos.y + 70
z = pos.z + 25


def buildSphere(x, y, z, r, id, data):
    mcdrawing.drawSphere(x, y, z, r, id, data)

def buildHorizontalCircle(x, y, z, r, id):
    mcdrawing.drawHorizontalCircle(x, y, z, r, id)


solar = [[0, 20, 14], [30, 3, 8], [44, 5, 4], [62, 4, 11], [80, 4, 8], [108, 10, 1], [146, 9, 4], [180, 8, 3],
         [212, 8, 9]]

for star in solar:
    buildSphere(x + star[0], y, z, star[1], wool, star[2])
    buildHorizontalCircle(x, y, z, star[0], glass)
    time.sleep(1)
