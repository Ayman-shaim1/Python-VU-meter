import subprocess
import numpy as np
import vlc
import time

AUDIO_FILE = "track1.mp3"

player = vlc.MediaPlayer(AUDIO_FILE)
player.play()
time.sleep(0.1)


# cmd = "ffmpeg"
cmd = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"

def decode_segment(time_sec, duration=0.01):
    """Décoder un petit segment audio via FFmpeg."""
    process = subprocess.Popen(
        [
            cmd,
            "-ss", str(time_sec),
            "-t", str(duration),
            "-i", AUDIO_FILE,
            "-f", "s16le",
            "-ac", "1",
            "-ar", "44100",
            "pipe:1"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
    raw = process.stdout.read()
    samples = np.frombuffer(raw, dtype=np.int16)

    return samples

def rms(block):
    if block.size == 0:
        return 0
    return np.sqrt(np.mean(block.astype(np.float64)**2))


#-----------------------------------------------------------------------------
# On choisit 300 parce que c’est le meilleur
# facteur pour transformer des valeurs RMS 16 bits (0 → 32000) 
# en un VU-mètre lisible (0 → 50 barres).
#-----------------------------------------------------------------------------

# rms_max = 300 
# block = decode_segment(22, duration=0.05)
# rms_value = rms(block)
# print("rms_value", rms_value)
# level = rms_value / rms_max
# level = max(0, min(level, 50))
# print(level)



while player.is_playing():
    state = player.get_state()
    if state == vlc.State.Ended:
        break

    # position VLC en secondes
    pos_sec = player.get_time() / 1000

    block = decode_segment(pos_sec, duration=0.05)

    level = rms(block) / 300
    level = max(0, min(level, 50))

    bar = "█" * int(level)
    print(f"\r[{bar:<50}] {int(level)}", end="")
    time.sleep(0.01)
