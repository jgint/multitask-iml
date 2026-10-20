"""
Combine the CAP party manifesto/platform files into one sentence-level dataset.
See notes.md for the issues handled here.
"""
from pathlib import Path

import pandas as pd
from ftfy import fix_text

RAW_DIR = Path(__file__).parent / "raw"
OUT_DIR = Path(__file__).parent / "clean"

# CAP master major topics; 0 = no policy content
VALID_MAJORTOPICS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23}
COLUMNS = ["doc_id", "country", "party", "year", "text", "majortopic", "subtopic"]


def load_uk():
    df = pd.read_csv(RAW_DIR / "uk_manifestos_v1__1.csv", encoding="cp1252")
    party_cols = {"filter_con": "con", "filter_lab": "lab", "filter_ld": "ld", "filter_ukip": "ukip"}
    df["party"] = df[list(party_cols)].idxmax(axis=1).map(party_cols)
    df["country"] = "uk"
    df["text"] = df["description"]
    df["doc_id"] = "uk_" + df["party"] + "_" + df["year"].astype(str)
    return df


def load_irl():
    df = pd.read_csv(RAW_DIR / "irl_manifestos_data_1981_2020_utf8.csv")
    # 99 = no policy content in the Irish codebook; 0 elsewhere
    df[["majortopic", "subtopic"]] = df[["majortopic", "subtopic"]].replace(99, 0)
    df["party"] = df["party"].astype(str)
    df["country"] = "irl"
    # election_in_year separates the Feb and Nov 1982 elections
    df["doc_id"] = (
        "irl_" + df["party"] + "_" + df["year"].astype(str) + "_" + df["election_in_year"].astype(str)
    )
    return df


def load_us(file_name, party):
    df = pd.read_csv(RAW_DIR / file_name)
    # Use the CAP master codes, not pap_majortopic/pap_subtopic (US Policy Agendas codes)
    df["party"] = party
    df["country"] = "us"
    df["text"] = df["description"]
    df["doc_id"] = "us_" + party + "_" + df["year"].astype(str)
    return df


if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)
    df = pd.concat(
        [
            load_uk()[COLUMNS],
            load_irl()[COLUMNS],
            load_us("Dem_partyplatform_20.2.csv", "dem")[COLUMNS],
            load_us("US-Party-Rep_Platform_19.3_0.csv", "rep")[COLUMNS],
        ],
        ignore_index=True,
    )

    # Fix mojibake (Irish and US files) and normalise whitespace
    df["text"] = df["text"].astype(str).map(fix_text).str.split().str.join(" ")

    # Drop empty text, and -555 / blank / out-of-scheme topic codes
    df["majortopic"] = pd.to_numeric(df["majortopic"], errors="coerce")
    df = df[(df["text"] != "") & (df["text"] != "nan") & df["majortopic"].isin(VALID_MAJORTOPICS)]
    df = df.astype({"majortopic": int, "subtopic": int})

    df.to_csv(OUT_DIR / "cap_manifestos.csv", index=False)
