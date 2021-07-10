import gc
from random import randint

import pygame


class Sound:
    def __init__(self):
        print("Started Sound class...")
        self.BLOCKS_SOUND = {}
        self.SOUNDS = {}
        self.MUSIC = []
        self.MENU_MUSIC = []
        self.music_already_playing = False

        self.musicPlayer = pygame.mixer.music

        self.volume = 1

    def startMusic(self, t):
        self.musicPlayer.stop()
        del self.musicPlayer
        self.musicPlayer = pygame.mixer.music

        if t:
            musicNum = randint(0, len(self.MUSIC) - 1)
            self.musicPlayer.load(self.MUSIC[musicNum])
            for i in range(len(self.MUSIC)):
                if i == musicNum:
                    continue
                self.musicPlayer.queue(self.MUSIC[i])
        else:
            musicNum = randint(0, len(self.MENU_MUSIC) - 1)
            self.musicPlayer.load(self.MENU_MUSIC[musicNum])
            for i in range(len(self.MENU_MUSIC)):
                if i == musicNum:
                    continue
                self.musicPlayer.queue(self.MENU_MUSIC[i])
        gc.collect

    def playSound(self, name, volume):
        channel = self.SOUNDS[name].play()
        channel.set_volume(volume)
        gc.collect

    def playGuiSound(self, st):
        if st == "click":
            channel = self.SOUNDS["GUI"]["click_stereo"][0].play()
            channel.set_volume(self.volume)
        gc.collect

    def playMusic(self):
        if self.music_already_playing:
            return
        if randint(0, 5000) == 746:
            self.music_already_playing = True
            self.musicPlayer.play()
            self.musicPlayer.set_volume(self.volume)
        gc.collect
