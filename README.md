### Karaoke ASS File Converter

This program converts `input.ass` files into `output.ass` files for karaoke-styled lyrics. The conversion process includes reading the content of the `input.ass` file, retrieving and processing the dialogues, and writing the transformed content into `output.ass`.

### How to Run the Program

1. Place your input in `input_subtitle.ass` file in the root directory.
2. Ensure you have the `run.sh` script with the following content (Already inside the root directory):
    ```bash
    #!/bin/bash
    cp input_subtitles.ass src/input.ass
    cd src && python3 main.py
    cp output.ass ../output_subtitles.ass
    ```
3. Make the `run.sh` script executable:
    ```bash
    chmod +x run.sh
    ```
4. Run the script:
    ```bash
    ./run.sh
    ```
5. Your converted `output.ass` file will be saved as `output_subtitles.ass` in the same directory.

### Notes
- The `run.sh` script copies `input_subtitles.ass` to `src/input.ass`, runs the conversion script, and then copies the resulting `output.ass` back to `output_subtitles.ass`.
- Make sure your `input_subtitle.ass` file is correctly named and placed in the appropriate directory (project root directory) before running the script.
### Overview

The program performs the following steps:
- Reads content from `input.ass`.
- Retrieves the content in the event section.
- Extracts and cleans the lyrics of the entire karaoke.
- Transforms the lyrics, showing the previous, current, and next lines.
- Writes the transformed content to `output.ass`.

### Algorithm Details

#### Step 1: Retrieve Dialogues

- **Input:** `input.ass`
- **Output:** Array of dialogues containing the different lines of the karaoke lyrics.
- **Method:** Uses `awk` to retrieve the content in the event section, splits the text at new lines, and stores it in dialogues.

#### Step 2: Clean Input

- **Input:** A line from the dialogue.
- **Output:** Dialogue without `{\r}` and `{\rH}`.
- **Method:** Replaces `{\r}` and `{\rH}` with an empty string.

#### Step 3: Insert Flags

- **Input:** Array dialogue (split at ',').
- **Output:** String dialogue after inserting the flag and joining.
- **Method:** Updates the flag in the dialogue and joins the parts back into a string.

#### Step 4: Retrieve Lyrics

- **Input:** Array of lines of lyrics.
- **Output:** Array of lines of lyrics, cleaned from the templates and without adjacent duplicates.
- **Method:** Cleans the content, removes duplicates, and returns the lyrics.

#### Step 5: Transform Subtitles to Karaoke

- **Input:** The dialogues from `input.ass` and lyrics after `get_lyrics()`.
- **Output:** `output.ass` containing the desired result in karaoke style.
- **Method:** Adds previous, current, and next lines to the dialogue and forms the karaoke style output.