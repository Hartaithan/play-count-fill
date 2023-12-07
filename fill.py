import os
import time


def run_script(command):
    """
    This function runs the given osascript command.
    """
    os.system(
        f"/usr/bin/osascript -e 'tell application \"Music\" to {command}'")


# START
print('Script started')

# FOCUS MUSIC APP
run_script('activate')

# PLAY
run_script('play')

# READ PAYLOAD
with open('payload.txt', 'r', encoding='utf-8') as file:
    # LOOP THROUGH PAYLOAD
    for i, line in enumerate(file):
        # FOR EACH ITEM GET PLAY COUNT
        track = line.strip()
        count = int(track)
        print('Current track:', i, ', Play count:', count)
        # PLAY TRACK N TIMES
        for i in range(count):
            run_script(
                'set player position to (get duration of current track) - 0.5')
            print('Count is set', i + 1, 'times')
            time.sleep(1)
        # SKIP TO NEXT TRACK
        run_script('set song repeat to off')
        run_script('next track')
        run_script('set song repeat to one')
        time.sleep(1)

# DONE
print('Script finished')
