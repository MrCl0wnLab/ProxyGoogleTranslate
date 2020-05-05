# Proxy Google Translate

[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/SenderMailgunPython?color=blue)

Python Module criado para envio de requests usando Google Translate como Proxy.

```
 + Autor: MrCl0wn
 + Blog: http://blog.mrcl0wn.com
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email: mrcl0wnlab\@\gmail.com
```

## Request flow
![Screenshot](https://i.imgur.com/1cCcVU1.png)

## Dependências

- [requests][https://requests.readthedocs.io/en/master/]

## Setup

```bash
$ pip install -r requirements.txt
```

## Usando via linha de comando
```bash
$ python3.7 proxytranslate.py 00000000000000000000000000000000000000dfjjjhv.000webhostapp.com 000000000000000000000000000000000000dbscrfg.000webhostapp.com
```

## Implementation Code

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

for result in proxytranslate.request_proxy(urls_list):
    print(result)

```
