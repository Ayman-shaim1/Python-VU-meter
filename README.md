# Python VU Meter (Audio Decoder)

A real-time audio visualizer that displays a VU (Volume Unit) meter while playing an audio file. This project uses VLC for audio playback and FFmpeg for real-time audio decoding to provide live audio level visualization in the terminal.

## Features

- Real-time audio playback using VLC media player
- Live VU meter visualization in the terminal
- RMS (Root Mean Square) audio level calculation
- Low-latency audio segment decoding via FFmpeg
- Visual bar representation of audio levels (0-50 bars)
- Configurable decode time for fine-tuning performance

## Requirements

### System Requirements
- Python 3.x
- FFmpeg installed on your system and accessible in PATH (or update the path in `main.py`)
- Windows/Linux/macOS compatible

### Python Dependencies
- `numpy` - For audio data processing and RMS calculations
- `python-vlc` - For audio playback control

Install dependencies:
```bash
pip install -r requirements.txt
```

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
   - Or uncomment `cmd = "ffmpeg"` if FFmpeg is in your PATH

5. **Prepare your audio file:**
   - Place your audio file named `track1.mp3` in the project directory
   - Or modify the `AUDIO_FILE` variable in `main.py` to point to your audio file
   - Supported formats: MP3, WAV, and other formats supported by FFmpeg

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Start playing the audio file using VLC
2. Wait 100ms for the audio to initialize
3. Display a real-time VU meter in the terminal showing audio levels
4. Update the meter every 20ms (0.02 seconds) - 50 updates per second
5. Continue until the audio playback ends

### Example Output
```
[██████████████████████████████████████████████████] 50
```

The VU meter displays:
- A bar graph using filled blocks (█) representing the audio level
- A numeric value (0-50) showing the current level
- Real-time updates as the audio plays

## How It Works

1. **Audio Playback:** VLC media player handles the audio playback
2. **Real-time Decoding:** FFmpeg decodes small audio segments (20ms) at the current playback position
3. **RMS Calculation:** The decoded audio samples are converted to RMS values to measure audio levels
4. **Visualization:** RMS values are scaled (divided by 300) and displayed as a bar graph (0-50 bars)
5. **Continuous Loop:** The process repeats every 20ms while the audio is playing

### Technical Details

- **Audio Format:** Decoded as 16-bit signed little-endian PCM, mono channel, 44.1kHz sample rate
- **RMS Scaling Factor:** 300 (optimized for 16-bit audio values ranging 0-32000 to create a readable VU meter with 0-50 bars)
- **Update Rate:** 20ms intervals (50 updates per second)
- **Segment Duration:** 20ms audio segments for decoding (configurable via `decode_time` variable)
- **Initial Delay:** 100ms delay after starting playback to ensure audio is ready

## Configuration

You can customize the following variables in `main.py`:

- `AUDIO_FILE`: Path to your audio file (default: `"track1.mp3"`)
- `decode_time`: Duration for audio segment decoding and update interval in seconds (default: `0.02` = 20ms)
- `cmd`: Path to FFmpeg executable (default: `"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"` for Windows)
  - Uncomment `cmd = "ffmpeg"` if FFmpeg is in your system PATH

### Adjusting Performance

- **Lower `decode_time`** (e.g., 0.01): More frequent updates, smoother visualization, higher CPU usage
- **Higher `decode_time`** (e.g., 0.05): Less frequent updates, lower CPU usage, less smooth visualization

## Code Structure

### Functions

- `decode_segment(time_sec, duration)`: Decodes a small audio segment at the specified time position using FFmpeg
  - Parameters:
    - `time_sec`: Time position in seconds
    - `duration`: Duration of the segment to decode (defaults to `decode_time`)
  - Returns: NumPy array of 16-bit signed integer audio samples

- `rms(block)`: Calculates the Root Mean Square value of audio samples
  - Parameters:
    - `block`: NumPy array of audio samples
  - Returns: RMS value as a float (0 if block is empty)

### Main Loop

The main loop:
1. Checks if the player is still playing
2. Gets the current playback position in seconds
3. Decodes the audio segment at that position
4. Calculates the RMS value
5. Scales and clamps the level (0-50)
6. Displays the VU meter
7. Sleeps for `decode_time` seconds before the next iteration

## Project Files

- `main.py` - Main application script
- `requirements.txt` - Python dependencies
- `track1.mp3`, `track2.mp3`, `track3.wav` - Sample audio files
- `workflow.png` - Workflow diagram (if available)

## Notes

- The VU meter displays levels from 0 to 50 bars
- The scaling factor of 300 is optimized for 16-bit audio samples (0 → 32000) to create a readable VU meter (0 → 50 bars)
- Ensure FFmpeg is properly installed and accessible
- The script requires the audio file to exist in the specified location
- The visualization updates at 50 Hz (every 20ms) for real-time display
- The decode time and update interval are synchronized for optimal performance

## Troubleshooting

- **FFmpeg not found:** Make sure FFmpeg is installed and the path in `main.py` is correct
- **No audio playback:** Check that the audio file exists and VLC is properly installed
- **VU meter not updating:** Verify that the audio file is playing and FFmpeg can decode it
- **Performance issues:** Try increasing `decode_time` to reduce CPU usage

## License

This project is open source and available for personal and educational use.
