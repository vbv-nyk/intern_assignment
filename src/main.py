# Program to convert input.ass into output.ass for karaoke styled lyrics
"""
High level overview of the algorithm:
Read content from input.ass
Retrieve the content in the event section
Transform the data 
Write content to output.ass
"""

import subprocess

# Processes the input and returns the output inside the event section
timestamps = subprocess.check_output(["./times.sh", "input.ass"], text=True)

dialogues = timestamps.splitlines()


def remove_templates(content):
    modified_content = content.replace("{\\rH}", "")
    modified_content = modified_content.replace("{\\r}", "")
    return modified_content


lyrics = []
for i, dialogue in enumerate(dialogues):
    n = len(lyrics)
    dialogue = dialogue.split(',')
    content = ''.join(dialogue[9:])
    modified_content = remove_templates(content)
    if n > 0 and lyrics[n - 1] == modified_content: continue
    lyrics.append(modified_content)

lyrics_pointer = 0
for i, dialogue in enumerate(dialogues):
    dialogue = dialogue.split(',')
    subtitle = remove_templates(''.join(dialogue[9:]))
    if lyrics_pointer < len(lyrics) and subtitle == lyrics[lyrics_pointer]:
        lyrics_pointer += 1

    previous_dialogue = dialogue[0:9]
    previous_dialogue[3] = 'P'
    previous_dialogue = ','.join(previous_dialogue)
    previous_dialogue += lyrics[lyrics_pointer - 2] if lyrics_pointer > 1 else ',...'

    current_dialogue = dialogue
    current_dialogue[3] = 'Default'
    current_dialogue = ','.join(current_dialogue)

    next_dialogue = dialogue[0:9]
    next_dialogue[3] = 'F'
    next_dialogue = ','.join(next_dialogue)
    next_dialogue += lyrics[lyrics_pointer] if lyrics_pointer < len(lyrics) else ',...'

    print(f'{previous_dialogue}\n{current_dialogue}\n{next_dialogue}\n')
