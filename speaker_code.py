import winsound
import random

distance = random.randint(51,400)
print(distance)

if distance <= 400 and distance > 300:
    winsound.PlaySound("APPLAUSE.wav",winsound.SND_FILENAME)
elif distance <= 300 and distance > 200:
    winsound.PlaySound("DRUMROLL.wav", winsound.SND_FILENAME)
elif distance <= 200 and distance > 100:
    winsound.PlaySound("HEARTBEAT.wav", winsound.SND_FILENAME)
elif distance <= 100 and > 50:
    wninsound.PlaySound("10kHZ.wav.wav", winsound.SND_FILENAME)
    
##should be able to connect speaker using bluetooth##
