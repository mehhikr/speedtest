import speedtest
import time
import datetime

def run_speed_test():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()
    print(f"Timestamp: {datetime.datetime.now()}")
    print(f"Download Speed: {results['download'] / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {results['upload'] / 1_000_000:.2f} Mbps")
    print(f"Ping: {results['ping']} ms")
    print('-' * 40)

while True:
    run_speed_test()
    time.sleep(60)
