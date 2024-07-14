### Karaoke ASS File Converter

This program converts `input.ass` files into `output.ass` files for karaoke-styled lyrics. The conversion process includes reading the content of the `input.ass` file, retrieving and processing the dialogues, and writing the transformed content into `output.ass`.

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