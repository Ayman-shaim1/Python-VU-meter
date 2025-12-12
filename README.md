# Python VU Meter (Audio Decoder)

A real-time audio visualizer that displays a VU (Volume Unit) meter while playing an audio file. This project uses VLC for audio playback and FFmpeg for real-time audio decoding to provide live audio level visualization in the terminal.

## Features

- Real-time audio playback using VLC media player
- Live VU meter visualization in the terminal
- RMS (Root Mean Square) audio level calculation
- Low-latency audio segment decoding via FFmpeg
- Visual bar representation of audio levels (0-50 bars)

## Requirements

### System Requirements
- Python 3.x
- FFmpeg installed on your system and accessible in PATH (or update the path in `main.py`)
- Windows/Linux/macOS compatible

### Python Dependencies
- `numpy` - For audio data processing and RMS calculations
- `python-vlc` - For audio playback control

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg:**
   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use a package manager like Chocolatey
   - **Linux:** `sudo apt-get install ffmpeg` (Ubuntu/Debian) or `sudo yum install ffmpeg` (CentOS/RHEL)
   - **macOS:** `brew install ffmpeg`

4. **Configure FFmpeg path (if needed):**
   - If FFmpeg is not in your system PATH, update the `cmd` variable in `main.py` with the full path to your FFmpeg executable
   - Example: `cmd = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"`

5. **Prepare your audio file:**
   - Place your audio file named `track1.mp3` in the project directory
   - Or modify the `AUDIO_FILE` variable in `main.py` to point to your audio file

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Start playing the audio file using VLC
2. Display a real-time VU meter in the terminal showing audio levels
3. Update the meter every 10ms (0.01 seconds) for smooth visualization
4. Continue until the audio playback ends

### Example Output
```
[██████████████████████████████████████████████████] 50
```

## How It Works

1. **Audio Playback:** VLC media player handles the audio playback
2. **Real-time Decoding:** FFmpeg decodes small audio segments (50ms) at the current playback position
3. **RMS Calculation:** The decoded audio samples are converted to RMS values to measure audio levels
4. **Visualization:** RMS values are scaled (divided by 300) and displayed as a bar graph (0-50 bars)
5. **Continuous Loop:** The process repeats every 10ms while the audio is playing

### Technical Details

- **Audio Format:** Decoded as 16-bit signed little-endian PCM, mono channel, 44.1kHz sample rate
- **RMS Scaling Factor:** 300 (optimized for 16-bit audio values ranging 0-32000)
- **Update Rate:** 10ms intervals (100 updates per second) for smooth visualization
- **Segment Duration:** 50ms audio segments for decoding
- **Initial Delay:** 100ms delay after starting playback to ensure audio is ready

## Configuration

You can customize the following in `main.py`:

- `AUDIO_FILE`: Path to your audio file (default: `"track1.mp3"`)
- `cmd`: Path to FFmpeg executable (default: `"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"` for Windows)
- `duration`: Audio segment duration in seconds for `decode_segment()` function (default: `0.01`)
- Segment duration in main loop: Currently set to `0.05` seconds (line 67)
- `time.sleep()`: Update interval in main loop (default: `0.01` seconds)

## Code Structure

- `decode_segment(time_sec, duration)`: Decodes a small audio segment at the specified time position
- `rms(block)`: Calculates the Root Mean Square value of audio samples
- Main loop: Continuously monitors playback position and updates the VU meter display

## Notes

- The VU meter displays levels from 0 to 50 bars
- The scaling factor of 300 is optimized for 16-bit audio samples (0 → 32000) to create a readable VU meter (0 → 50 bars)
- Ensure FFmpeg is properly installed and accessible
- The script requires the audio file to exist in the specified location
- The visualization updates at 100 Hz (every 10ms) for smooth real-time display

## License

This project is open source and available for personal and educational use.
