# IP Subnet Calculator API

A FastAPI application that analyzes IPv4 networks and returns useful subnet information.

## Features

- IPv4 Validation
- Network Address
- Broadcast Address
- Subnet Mask
- Usable Host Count
- First Usable IP
- Last Usable IP
- Private/Public Network Detection

## Technologies

- Python
- FastAPI
- Pydantic
- ipaddress

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Endpoint

```text
POST /analyze
```

## Example Request

```json
{
    "network": "192.168.1.0/24"
}
```

## Example Response

```json
{
    "network": "192.168.1.0/24",
    "network_address": "192.168.1.0",
    "broadcast_address": "192.168.1.255",
    "subnet_mask": "255.255.255.0",
    "total_addresses": 256,
    "usable_hosts": 254,
    "first_usable_ip": "192.168.1.1",
    "last_usable_ip": "192.168.1.254",
    "is_private": true
}
```