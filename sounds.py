import numpy as np
import pygame
from config import NOTE_FREQUENCIES


SOUNDS = {}


def generate_sine_wave(freq, duration=1.0, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(freq * t * 2 * np.pi)


    attack = int(0.01 * sample_rate)
    decay = int(0.02 * sample_rate)
    sustain = len(wave) - attack - decay
    envelope = np.ones_like(wave)
    envelope[:attack] *= np.linspace(0, 1, attack)
    envelope[attack:attack + sustain] *= 1
    envelope[attack + sustain:] *= np.linspace(1, 0, decay)
    wave = wave * envelope

    # Normalize to 16-bit Range
    audio = wave * (2 ** 15 - 1) * volume
    return audio.astype(np.int16).tobytes()


def initialize_pygame_mixer():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()
    for note, freq in NOTE_FREQUENCIES.items():
        sound_wave = generate_sine_wave(freq)
        SOUNDS[note] = pygame.mixer.Sound(buffer=sound_wave)
