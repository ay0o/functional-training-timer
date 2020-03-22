import argparse
import time
import pygame


def parse_args():
    parser = argparse.ArgumentParser(description='Functional Training Timer',
                                     usage='python ftt.py -n WORKOUTS -t TIME -r REST')
    required = parser.add_argument_group('required_arguments')
    required.add_argument('-n', help='Number of workouts', action='store', required=True, type=int)
    required.add_argument('-t', help='Time per workout', action='store', required=True, type=int)
    required.add_argument('-r', help='Rest time between workouts', action='store', required=True, type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    workouts = args.n
    workout_time = args.t
    rest_time = args.r

    pygame.mixer.init()
    countdown = pygame.mixer.Sound('sounds/countdown.wav')
    beep = pygame.mixer.Sound('sounds/beep.wav')
    start = pygame.mixer.Sound('sounds/start.wav')
    end = pygame.mixer.Sound('sounds/end.wav')

    countdown.play()
    time.sleep(5)
    for i in range(1, workouts + 1):
        start.play()
        print(f'Workout: {i}')
        time.sleep(workout_time)
        # Don't play beep nor wait rest time on last workout
        if i < workouts:
            beep.play()
            time.sleep(rest_time)

    end.play()
    time.sleep(2)


if __name__ == '__main__':
    main()
