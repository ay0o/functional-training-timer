import pygame
import time


pygame.mixer.init()
countdown = pygame.mixer.Sound('sounds/countdown.wav')
beep = pygame.mixer.Sound('sounds/beep.wav')
start = pygame.mixer.Sound('sounds/start.wav')
end = pygame.mixer.Sound('sounds/end.wav')

exercises = int(input("Number of exercises: "))
duration = int(input("Duration of each exercise (in seconds): "))
rounds = int(input("Number of rounds: "))
if rounds > 1:
    rest_time = int(input("Rest time (in seconds): "))

for i in range(1, rounds + 1):
    countdown.play()
    time.sleep(5)
    print("Round {} starts!".format(str(i)))
    start.play()
    for j in range(1, exercises + 1):
        time.sleep(duration)
        print("Exercise {} finished".format(str(j)))
        # Play a beep for change of exercise. If last one, beep won't be played
        if j < exercises:
            beep.play()
    end.play()
    print("Round {} over!\n".format(str(i)))
    if i < rounds:
        time.sleep(rest_time)
    else:
        # 2 secs delay at the end to hear the end sound.
        time.sleep(2)
