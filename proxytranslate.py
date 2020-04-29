import re
import html
import time
import datetime
import threading
import requests
from urllib import request

HEADERS = {
    'Host': 'translate.google.com',
    'User-Agent': 'android'
}

RESULT_URLS_THREAD = []
MAX_CONECTION_THREAD = 10
URL_PROCESS = []


base_url_proxy = 'https://translate.googleusercontent.com'
base_url_translate = 'https://translate.google.com/translate?hl=pt-BR&sl=en&tl=pt&u=[TARGET_URL]&sandbox=0'


def checker_url(html, url):
    grep_regex = re.findall(
        r'href="|src="|value="|((?:http[s]://|ftp[s]://)+\.*([-a-zA-Z0-9\.]+)([-a-zA-Z0-9\.]){1,}([-a-zA-Z0-9_\.\#\@\:%_/\?\=\~\&\-\//\!\'\;\(\)\s\^\:blank:\:punct:\:xdigit:\:space:\$]+))', html)
    for url_result_regex in grep_regex:
        if url in url_result_regex[0]:
            return url_result_regex[0]


def process_request_proxy(url_list):

    url_list_process = []
    url_list_process.append(url_list)

    try:
        for url in url_list_process:
            if url:
                target_url = base_url_translate.replace(
                    '[TARGET_URL]', request.quote(url))

                return_html = requests.get(
                    target_url, timeout=20, headers=HEADERS)
                if return_html:
                    url_request = checker_url(
                        return_html.text, f'{base_url_proxy}/translate_p?hl=pt-BR&sl=en&tl=pt&u=')

                    request_final = requests.get(url_request, timeout=20, headers={
                                                 'User-Agent': 'android'})

                    url_request_proxy = html.unescape(checker_url(
                        request_final.text, f'{base_url_proxy}/translate_c?depth=1'))

                    timenow = str(datetime.datetime.now())
                    result = requests.get(url_request_proxy, timeout=20, headers={
                                          'User-Agent': 'android'})

                    RESULT_URLS_THREAD.append(
                        {'url': url.strip(), 'time': timenow, 'result': result})
    except Exception as e:
        print(e)


def select_range_url(total_select_url):
    tmp_urls = []
    try:
        for url in range(total_select_url):
            if url:
                tmp_urls.append(URL_PROCESS[url])
                URL_PROCESS.pop(url)
    except:
        pass
    return tmp_urls


def process_translate_engine_thread(urls, count_url):
    process_request_proxy(urls)


def request_proxy(urls_file):

    list_threads = []
    count_url = 0
    RESULT_URLS_THREAD.clear()

    for target_url in urls_file:

        while threading.active_count() > MAX_CONECTION_THREAD:
            time.sleep(0.5)

        thread = threading.Thread(
            target=process_translate_engine_thread, args=(target_url, count_url))

        count_url += 1

        list_threads.append(thread)
        thread.start()

    for thread in list_threads:
        thread.join()
