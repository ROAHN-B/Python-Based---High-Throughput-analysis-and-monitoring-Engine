# [timestamp] [log_level][module][message]  --> structure of log
# which will be feeded to the analyzer
# Table headings timestamp, log_level, module, message

from config.dask_config import start_dask
from ingestion.loader import load_logs

if __name__ == "__main__":
    Client = start_dask()
    df = load_logs(r"data\sample_log.log")
    print("Dask Client started: ", Client)
    print(df)
