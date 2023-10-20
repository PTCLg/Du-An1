# import time

# # Đoạn mã 1
# start_time = time.time()
# # Chèn đoạn mã 1 tại đây

# print("Thời gian chạy của đoạn mã 1: %s giây" % (time.time() - start_time))

# # Đoạn mã 2
# start_time = time.time()
# # Chèn đoạn mã 2 tại đây

# print("Thời gian chạy của đoạn mã 2: %s giây" % (time.time() - start_time))

import os
import cachetools
from pathlib import Path
from mutagen.mp3 import MP3
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

def find_mp3_files(cache, path):
    base_path = Path(path)
    for entry in base_path.rglob('*.mp3'):
        if entry.is_file():
            audio = MP3(entry)
            if audio.info.length > 60 and entry.stat().st_size > 120:
                yield cache.setdefault(entry.name, str(entry))

def list_drives():
    drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
    return drives

def main():
    """Chạy chương trình."""
    cache = cachetools.TTLCache(maxsize=100, ttl=60)
    paths = list_drives()

    with ThreadPoolExecutor() as executor:
        future_to_path = {executor.submit(find_mp3_files, cache, path): path for path in paths}
        for future in concurrent.futures.as_completed(future_to_path):
            mp3_files = future.result()
            for mp3_file in mp3_files:
                print(mp3_file)

if __name__ == "__main__":
    main()