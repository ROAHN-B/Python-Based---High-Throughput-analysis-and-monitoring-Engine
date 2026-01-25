# from config.dask_config import start_dask
# from ingestion.loader import load_logs
# from ingestion.parser import parse_log_line
# from processing.pipeline import build_pipeline
# import time
# import dask.dataframe as df
# from anomaly.detecter import detect_anomaly
# from config.email_config import send_mail
from fastapi import FastAPI
from backend.router import service

app = FastAPI()

# user_mail = "rohanbelsare113@gmail.com"
# def main():
    # client = start_dask()
    # print(client)
    # print(f"Dashboard link: {client.dashboard_link}")
    # print("\n" + "=" * 50)

    # start = time.time()
    # log_df = build_pipeline(r"data\sample_log.log")
    # print(log_df.tail())
    # print("start time:", start)

    # total_logs = log_df.count().compute()
    # end = time.time()

    # print("Running Anomaly detection...")
    # anomalies_df = detect_anomaly(log_df)

    # # anomalies = anomalies_df.compute()
    # anomalies = anomalies_df

    # if anomalies.empty:
    #     print("No anomalies detected")
    # else:
    #     print(f"🚨 {len(anomalies)} anomalies detected!")

    #     for _, row in anomalies.iterrows():
    #         anomaly_data = {
    #             "timestamp": row["timestamp"],
    #             "error_count": row["error_count"],
    #             "z_score": row["z_score"],
    #         }

    #         send_mail(to_email=user_mail, anomaly=anomaly_data)

    #         print(
    #             f"📧 Alert sent | Time: {row['timestamp']} | "
    #             f"Errors: {row['error_count']}"
    #         )

    # input("\nPress Enter to exit...")

app.include_router(service.router)
# if __name__ == "__main__":
#     main()


