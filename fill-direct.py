import csv
import subprocess


def run_script(scr):
    """
    This function runs the given osascript script.
    """
    process = subprocess.Popen(
        ['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.communicate(scr.encode())


with open('playlist.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        title = row['Название']
        played_count = row['Воспроизведено']

        set_counts = f"""
        tell application "Music"
            set song repeat to off
            set played count of current track to {played_count}
            next track
        end tell
        """
        run_script(set_counts)
