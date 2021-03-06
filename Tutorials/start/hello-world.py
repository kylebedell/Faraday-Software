#!/usr/bin/env python

import time

# Imports - Faraday Specific
from faraday.proxyio import faradaybasicproxyio
from faraday.proxyio import faradaycommands

#Setup a Faraday IO object
faraday_1 = faradaybasicproxyio.proxyio()  #default proxy port
faraday_cmd = faradaycommands.faraday_commands()

callsign = 'REPLACEME'  # Callsign string
node_id = 0  # Integer 0-255

while True:
    #Turn LED 1 ON (GREEN)
    print "Turning LED 1 ON"
    command = faraday_cmd.CommandLocalGPIOLED1On()
    faraday_1.POST("127.0.0.1", callsign, node_id, faraday_1.CMD_UART_PORT, command)
    time.sleep(0.5)

    #Turn LED 1 OFF
    print "Turning LED 1 OFF"
    command = faraday_cmd.CommandLocalGPIOLED1Off()
    faraday_1.POST("127.0.0.1", callsign, node_id, faraday_1.CMD_UART_PORT, command)
    time.sleep(0.5)
