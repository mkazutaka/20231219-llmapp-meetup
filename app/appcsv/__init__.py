from typing import List
import os
import csv
import numpy as np
from datetime import datetime


def write_any(path: str, name: str, headers: List[str], value: dict):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            csv_headers = ['file', 'bench'] + headers + ['created_at']
            f.write(','.join(csv_headers) + '\n')

    file_name = os.path.splitext(os.path.basename(path))[0]
    with open(path, 'a') as f:
        writer = csv.writer(f)
        row = [file_name, name]
        for header in headers:
            if isinstance(value[header], str):
                value[header] = value[header].replace('\n', '_')
            if isinstance(value[header], float):
                value[header] = round(value[header], 3)
            row.append(value[header])
        row.append(now)
        writer.writerow(row)


def write_score(path: str, name: str, scores: List[float], verbose: bool = True):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write('file,bench,平均,中央値,標準偏差,最小値,最大値,作成日時\n')

    file_name = os.path.splitext(os.path.basename(path))[0]
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(
            [file_name, name, np.mean(scores), np.median(scores), np.std(scores), np.min(scores), np.max(scores), now]
        )
        if verbose:
            print(f"{name}: 平均:{np.mean(scores)}, 中央値: {np.median(scores)}")

