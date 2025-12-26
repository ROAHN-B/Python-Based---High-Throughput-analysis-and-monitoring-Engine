import dask.bag as db
from ingestion.parser import parse_log_line
from schema.schema import LOG_SCHEMA
import pandas as pd


def load_logs(file_path):
    bag = db.read_text(file_path)
    parsed = bag.map(parse_log_line).filter(lambda x: x is not None)

    # Debug first
    sample_data = parsed.take(3)
    print("Sample data:", sample_data)

    if len(sample_data) == 0:
        print("No data was parsed!")
        return pd.DataFrame()

    # Create DataFrame with explicit meta
    meta = pd.DataFrame(
        {
            "timestamp": pd.Series([], dtype="datetime64[ns]"),
            "level": pd.Series([], dtype="string"),
            "service_level": pd.Series([], dtype="string"),
            "message": pd.Series([], dtype="string"),
        }
    )

    df = parsed.to_dataframe(meta=meta)
    return df.astype(LOG_SCHEMA)
