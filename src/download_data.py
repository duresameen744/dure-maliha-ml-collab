from pathlib import Path
from sklearn.datasets import fetch_openml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "adult.csv"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df = fetch_openml("adult", version=2, as_frame=True).frame
    df.to_csv(OUT, index=False)
    print(f"Saved {len(df)} rows to {OUT}")

if __name__ == "__main__":
    main()