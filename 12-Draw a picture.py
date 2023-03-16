import mcpi.minecraft
import mcpi.block as block

mc = mcpi.minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

list_a = [[0,1,1,0],[1,1,1,1],[0,1,1,0],[0,1,1,0]]
for i in range(4):
    for j in range(4):
    #     print(list_a[i][j],end=" ")
    # print()
        if list_a[i][j] == 1:
            mc.setBlock(x+i,y,z+j,block.STONE.id)
        else:
            mc.setBlock(x+i,y,z+j,block.AIR.id)