import dask.bag as db  # for paraller computing of large data


# dask.bag is used to pass the data to dask dataframe by filtering and mapping
def load_logs(file_path):
    bag = db.read_text(file_path)
