import pygame
from config import WHITE, BLACK, GRAY, RED, KEY_WIDTH, BLACK_KEY_WIDTH
from sounds import SOUNDS


class WhiteKey:
    def __init__(self, note, x, width, height):
        self.note = note
        self.rect = pygame.Rect(x, 0, width, height)
        self.color = WHITE
        self.highlight = False
        self.label = pygame.font.SysFont(None, 20).render(note, True, BLACK)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # Outline
        # Draw label
        screen.blit(
            self.label,
            (
                self.rect.x + self.rect.width / 2 - self.label.get_width() / 2,
                self.rect.y + self.rect.height - 20
            )
        )
        if self.highlight:
            pygame.draw.rect(screen, GRAY, self.rect, 4)

    def play_sound(self):
        if self.note in SOUNDS:
            SOUNDS[self.note].play()


class BlackKey:
    def __init__(self, note, x, width, height):
        self.note = note
        self.rect = pygame.Rect(x, 0, width, height)
        self.color = BLACK
        self.highlight = False
        self.label = pygame.font.SysFont(None, 15).render(note, True, WHITE)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, GRAY, self.rect, 2)  # Outline
        # Draw label
        screen.blit(
            self.label,
            (
                self.rect.x + self.rect.width / 2 - self.label.get_width() / 2,
                self.rect.y + self.rect.height - 15
            )
        )
        if self.highlight:
            pygame.draw.rect(screen, RED, self.rect, 3)

    def play_sound(self):
        if self.note in SOUNDS:
            SOUNDS[self.note].play()
