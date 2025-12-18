import vlc
import subprocess
import numpy as np
import math
import time
import sys

# =============================
# CONFIGURATION
# =============================
AUDIO_FILE = "audios/track1.mp3"   # chemin vers ton audio
SAMPLE_RATE = 44100
BLOCK_DURATION = 0.05      # 50 ms
BLOCK_SIZE = int(SAMPLE_RATE * BLOCK_DURATION)
MAX_INT16 = 32768
DB_MIN = -60
FFMPEG_PATH = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
# =============================
# VLC PLAYER (LECTURE AUDIO)
# =============================
vlc_instance = vlc.Instance("--no-video")
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(AUDIO_FILE)


player.set_media(media)

player.play()
time.sleep(0.5)  # laisser VLC démarrer

# =============================
# FFMPEG (DÉCODAGE AUDIO)
# =============================
ffmpeg_cmd = [
    FFMPEG_PATH,
    "-i", AUDIO_FILE,
    "-f", "s16le",
    "-ac", "1",
    "-ar", str(SAMPLE_RATE),
    "pipe:1"
]

ffmpeg = subprocess.Popen(
    ffmpeg_cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
)

# =============================
# AUDIO CALCULS
# =============================
def rms(samples):
    return np.sqrt(np.mean(samples.astype(np.float64) ** 2))

def dbfs(rms_value):
    if rms_value <= 0:
        return DB_MIN
    return max(DB_MIN, 20 * math.log10(rms_value / MAX_INT16))

def draw_vu(db):
    width = 50
    level = int((db - DB_MIN) / abs(DB_MIN) * width)
    level = max(0, min(width, level))
    bar = "█" * level + "-" * (width - level)
    sys.stdout.write(f"\r🎚️ [{bar}] {db:6.1f} dBFS")
    sys.stdout.flush()

# =============================
# MAIN LOOP
# =============================
print("▶️ Lecture VLC + VU-mètre en cours (Ctrl+C pour arrêter)")

try:
    while True:
        if not player.is_playing():
            time.sleep(0.05)
            continue

        raw = ffmpeg.stdout.read(BLOCK_SIZE * 2)
        if not raw:
            break

        samples = np.frombuffer(raw, dtype=np.int16)
        r = rms(samples)
        db = dbfs(r)
        draw_vu(db)

        time.sleep(BLOCK_DURATION)

except KeyboardInterrupt:
    pass

# =============================
# CLEAN EXIT
# =============================
print("\n⏹️ Arrêt")
player.stop()
ffmpeg.terminate()
