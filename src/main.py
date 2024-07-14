# Program to convert input.ass into output.ass for karaoke styled lyrics
import subprocess

# Processes the input and returns the output inside the event section
timestamps = subprocess.check_output(["./times.sh", "input.ass"], text=True)

dialogues = timestamps.splitlines()

output_lines = []
for dialogue in dialogues:
    dialogue = dialogue.split(',')
    start_time = dialogue[1]
    end_time = dialogue[2]
    content = ''.join(dialogue[9:])
    print(start_time, end_time, content)