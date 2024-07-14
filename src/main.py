# Program to convert input.ass into output.ass for karaoke styled lyrics
"""
High level overview of the algorithm:
1) Read content from input.ass
2) Retrieve the content in the event section
3) Get the lyrics of the entire karaoke
4) Start conversion showing previous line and next line
5) Write content to output.ass
"""

import subprocess

"""
Algorithm: To retrieve the dialogues present in input.ass
input: input.ass
output: dialogues array containing the different lines of the karaoke lyrics
1) Use awk to retrieve the content in the event section
2) Split the text at new line and store it inside dialogues
"""
def init_input():
    timestamps = subprocess.check_output(["./times.sh", "input.ass"], text=True)
    dialogues = timestamps.splitlines()
    return dialogues

"""
Algorithm: To clean the input from {\rH} and {\r}
input: A line from the dialogue
output: Dialogue without the {\r} and {\rH}
"""
def remove_templates(content):
    modified_content = content.replace("{\\rH}", "")
    modified_content = modified_content.replace("{\\r}", "")
    return modified_content

"""
Algorithm to insert the flags F, P and Default into the dialogue during conversion
input: Array dialogue (split at ',')
output: String dialogue after inserting the flag and joining
"""
def transform_input(dialogue, flag):
   dialogue[3] = flag 
   dialogue = ','.join(dialogue)
   return dialogue

"""
Algorithm to retrieve the entire lyrics
Input: Array of lines of lyrics
Output: Array of lines of lyrics, where adjacent elements are not the same and are cleaned from the templates
"""
def get_lyrics(dialogues):
    lyrics = []
    for i, dialogue in enumerate(dialogues):
        n = len(lyrics)
        dialogue = dialogue.split(',')
        content = ''.join(dialogue[9:])
        modified_content = remove_templates(content)
        if n > 0 and lyrics[n - 1] == modified_content: continue
        lyrics.append(modified_content)
    return lyrics

"""
Algorithm to transform the subtitles to karaoke
Input: The dialogues from the input.ass and lyrics after get_lyrics()
Output: output.ass containing the desired result in karaoke style
"""
def transform_result(dialogues, lyrics):
    lyrics_pointer = 0
    result = ""
    for i, dialogue in enumerate(dialogues):
        dialogue = dialogue.split(',')
        subtitle = remove_templates(''.join(dialogue[9:]))
        
        # If lyrics pointer is pointing to the same element as the subtitle, move the pointer forward
        if lyrics_pointer < len(lyrics) and subtitle == lyrics[lyrics_pointer]:
            lyrics_pointer += 1

        previous_dialogue = transform_input(dialogue[0:9], 'P')
        previous_dialogue += lyrics[lyrics_pointer - 2] if lyrics_pointer > 1 else ',...'

        current_dialogue = transform_input(dialogue, 'Default')

        next_dialogue = transform_input(dialogue[0:9], 'F')
        next_dialogue += lyrics[lyrics_pointer] if lyrics_pointer < len(lyrics) else ',...'

        result += (f'{previous_dialogue}\n{current_dialogue}\n{next_dialogue}\n\n')
    return result

def create_output(result):
    open('output.ass', 'w').write(result)

dialogues = init_input()
lyrics = get_lyrics(dialogues)
result = transform_result(dialogues, lyrics)

create_output(result)