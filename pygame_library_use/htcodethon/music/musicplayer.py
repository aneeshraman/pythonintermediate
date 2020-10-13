from pygame import mixer

# Initialize the mixer function
mixer.init()

# Loading the music so that we can play it. Please remember to save music.mp3 file in the same folder.
mixer.music.load("music.mp3")

# Setting the music volume. The volume can be set from 0 to 1 where 0 is no sound and 1 is the maximum sound.
mixer.music.set_volume(1)

# Playing the music
mixer.music.play()

while True:
    # These are the conditions which are being displayed on the run console. These sat that 'p' is to pause the music,
    # 'r' is to resume the music and 'e' is to exit the program
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    # Making a query variable which would take the input and would help us in giving the right output.
    query = input("Choose any of the above options ")

    # When the user presses 'p' to pause the music.
    if query == 'p':
        # This is to pause the music when 'p' is pressed.
        mixer.music.pause()

    # When the user presses 'r' to resume the music.
    elif query == 'r':
        # This is to unpause (resume) the music.
        mixer.music.unpause()

    # When the user presses 'e' to exit the music.
    elif query == 'e':
        # This is to stop the music. 
        mixer.music.stop()
        break
