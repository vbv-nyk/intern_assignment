#!/bin/bash
cp input_subtitles.ass src/input.ass
cd src && python3 main.py
cp output.ass ../output_subtitles.ass
