# Python VU-Meter

A simple VU-meter (volume meter) that uses **VLC** for audio playback and **FFmpeg** for decoding and analyzing audio levels.

## Features

- **Audio playback** with VLC Player
- **Audio decoding** with FFmpeg
- **Real-time display** of a VU-meter in the console
- Level calculation in **dBFS** (decibels Full Scale)
- Visual progress bar

## Prerequisites

- Python 3.x
- VLC Media Player installed
- FFmpeg installed at `C:\Program Files\ffmpeg\bin\ffmpeg.exe`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Place your audio file in the `audios/` folder (e.g., `audios/track1.mp3`)
2. Modify the `AUDIO_FILE` variable in `main.py` if needed
3. Make sure the `FFMPEG_PATH` matches your FFmpeg installation
4. Run the script:

```bash
python main.py
```

## How It Works

1. **VLC** plays the audio file for sound output
2. **FFmpeg** decodes the same audio file in real-time and sends raw data through a pipe
3. The script analyzes each audio block (50ms) to calculate:
   - The **RMS** (Root Mean Square) level
   - Conversion to **dBFS**
4. The VU-meter displays in the console with a progress bar

## Configuration

In `main.py`, you can modify:

- `AUDIO_FILE`: Path to your audio file
- `SAMPLE_RATE`: Sample rate (default 44100 Hz)
- `BLOCK_DURATION`: Duration of each analysis block (default 0.05s = 50ms)
- `FFMPEG_PATH`: Path to the FFmpeg executable
- `DB_MIN`: Minimum displayed level in dB (default -60 dB)

## Stop

Press `Ctrl+C` to stop playback and the VU-meter.
