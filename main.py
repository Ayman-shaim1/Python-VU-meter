import subprocess
import numpy as np
import vlc
import time

AUDIO_FILE = "track1.mp3"
# Audio / VU-meter constants
MAX_INT16 = 32768.0  # Max value for 16-bit audio (for normalisation)
DB_EPSILON = 1e-12  # Small value to avoid log(0)
DB_OFFSET = 60.0  # Shift dB range so -60 dB -> 0
DB_RANGE = 60.0  # dB range used for scaling
VU_MAX_LEVEL = 50.0  # Max value for the VU-meter
VU_GAIN = 1.8  # Extra gain for visual effect


player = vlc.MediaPlayer(AUDIO_FILE)
player.play()
time.sleep(0.3)


decode_time = 0.05
# cmd = "ffmpeg"
cmd = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"


def decode_segment(time_sec, duration=decode_time):
    """Décoder un petit segment audio via FFmpeg."""
    process = subprocess.Popen(
        [
            cmd,
            "-ss",
            str(time_sec),
            "-t",
            str(duration),
            "-i",
            AUDIO_FILE,
            "-f",
            "s16le",
            "-ac",
            "1",
            "-ar",
            "44100",
            "pipe:1",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    raw = process.stdout.read()
    samples = np.frombuffer(raw, dtype=np.int16)

    return samples


def rms(block):
    if block.size == 0:
        return 0
    return np.sqrt(np.mean(block.astype(np.float64) ** 2))


def calculate_audio_level(time_sec, duration=0.05):
    rms_max = 50
    block = decode_segment(player.get_time() / 1000, duration=0.05)
    rms_value = rms(block)
    level = rms_value / rms_max
    level = max(0, min(level, 50))
    return level

# On choisit 3500 parce que c’est le meilleur
# facteur pour transformer des valeurs RMS 16 bits (0 → 3500)
# en un VU-mètre lisible (0 → 50 barres).





while player.is_playing():
    state = player.get_state()
    if state == vlc.State.Ended:
        break

    level = calculate_audio_level(player.get_time() / 1000)

    bar = "█" * int(level)
    print(f"\r[{bar:<50}] {int(level)}", end="")

    time.sleep(decode_time)
