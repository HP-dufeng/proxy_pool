from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time

import crawl

def do_work(link):
    current_thread_identity = threading.current_thread().ident
    print("thread:"+ str(current_thread_identity) + " crawling page: " + link)
    result = crawl.crawl_proxy(link)

    return result


def wait_for_all_complete(features):
    total = 0
    for feature in as_completed(features):
        total += feature.result()
    print("complete: " + str(total))


def main():
    with ThreadPoolExecutor(max_workers=8) as executor:
        features = set()
        for link in crawl.getther_links(1582):
            feature = executor.submit(do_work, link)
            features.add(feature)
            time.sleep(1)

        wait_for_all_complete(features)


main()  











