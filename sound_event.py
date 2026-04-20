import pygame

class SoundEvent:
    def __init__(self, file, trigger, start_time, volume=1.0, delay=0, loop=False):

        self.sound = pygame.mixer.Sound(file)
        self.sound.set_volume(volume)

        self.trigger = trigger
        self.start_time = start_time
        self.delay = delay
        self.loop = loop

        self.played = False
        self.channel = None

    def update(self, current_time):
        if self.played:
            return
        if self.trigger == "start"and not self.played:
            self.play()

        elif self.trigger == "delay":
            if current_time - self.start_time >= self.delay:
                self.play()

    def play(self):
        loops = -1 if self.loop else 0
        self.channel = self.sound.play(loops=loops)
        self.played = True

    def stop(self):
        if self.channel:
            self.channel.stop()

    def trigger_play(self):
        self.played = False
        self.play()