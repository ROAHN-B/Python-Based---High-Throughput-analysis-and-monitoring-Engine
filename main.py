# [timestamp] [log_level][module][message]  --> structure of log
# which will be feeded to the analyzer
# Table headings timestamp, log_level, module, message
from config.dask_config import start_dask

if __name__ == "__main__":
    Client = start_dask()
    print(Client)
