import mcpi.minecraft
import time

gold = 41
mc = mcpi.minecraft.Minecraft.create()
x,y,z = mc.player.getTilePos()

box ={}
def turnStone():
    events = mc.events.pollBlockHits()
    if events:
        e = events[0]
        mc.postToChat(e)
        block = mc.getBlock(e.pos)
        mc.postToChat(block)
        pos = tuple(e.pos)
        if pos not in box:
            box[pos] = block
            mc.setBlock(pos, gold)
            print(box)
        else:
            mc.setBlock(pos, box[pos])
            del box[pos]
            print(box)

while True:
    turnStone()
    time.sleep(0.1)

