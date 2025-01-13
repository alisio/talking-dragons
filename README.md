# TalkingDragons: Batch Audio Transcription with Whisper

TalkingDragons Bash script utilizes the Whisper speech recognition model to transcribe all ffmpeg compatible audio and video files in a specific folder. It creates a transcription txt file for each media file if it doesn't already exist.


![dragao_do_mar](./images/dragao_do_mar.png)

The name "TalkingDragons" is inspired by the cultural significance of the Dragão do Mar. "Dragão do Mar, or 'Sea Dragon,' is the honored name of Francisco José do Nascimento, an Afro-Brazilian jangadeiro and abolitionist, who courageously led a strike in 1881, refusing to transport enslaved individuals in Fortaleza, ultimately contributing to the abolition of slavery in Ceará, Brazil in 1884."

For more information regarding Francisco José do Nascimento checkout his [wikipedia article](https://en.wikipedia.org/wiki/Dragão_do_Mar)

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
    ./talkingdragons.sh /path/to/your/input/folder
    ```

## Installation

Ensure you have the Whisper executable installed. You can follow the installation instructions provided by the [OpenAI Whisper GitHub](https://github.com/openai/whisper).

## Configuration

Set the script parameters as needed:

* `WHISPER_EXECUTABLE`: whisper executable
* `MODEL_SIZE`: Model Size (default: "base");
* `LANGUAGE`: Model Language (default: "pt");

Check whisper documentation for more information regarding available models and languages.

## Dependencies

- Python 3.11
- PyTorch
- OpenAI's tiktoken
- Whisper

Tested using MacOS Ventura

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
