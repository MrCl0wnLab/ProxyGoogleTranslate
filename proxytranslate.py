import re
import html
import datetime
import requests
from urllib import request
import sys
from concurrent.futures import ThreadPoolExecutor

HEADERS = {
    'Host': 'translate.google.com',
    'User-Agent': 'android'
}

MAX_CONECTION_THREAD = 10

BASE_URL_PROXY = 'https://translate.googleusercontent.com'
BASE_URL_TRANSLATE = 'https://translate.google.com/translate?hl=pt-BR&sl=en&tl=pt&u=[TARGET_URL]&sandbox=0'  # noqa: E501


def checker_url(html, url):
    grep_regex = re.findall(r'href="|src="|value="|((?:http[s]://|ftp[s]://)+\.*([-a-zA-Z0-9\.]+)([-a-zA-Z0-9\.]){1,}([-a-zA-Z0-9_\.\#\@\:%_/\?\=\~\&\-\//\!\'\;\(\)\s\^\:blank:\:punct:\:xdigit:\:space:\$]+))', html)  # noqa: E501
    for url_result_regex in grep_regex:
        if url in url_result_regex[0]:
            return url_result_regex[0]


def process_request_proxy(url):
    if not url:
        return

    try:
        target_url = \
            BASE_URL_TRANSLATE.replace('[TARGET_URL]', request.quote(url))

        return_html = requests.get(target_url, timeout=20, headers=HEADERS)

        if not return_html:
            return

        url_request = checker_url(
            return_html.text,
            f'{BASE_URL_PROXY}/translate_p?hl=pt-BR&sl=en&tl=pt&u='
        )

        request_final = requests.get(
            url_request,
            timeout=20,
            headers={'User-Agent': 'android'}
        )

        url_request_proxy = html.unescape(checker_url(
            request_final.text, f'{BASE_URL_PROXY}/translate_c?depth=1')
        )

        timenow = str(datetime.datetime.now())
        result = requests.get(
            url_request_proxy,
            timeout=20,
            headers={'User-Agent': 'android'}
        )

        return {'url': url.strip(), 'time': timenow, 'result': result}
    except Exception as e:
        print(e)


def request_proxy(urls_file):
    executor = ThreadPoolExecutor(max_workers=MAX_CONECTION_THREAD)
    for result in executor.map(process_request_proxy, urls_file):
        yield result

    executor.shutdown(wait=True)


# Using as command line
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:')
        print(f'\tpython {sys.argv[0]} [host1] [host2] ... [hostn]\n')
        sys.exit(0)

    hosts = sys.argv[1:]
    print(list(request_proxy(hosts)))
