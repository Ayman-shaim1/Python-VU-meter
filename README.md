# Python Vu Meter (Audio Decoder)

A simple real-time audio visualizer that displays a VU meter while playing an audio file.

## What it does

- Plays an audio file (`track1.mp3`) using VLC
- Continuously decodes small audio segments using FFmpeg
- Calculates RMS (Root Mean Square) values to measure audio levels
- Displays a real-time visual VU meter with bars showing the current audio level

## Requirements

- Python 3
- `python-vlc` library
- `numpy`
- FFmpeg installed on your system

## Usage

```bash
python main.py
```

The script will play the audio file and show a live VU meter in the terminal.
