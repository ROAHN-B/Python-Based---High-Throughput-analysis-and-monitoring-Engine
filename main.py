# [timestamp] [log_level][module][message]  --> structure of log
# which will be feeded to the analyzer
# Table headings timestamp, log_level, module, message
from config.dask_config import start_dask

if __name__ == "__main__":
    client = start_dask()

    print("=" * 60)
    print("DASK CLIENT STARTED")
    print("=" * 60)
    print(f"Client: {client}")
    print(f"Dashboard link: {client.dashboard_link}")
    print("=" * 60)
    input("**Enter any key to exit**")
