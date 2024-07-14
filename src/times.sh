#!/bin/bash

# Uses awk to retrieve all the dialogues
INPUT=$(cat $1)

# Extract all lines containing "Dialogue"
DIALOGUES=$(awk -F ',' '/Dialogue/ {print}' "$1")


echo "$DIALOGUES"