import winsound
import random

distance = random.randint(101,400)
print(distance)

if distance <= 400 and distance > 300:
    winsound.PlaySound("APPLAUSE.wav",winsound.SND_FILENAME)
elif distance <= 300 and distance > 200:
    winsound.PlaySound("DRUMROLL.wav", winsound.SND_FILENAME)
elif distance <= 200 and distance > 100:
    winsound.PlaySound("HEARTBEAT.wav", winsound.SND_FILENAME)

