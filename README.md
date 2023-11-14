# TalkingDragons: Audio Transcription with Whisper

TalkingDragons Bash script utilizes the Whisper speech recognition model to transcribe MP3 files in a specific folder. It creates a transcription file for each MP3 file if it doesn't already exist.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/talkingdragons.git
    ```

2. Navigate to the script directory:

    ```bash
    cd talkingdragons
    ```

3. Run the script, providing the input folder as an argument:

    ```bash
    ./transcribe.sh /path/to/your/input/folder
    ```

## Installation

Ensure you have the Whisper executable installed. You can follow the installation instructions provided by the [OpenAI Whisper GitHub](https://github.com/openai/whisper).

## Configuration

Set the script parameters as needed:

* `WHISPER_EXECUTABLE`: whisper executable
* `MODEL_SIZE`: Model Size (e.g "tiny");
* `LANGUAGE`: Model Language (e.g "pt");

Check whisper documentation for more information regarding available models and languages.

## Dependencies

- Python 3.11
- PyTorch
- OpenAI's tiktoken
- Whisper

Teste using MacOS Ventura


## Origin of the Name

The name "TalkingDragons" is inspired by the cultural significance of the Dragão do Mar Cultural Center in Ceará, Brazil, 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.