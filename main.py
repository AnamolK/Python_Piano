import pygame
from config import (
    SCREEN, GRAY, WHITE_KEY_NOTES, BLACK_KEY_NOTES,
    KEY_WIDTH, BLACK_KEY_WIDTH, KEY_HEIGHT, BLACK_KEY_HEIGHT, FPS
)
from keys import WhiteKey, BlackKey
from sounds import initialize_pygame_mixer
from mapping import KEYBOARD_MAPPING


def main():
    pygame.init()
    initialize_pygame_mixer()

    # Create White Keys
    white_keys = []
    current_x = 0
    for note in WHITE_KEY_NOTES:
        key = WhiteKey(note, current_x, KEY_WIDTH, KEY_HEIGHT)
        white_keys.append(key)
        current_x += KEY_WIDTH

    # Create Black Keys
    black_keys = []
    for i, note in enumerate(BLACK_KEY_NOTES):
        if note is not None:
            # Position black keys between white keys
            x = (i + 1) * KEY_WIDTH - (BLACK_KEY_WIDTH / 2)
            key = BlackKey(note, x, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)
            black_keys.append(key)

    clock = pygame.time.Clock()
    running = True

    while running:
        SCREEN.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Check Black Keys First
                for key in black_keys:
                    if key.rect.collidepoint(pos):
                        key.play_sound()
                        key.highlight = True
                        break
                else:
                    # Then Check White Keys
                    for key in white_keys:
                        if key.rect.collidepoint(pos):
                            key.play_sound()
                            key.highlight = True
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                for key in black_keys + white_keys:
                    key.highlight = False

            elif event.type == pygame.KEYDOWN:
                if event.key in KEYBOARD_MAPPING:
                    note = KEYBOARD_MAPPING[event.key]
                    for key in black_keys:
                        if key.note == note:
                            key.play_sound()
                            key.highlight = True
                            break
                    else:
                        for key in white_keys:
                            if key.note == note:
                                key.play_sound()
                                key.highlight = True
                                break

            elif event.type == pygame.KEYUP:
                if event.key in KEYBOARD_MAPPING:
                    note = KEYBOARD_MAPPING[event.key]
                    for key in black_keys:
                        if key.note == note:
                            key.highlight = False
                            break
                    else:
                        for key in white_keys:
                            if key.note == note:
                                key.highlight = False
                                break

        # Draw White Keys First
        for key in white_keys:
            key.draw(SCREEN)

        # Draw Black Keys on Top
        for key in black_keys:
            key.draw(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
