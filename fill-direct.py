import subprocess

script = """
tell application "Music"
    set played count of current track to 10
end tell
"""

process = subprocess.Popen(
    ['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, stderr = process.communicate(script.encode())
