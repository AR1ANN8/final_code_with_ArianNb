#theradingpool example code
import time
from concurrent.futures import ThreadPoolExecutor
import requests
urls = [f"https://picsum.photos/{200 + (i % 10) * 10}/{300 + (i % 5) * 10}" for i in range(1000)]
number = 1
def image_download(url):
    global number
    response = requests.get(url)
    with open(f"my_folder/image_{number}.jpg", "wb") as f:
        f.write(response.content)
    number += 1
start_time = time.perf_counter()
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(image_download, urls)
end_time = time.perf_counter()
print("elapsed time:", round(end_time - start_time))