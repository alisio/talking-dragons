# TalkingDragons: Batch Audio Transcription


The **TalkingDragons** project is a Python-based solution designed to batch transcribe audio and video files within a specified folder using OpenAI's Whisper speech recognition model. It processes all ffmpeg-compatible media files, generating a transcription `.txt` file for each, and ensures backups of existing transcription files to avoid overwriting.


![dragao_do_mar](./images/dragao_do_mar.png)

The name "TalkingDragons" is inspired by the cultural significance of the Dragão do Mar. "Dragão do Mar, or 'Sea Dragon,' is the honored name of Francisco José do Nascimento, an Afro-Brazilian jangadeiro and abolitionist, who courageously led a strike in 1881, refusing to transport enslaved individuals in Fortaleza, ultimately contributing to the abolition of slavery in Ceará, Brazil in 1884."

For more information regarding Francisco José do Nascimento checkout his [wikipedia article](https://en.wikipedia.org/wiki/Dragão_do_Mar)

---

## Key Features

- **Batch Processing**: Automatically transcribes multiple audio and video files in a specified directory.
- **Whisper Integration**: Utilizes OpenAI's Whisper model for state-of-the-art speech recognition.
- **Automatic Backup**: Backs up existing transcription files with incremental numeric suffixes starting from `001`.
- **Detailed Reporting**: Provides a summary report including transcription time, language detected, and model used.
- **Language and Model Selection**: Supports automatic language detection or user-specified input, with customizable Whisper models.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alisio/talking-dragons.git
   ```

2. **Navigate to the Script Directory**:
   ```bash
   cd talkingdragons
   ```

3. **Install Dependencies**:
   Ensure Python 3.7 or later is installed, and run:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the Python script from the command line:

```bash
python whisper_transcription.py <inputs> [--language <language>] [--model <model>]
```

### Arguments
- `<inputs>`: One or more files or directories containing media files to transcribe.
- `--language`: (Optional) Specify the language of the audio. If omitted, the script will detect it automatically.
- `--model`: (Optional) Specify the Whisper model to use (default: `base`).

### Example

```bash
python whisper_transcription.py /path/to/media/files --language en --model large
```

---

## Configuration

The following parameters can be customized within the script or passed as arguments:

- **Language**: Detects automatically or can be set explicitly using `--language`.
- **Model**: Use the `--model` flag to specify the Whisper model size (e.g., `tiny`, `base`, `large`).

---

## Output

- Transcriptions are saved as `.txt` files in the same directory as the input files.
- Existing transcription files are backed up with incremental suffixes (e.g., `_backup_001`).
- A detailed report is generated at the end, showing:
  - Transcription time per file
  - Total processing time
  - Model used
  - Language detected
  - Output file paths

---

## Dependencies

- Python 3.7 or later
- whisper
- tqdm
- ffmpeg (installed on your system)

Install Python dependencies via:

```bash
pip install whisper tqdm
```

Ensure `ffmpeg` is installed and available in your system's PATH. For installation instructions, refer to the [FFmpeg documentation](https://ffmpeg.org/download.html).

---

## Cultural Inspiration

This project draws inspiration from the "Dragão do Mar" (Sea Dragon), honoring Francisco José do Nascimento, an Afro-Brazilian jangadeiro and abolitionist who played a pivotal role in the abolition of slavery in Ceará, Brazil, in 1884.

---

## License

This project is licensed under the MIT License. For more details, see the [LICENSE.md](LICENSE.md) file in the repository.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the project.

