#!/bin/bash

if [ "$PROXY" = "true" ]; then
    export HTTP_PROXY=$PROXY_URL
    export HTTPS_PROXY=$PROXY_URL
    echo "Proxy enabled. Using SOCKS5 proxy at $PROXY_URL"
    proxychains4 python bot.py
else
    echo "Proxy disabled. Connecting directly."
    python bot.py
fi
