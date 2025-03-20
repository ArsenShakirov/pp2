import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
folder = 'folder'

if not os.path.exists(folder) or not os.listdir(folder):
    print("Error: Folder does not exist or contains no music files.")
    pygame.quit()
    exit()

music_list = [song for song in os.listdir(folder) if song.endswith('.mp3')]
if not music_list:
    print("Error: No MP3 files found in the folder.")
    pygame.quit()
    exit()

index = 0
runtime = True
is_playing = True

song = os.path.join(folder, music_list[index])
pygame.mixer.music.load(song)
pygame.mixer.music.play()

clock = pygame.time.Clock()

while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runtime = False

            elif event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing

            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                index = (index + 1) % len(music_list)
                song = os.path.join(folder, music_list[index])
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                index = (index - 1) % len(music_list)
                song = os.path.join(folder, music_list[index])
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
