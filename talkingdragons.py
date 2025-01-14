import os
import sys
import argparse
from pathlib import Path
import whisper
from tqdm import tqdm
import time

"""
Script Name: talkingdragons.py
Description: This script uses the Whisper library to transcribe audio or video files, supports backup of existing transcriptions, and generates a detailed report.
Author: Alisio Meneses
Date: 2025-01-12
Version: 2.0
Usage: python talkingdragons.py <inputs> [--language <language>] [--model <model>]

Dependencies:
- Python 3.7 or later
- whisper
- tqdm

Features:
- Automatic transcription using Whisper.
- Supports individual files, multiple files, and directories.
- Detects or accepts input language.
- Backs up existing transcriptions with incremental suffixes starting from 001.
- Generates a detailed summary report including time, language, and output file details.
"""

def backup_existing_file(file_path):
    """
    Creates a backup of an existing file by adding an incremental numeric suffix, starting at 001.

    Args:
        file_path (Path): Path of the existing file.

    Returns:
        None
    """
    counter = 1
    while True:
        backup_path = file_path.with_stem(f"{file_path.stem}_backup_{counter:03}")
        if not backup_path.exists():
            file_path.rename(backup_path)
            print(f"Backup created: {backup_path}")
            break
        counter += 1

def transcribe_file(file_path, model, language, output_folder, report):
    """
    Transcribes a single audio/video file using the Whisper library.

    Args:
        file_path (str): Path of the file to be transcribed.
        model (whisper.Whisper): Loaded Whisper model.
        language (str): Audio language (or None for automatic detection).
        output_folder (str): Folder where the transcription will be saved.
        report (dict): Dictionary to store transcription details for reporting.

    Returns:
        None
    """
    try:
        print(f"Transcribing: {file_path}")
        start_time = time.time()
        result = model.transcribe(str(file_path), language=language)
        transcription = result['text']
        duration = time.time() - start_time

        # Create the output file name
        output_file = Path(output_folder) / (Path(file_path).stem + "_transcription.txt")

        # Backup the existing file if necessary
        if output_file.exists():
            backup_existing_file(output_file)

        # Write the transcription to the file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcription)

        print(f"Transcription saved to: {output_file}")

        # Add to report
        report[file_path.name] = {
            "time": duration,
            "output_file": str(output_file),
            "language": result.get('language', 'unknown')
        }

    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")

def generate_report(report, total_time, model, language):
    """
    Generates a summary report of the transcription process.

    Args:
        report (dict): Details of each file's transcription.
        total_time (float): Total time for all transcriptions.
        model (str): Whisper model used.
        language (str): Language used or detected.

    Returns:
        None
    """
    print("\n--- Transcription Report ---")
    print(f"Model: {model}")
    print(f"Language: {language if language else 'Auto-detected'}")
    print(f"Total Time: {total_time:.2f} seconds")
    print("\nFile Details:")
    for file_name, details in report.items():
        print(f"  {file_name}: {details['time']:.2f} seconds, Output: {details['output_file']}, Language: {details['language']}")
    print("----------------------------")

def main():
    parser = argparse.ArgumentParser(description="Script for transcribing files using Whisper.")
    parser.add_argument("inputs", nargs="+", help="File(s) or folder containing files to be transcribed.")
    parser.add_argument("--language", type=str, default=None, help="Audio language. If not specified, it will be detected automatically.")
    parser.add_argument("--model", type=str, default="base", help="Whisper model to be used. Default: 'base'.")

    args = parser.parse_args()

    # Load the Whisper model
    print(f"Loading model '{args.model}'...")
    model = whisper.load_model(args.model)

    # Identify the files to be transcribed
    files_to_transcribe = []
    for input_path in args.inputs:
        path = Path(input_path)
        if path.is_file():
            files_to_transcribe.append(path)
        elif path.is_dir():
            files_to_transcribe.extend(path.glob("**/*"))
        else:
            print(f"Invalid input: {input_path}")

    # Filter compatible files
    supported_formats = {".mp3", ".mp4", ".wav", ".m4a", ".flac", ".aac"}
    files_to_transcribe = [file for file in files_to_transcribe if file.suffix.lower() in supported_formats]

    if not files_to_transcribe:
        print("No valid files found for transcription.")
        sys.exit(1)

    # Transcribe files and collect report data
    report = {}
    total_start_time = time.time()

    for file_path in tqdm(files_to_transcribe, desc="Transcribing files"):
        transcribe_file(file_path, model, args.language, file_path.parent, report)

    total_time = time.time() - total_start_time

    # Generate and print report
    generate_report(report, total_time, args.model, args.language)

if __name__ == "__main__":
    main()
