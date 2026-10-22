"""
Aggregate the Measuring Hate Speech annotations to one row per comment.
"""
from pathlib import Path

import pandas as pd

# The top-level measuring-hate-speech.parquet is missing the target_politics_* columns
RAW_PATH = Path(__file__).parent / "raw" / "data" / "train-00000-of-00001.parquet"
OUT_DIR = Path(__file__).parent / "clean"

# Ordinal items that feed the continuous hate_speech_score
ORDINAL_COLS = [
    "sentiment",
    "respect",
    "insult",
    "humiliate",
    "status",
    "dehumanize",
    "violence",
    "genocide",
    "attack_defend",
    "hatespeech",
]

if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)
    df = pd.read_parquet(RAW_PATH)
    target_cols = [c for c in df.columns if c.startswith("target_")]

    grouped = df.groupby("comment_id")

    # TODO: Verify these aggregation decisions
    clean = pd.concat(
        [
            grouped[["text", "platform"]].first(),
            # Some scores are exactly -1.0, the library's default mask_value: set ModelConfig(mask_value=...) to e.g. -999
            grouped["hate_speech_score"].mean(),
            grouped[ORDINAL_COLS].mean(),
            # Target identity groups: majority vote across annotators
            (grouped[target_cols].mean() >= 0.5).astype(int),
            grouped.size().rename("n_annotators"),
        ],
        axis=1,
    ).reset_index()

    clean.to_csv(OUT_DIR / "hatespeech.csv", index=False)
