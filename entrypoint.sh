#!/bin/bash

# Ensure proxychains config file is set up
PROXYCHAINS_CONF="/etc/proxychains4.conf"

if [ "$PROXY" = "true" ]; then
    echo "Proxy enabled. Using SOCKS5 proxy at $PROXY_URL"

    # Extract host and port from PROXY_URL
    PROXY_HOST=$(echo $PROXY_URL | sed -E 's#socks5://([^:]+):([^@]+)@([^:]+):([0-9]+)#\3#')
    PROXY_PORT=$(echo $PROXY_URL | sed -E 's#socks5://([^:]+):([^@]+)@([^:]+):([0-9]+)#\4#')
    PROXY_USER=$(echo $PROXY_URL | sed -E 's#socks5://([^:]+):([^@]+)@([^:]+):([0-9]+)#\1#')
    PROXY_PASS=$(echo $PROXY_URL | sed -E 's#socks5://([^:]+):([^@]+)@([^:]+):([0-9]+)#\2#')

    # Update proxychains4 configuration dynamically
    echo "socks5 $PROXY_HOST $PROXY_PORT $PROXY_USER $PROXY_PASS" >> "$PROXYCHAINS_CONF"

    # Run Python bot through ProxyChains4
    proxychains4 python bot.py
else
    echo "Proxy disabled. Connecting directly."
    python bot.py
fi
