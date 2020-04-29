# Proxy Google Translate
 
[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/SenderMailgunPython?color=blue)

Modulo Python criado para envio de requests usando Google Translate como Proxy.

```
 + Autor: MrCl0wn
 + Blog: http://blog.mrcl0wn.com
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email: mrcl0wnlab\@\gmail.com
```

## Implementation Code / Simples
```python
import proxytranslate

url_googl_engine = ['http://ifconfig.ca']

proxytranslate.request_proxy(url_googl_engine)
for result_request in proxytranslate.RESULT_URLS_THREAD:
    print(result_request.get('url'),
          result_request.get('time'),
          result_request.get('result').text)
```
## Implementation Code / Multiple URLs
```python

import proxytranslate

#########################################################################
#      EXEMPLO USANDO PROXY TRANSLATE EM VARIOS HOSTS  / MULTHREAD      #
#########################################################################
urls_list = ['00000000000000000000000000000000000000dfjjjhv.000webhostapp.com',
             '000000000000000000000000000000000000dbscrfg.000webhostapp.com',
             '000000000000000000000000000yteyeuya.000webhostapp.com',
             '00000000000000000dhl.000webhostapp.co',
             '00000000000000rqrewewrwrdfq.000webhostapp.com',
             '0000000000000qowowiieueu0000000.000webhostapp.com',
             '0000000wer.000webhostapp.com',
             '00000skunnnn.000webhostapp.com',
             '00024390000067.000webhostapp.com',
             '000945.000webhostapp.com',
             '000f02ef-3ec1-4247-ae2a-17788214a6a0.htmlpasta.com',
             '000m8ih.wcomhost.com',
             '000web2.000webhostapp.com',
             '000web3.000webhostapp.com',
             '000webhos1.000webhostapp.com',
             '000webhostcrazystikers.000webhostapp.com',
             '000wechost.000webhostapp.com',
             '000wexbhost.000webhostapp.com']


proxytranslate.URL_PROCESS = urls_list
proxytranslate.MAX_CONECTION_THREAD = 20

count_process_url = 0
url_tmp = []

for url in proxytranslate.URL_PROCESS:

    url_tmp = proxytranslate.select_range_url(
        proxytranslate.MAX_CONECTION_THREAD)
    proxytranslate.request_proxy(url_tmp)
    try:
        for result in proxytranslate.RESULT_URLS_THREAD:
            url_request = result.get('url')
            time_request = result.get('time')
            result_request = result.get('result')

            print(
                f' [{count_process_url}] {time_request} | {url_request} | {result_request.status_code}')
            count_process_url += 1
    except:
        pass

```

