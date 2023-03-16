import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.168.0.153",name="sans")
mc.postToChat('hello world')
