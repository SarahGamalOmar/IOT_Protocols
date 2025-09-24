# IoT Protocols 

This repository contains simple Python examples for three common IoT protocols: **HTTP**, **MQTT**, and **CoAP**.


## Description

- **HTTP:**  
  Uses Flask to implement a REST API for temperature values.  
  Client sends GET and POST requests using the `requests` library.

- **MQTT:**  
  Uses Paho MQTT library.  
  Publisher sends random temperature data to a topic.  
  Subscriber listens to that topic and prints incoming messages.

- **CoAP:**  
  Uses aiocoap library to create a simple CoAP server with a `/temperature` resource.  
  Client sends a GET request to retrieve the temperature.

##️ Requirements

Install the required libraries before running:

```bash
pip install flask requests paho-mqtt aiocoap




