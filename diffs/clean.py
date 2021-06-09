import os
import os.path

for dr in os.listdir():
    if dr == 'clean.py':
        continue
    for file in os.listdir(dr):
        if file == 'diff_info.json':
            continue
        path = os.path.join(dr, file)
        os.remove(path)
