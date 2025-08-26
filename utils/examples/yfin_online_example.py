from pathlib import Path
import sys
import os
import dotenv

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_YFin_data_online

# Load environment variables from .env
dotenv.load_dotenv()
DATA_DIR = os.getenv("DATA_DIR")

def main() -> None:
    # Example usage: fetch AAPL data from 2024-01-01 to 2024-03-01
    symbol = "AAPL"
    start_date = "2024-01-01"
    end_date = "2024-03-01"

    try:
        result_csv_with_header = get_YFin_data_online(symbol, start_date, end_date)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Print to console
    print(result_csv_with_header)

    # Save to DATA_DIR from .env
    if DATA_DIR is None:
        print("DATA_DIR is not set in .env file.")
        return

    data_dir_path = Path(DATA_DIR)
    data_dir_path.mkdir(parents=True, exist_ok=True)

    outfile = data_dir_path / f"{symbol}-YFin-online-{start_date}-{end_date}.csv"
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(result_csv_with_header)

    print(f"Saved output to: {outfile}")


if __name__ == "__main__":
    main() 