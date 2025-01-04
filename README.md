

# Project Overview
====================
This project is a collection of tools and scripts for testing and analyzing various messaging protocols, including AMQP (Advanced Message Queuing Protocol) and MQTT (Message Queuing Telemetry Transport). The project also includes a set of scripts for scanning and testing IP addresses.

## AMQP
--------

The AMQP directory contains scripts for testing and demonstrating AMQP functionality. These scripts include:

* `attacker.py`: A script that sends a message to an AMQP queue in chunks, simulating a slowloris-style attack.
* `producer.py`: A script that sends a message to an AMQP queue.
* `consumer.py`: A script that consumes messages from an AMQP queue.

## MQTT
--------

The MQTT directory contains scripts for testing and demonstrating MQTT functionality. These scripts include:

* `publisher.py`: A script that publishes a message to an MQTT topic.
* `subscriber.py`: A script that subscribes to an MQTT topic and prints incoming messages.

## MQTT_Attack
-------------

The MQTT_Attack directory contains scripts for testing and demonstrating MQTT-based attacks. These scripts include:

* `slowite.py`: A script that performs a slowloris-style attack on an MQTT broker.
* `slowtt.py`: A script that performs a slowloris-style attack on an MQTT broker using multiple clients.
* `slowite_data.py`: A script that analyzes the results of a slowloris-style attack on an MQTT broker.

## IPAddressScan
----------------

The IPAddressScan directory contains scripts for scanning and testing IP addresses. These scripts include:

* `ipscan.py`: A script that scans a range of IP addresses for open ports.
* `check_ip.py`: A script that checks if a given IP address has an MQTT service running on a specified port.

## Running the Scripts
----------------------

### Prerequisites

* Python 3.6 or later
* `paho-mqtt` library (install with `pip install paho-mqtt`)
* `pika` library (install with `pip install pika`)
* `asyncio` library (install with `pip install asyncio`)

### Running the Scripts

1. Clone the repository to your local machine.
2. Navigate to the directory containing the script you want to run.
3. Run the script using Python (e.g. `python slowite.py`).

### Script-Specific Instructions

* `slowite.py`: Run with `python slowite.py -a <broker_address> -p <broker_port> -k <keep_alive>`. Replace `<broker_address>` with the IP address of the MQTT broker, `<broker_port>` with the port number of the MQTT broker, and `<keep_alive>` with the keep-alive interval.
* `slowtt.py`: Run with `python slowtt.py -a <broker_address> -p <broker_port> -k <keep_alive> -c <connections>`. Replace `<broker_address>` with the IP address of the MQTT broker, `<broker_port>` with the port number of the MQTT broker, `<keep_alive>` with the keep-alive interval, and `<connections>` with the number of connections to establish.
* `ipscan.py`: Run with `python ipscan.py <start_ip> <end_ip>`. Replace `<start_ip>` and `<end_ip>` with the start and end IP addresses of the range you want to scan.
* `check_ip.py`: Run with `python check_ip.py <ip_address> <port>`. Replace `<ip_address>` with the IP address you want to check and `<port>` with the port number of the MQTT service.

## Usage
-----

To use these scripts, simply run them from the command line. For example, to run the `slowite.py` script, navigate to the MQTT_Attack directory and run `python slowite.py`.

Note: These scripts are for testing and demonstration purposes only and should not be used to attack or harm any system or network without explicit permission.

## Requirements
------------

These scripts require the following libraries and tools:

* `paho-mqtt` for MQTT functionality
* `pika` for AMQP functionality
* `socket` and `struct` for IP address scanning
* `asyncio` for asynchronous programming