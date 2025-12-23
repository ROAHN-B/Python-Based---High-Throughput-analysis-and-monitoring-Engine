import dask.bag as db  # for paraller computing of large data
from parser import parse_log_line
from schema.schema import LOG_SCHEMA


# dask.bag is used to pass the data to dask dataframe by filtering and mapping
def load_logs(file_path):
    bag = db.read_text(file_path)

    parsed = bag.map(parse_log_line).filter(lambda x: x is not None)
    df = parsed.to_dataframe()
    return df.df.astype(LOG_SCHEMA)
