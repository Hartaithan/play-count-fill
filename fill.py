import os
import time

# START
print('Script started')

# FOCUS MUSIC APP
os.system('''/usr/bin/osascript -e 'tell application "Music" to activate' ''')

# PLAY
os.system('''/usr/bin/osascript -e 'tell application "Music" to play' ''')

# READ PAYLOAD
with open('payload.txt', 'r', encoding='utf-8') as file:
    # LOOP THROUGH PAYLOAD
    for i, line in enumerate(file):
        # FOR EACH ITEM GET PLAY COUNT
        track = line.strip()
        count = int(track)
        print('Current track: ', i, ', Play count: ', count)
        # PLAY TRACK N TIMES
        for i in range(count):
            os.system(
                '''/usr/bin/osascript -e 'tell application "Music" to set player position to (get duration of current track) - 0.5' ''')
            print('Count is set ', i + 1, ' times')
            time.sleep(1)
        # SKIP TO NEXT TRACK
        os.system(
            '''/usr/bin/osascript -e 'tell application "Music" to set song repeat to off' ''')
        os.system(
            '''/usr/bin/osascript -e 'tell application "Music" to next track' ''')
        os.system(
            '''/usr/bin/osascript -e 'tell application "Music" to set song repeat to one' ''')
        time.sleep(1)

# DONE
print('Script finished')
