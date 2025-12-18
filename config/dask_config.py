# Business is written here!
from dask.distributed import LocalCluster, Client


def start_dask():
    cluster = LocalCluster(n_workers=2, thread_per_workers=3, memory_limit=2)
    return Client(cluster)


# client is method how python connects dask cluster(Connection between client and cluster)
# local cluster is mini distributed cluster, installed in our local system
# n_workers ---> chunks
# Threads per worker if n_workers = 2 , then task will be 2X2
# memory limit---> "1GB" works when data is greater than 10 TB
# Send task to worler with the help of client and process easily.
