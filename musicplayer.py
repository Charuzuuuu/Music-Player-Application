import pygame

# Initialize pygame mixer
pygame.mixer.init()

print("\n\n\n=========== OPENING APP ===========\n\n")

# List of music files
playlist = [
    'Diviners - Savannah.mp3',
    'Elektronomia - Sky High.mp3',
    'Itro & Tobu - Cloud 9.mp3',
    'Jim Yosef - Link.mp3',
    'Lost Sky - Dreams.mp3'
]

# Current track index
current_track = 0

# 1 = Playing / 0 = Not Playing / 2 = Inactive State
status = 0

# 1 = Shuffled / 0 - Not Shuffled
shuffle = 0

# 1 = Loop / 0 - Not Looping
loop = 0

def load_track(index):
    pygame.mixer.music.load(playlist[index])

def display_menu():
    print("\nMusic Player Menu:")
    print("1. Play")
    print("2. Pause")
    print("3. Stop")
    print("4. Next")
    print("5. Previous")
    print("6. Shuffle")
    print("7. Repeat")
    print("8. Exit")

def handle_input(choice):
    global current_track, status, shuffle, loop
    if choice == 1:
        pygame.mixer.music.play()
        print("\n\n=========== Playing ===========\n")
        status = 1
    elif choice == 2:
        if status == 1:
            pygame.mixer.music.pause()
            print("\n\n=========== Paused ===========\n")
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 3:
        if status == 1:
            pygame.mixer.music.stop()
            print("\n\n=========== Stop Playing ===========\n")
            status = 2
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 4:
        if status == 1:
            current_track = (current_track + 1) % len(playlist)
            load_track(current_track)
            print("\n\n=========== Next Song ===========\n")
            pygame.mixer.music.play()
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 5:
        if status == 1:
            current_track = (current_track - 1) % len(playlist)
            load_track(current_track)
            print("\n\n=========== Previous Song ===========\n")
            pygame.mixer.music.play()
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 6:
        if status == 1:
            if shuffle == 0:
                shuffle = 1
                print("\n\n=========== Song Shuffle ===========\n")
            else:
                shuffle = 0
                print("\n\n=========== Off Shuffle ===========\n")
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 7:
        if status == 1:
            if loop == 0:
                loop = 1
                print("\n\n=========== Song Looped ===========\n")
            else:
                loop = 0
                print("\n\n=========== Off Loop ===========\n")
        elif status == 2:
            print("\n\n=========== Inactive State ===========\n")
        else:
            print("\n\n=========== Dead State ===========\n")
    elif choice == 8:
        pygame.mixer.music.stop()
        print("\n\n=========== Closing App... ===========\n")
        return False
    return True

load_track(current_track)
running = True
while running:
    display_menu()
    try:
        choice = int(input("Choose an option: "))
        if 1 <= choice <= 8:
            running = handle_input(choice)
        else:
            print("\n\n=========== Please choose a number between 1 and 8. ===========\n")
    except ValueError:
        print("\n\n=========== Please enter a valid number. ===========\n")

pygame.mixer.quit()
