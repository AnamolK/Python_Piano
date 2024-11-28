import pygame

OCTAVES = 3
WHITE_KEYS_PER_OCTAVE = 7
BLACK_KEYS_PER_OCTAVE = 5
TOTAL_WHITE_KEYS = WHITE_KEYS_PER_OCTAVE * OCTAVES
TOTAL_BLACK_KEYS = BLACK_KEYS_PER_OCTAVE * OCTAVES
KEY_WIDTH = 40
KEY_HEIGHT = 200
BLACK_KEY_WIDTH = int(KEY_WIDTH * 0.6)
BLACK_KEY_HEIGHT = int(KEY_HEIGHT * 0.6)
SCREEN_WIDTH = TOTAL_WHITE_KEYS * KEY_WIDTH
SCREEN_HEIGHT = int(KEY_HEIGHT * 1.2)
FPS = 60


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Python Virtual Piano")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

BASE_OCTAVE = 3
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

# Calculate Frequencies for Each Note
NOTE_FREQUENCIES = {}
for octave in range(BASE_OCTAVE, BASE_OCTAVE + OCTAVES):
    for i, note in enumerate(NOTE_NAMES):
        key = f"{note}{octave}"
        # Formula to calculate frequency: 440 * 2^((n - 49)/12)
        # where n is the key number starting from A0 = 1
        # C0 is key number 4, so C3 is key number 40
        n = (octave * 12) + i - 8
        freq = 440 * (2 ** ((n - 49) / 12))
        NOTE_FREQUENCIES[key] = round(freq, 2)

# Define Order of White and Black Keys
WHITE_KEY_NOTES = []
for octave in range(BASE_OCTAVE, BASE_OCTAVE + OCTAVES):
    for note in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
        WHITE_KEY_NOTES.append(f"{note}{octave}")

BLACK_KEY_NOTES = []
for octave in range(BASE_OCTAVE, BASE_OCTAVE + OCTAVES):
    for note in ['C#', 'D#', None, 'F#', 'G#', 'A#', None]:
        if note:
            BLACK_KEY_NOTES.append(f"{note}{octave}")
        else:
            BLACK_KEY_NOTES.append(None)
