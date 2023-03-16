import mcpi.minecraft as minecraft
import time, random

gold, diamond, green, black = 41, 57, 133, 49
gems= [gold, diamond, green]
mc = minecraft.Minecraft.create()
def turnGold():
    events = mc.events.pollBlockHits()
    if events:
        print(events)
        e = events[0]
        mc.postToChat(e)
        block = mc.getBlock(e.pos)
        mc.postToChat(block)
        if block in gems:
            mc.setBlock(e.pos, black)
        else:
            mc.setBlock(e.pos, random.choice(gems))
while True:
    turnGold()
    time.sleep(0.1)