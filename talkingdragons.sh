#!/bin/bash

# Path to the Whisper executable
WHISPER_EXECUTABLE="whisper"

# Model size and language
MODEL_SIZE="tiny"
LANGUAGE="pt"

# Check if the correct number of arguments has been provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_folder>"
    exit 1
fi

# Set the input folder from the command-line argument
INPUT_FOLDER="$1"

# Check if the Whisper executable is available
if ! command -v $WHISPER_EXECUTABLE &> /dev/null; then
    echo "Whisper executable not found. Please make sure it is installed and in your PATH."
    exit 1
fi

# Loop through each MP3 file in the input folder
for mp3_file in "$INPUT_FOLDER"/*.mp3; do
    # Check if the transcription file already exists
    transcript_file="${mp3_file%.mp3}.transcript.txt"
    if [ -e "$transcript_file" ]; then
        echo "Transcription file already exists for $mp3_file. Skipping."
    else
        # Transcribe the MP3 file using the tiny Portuguese model
        $WHISPER_EXECUTABLE "$mp3_file" --model "$MODEL_SIZE" --language "$LANGUAGE" > "$transcript_file"
        echo "Transcription of $mp3_file completed. Transcript saved to $transcript_file"
    fi
done

echo "Transcription process completed."
