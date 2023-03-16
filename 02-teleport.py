import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create(address="192.168.0.103")

x,y,z=mc.player.getTilePos()#获得角色当前坐标,将坐标数据给到变量x,y,z
mc.postToChat("x:"+str(x)+"y:"+str(y)+"z:"+str(z))#发送当前坐标到游戏聊天框
mc.player.setTilePos(x+20,y,z+100)#改变坐标
time.sleep(1)#等待一秒
x,y,z=mc.player.getTilePos()#再次获得角色当前坐标,将改变后的坐标数据给到变量x,y,z
mc.postToChat("x:"+str(x)+"y:"+str(y)+"z:"+str(z))


