import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
x,y,z = mc.player.getTilePos() #使用getTilePos()方法获取玩家位置，再把位置数据给变量。

#建造起始基地
mc.setBlocks(x,y-1,z,x+10,y+10,z+10,block.GLASS.id)
mc.setBlocks(x+1,y-1,z+1,x+10,y+9,z+9,block.AIR.id)

#建造结束基地
mc.setBlocks(x+142,y+99,z,x+132,y+109,z+10,block.GLASS.id)
mc.setBlocks(x+141,y+100,z+1,x+132,y+108,z+9,block.AIR.id)

#建造铁路
for i in range(21):
    mc.setBlock(x+1+i,y-1,z+4,block.GLASS.id)
    mc.setBlock(x+1+i,y-1,z+6,block.GLASS.id)
    mc.setBlock(x + 1 + i, y - 1, z + 5, 152)
    mc.setBlock(x + 1 + i, y , z + 5, 27)

for i in range(101):
    mc.setBlock(x+21+i,y-1+i,z+4,block.GLASS.id)
    mc.setBlock(x+21+i,y-1+i,z+6,block.GLASS.id)
    mc.setBlock(x + 21 + i, y - 1 + i, z + 5, 152)
    mc.setBlock(x + 21 + i, y + i , z + 5, 27)

for i in range(20):
    mc.setBlock(x+122+i,y+99,z+4,block.GLASS.id)
    mc.setBlock(x+122+i,y+99,z+6,block.GLASS.id)
    mc.setBlock(x + 122 + i, y+99 , z + 5, 152)
    mc.setBlock(x + 122 + i, y +100 , z + 5, 27)



