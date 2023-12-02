import os
# import pyautogui

# START
print('Script started')

# FOCUS MUSIC APP
os.system('''/usr/bin/osascript -e 'tell application "Music" to activate' ''')
os.system(
    '''/usr/bin/osascript -e 'tell application "System Events" to keystroke "f" using {control down, command down}' ''')

# PLAY
os.system('''/usr/bin/osascript -e 'tell application "Music" to play' ''')

# READ PAYLOAD
with open('payload.txt', 'r', encoding='utf-8') as file:
    # LOOP THROUGH PAYLOAD
    for line in file:
        print(line.strip())
        # FOR EACH ITEM REPEAT N TIMES MOUSE CLICK ON LAST SECOND OF THE TIMELINE
        # pyautogui.moveTo(1343,915)

# DONE
print('Script finished')
