from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ipaddress

app = FastAPI()


class NetworkData(BaseModel):
    network: str


@app.get("/")
def home():
    return {
        "message": "IP Subnet Calculator API Running"
    }


@app.post("/analyze")
def analyze_network(data: NetworkData):

    try:
        network = ipaddress.ip_network(
            data.network,
            strict=False
        )

        total_addresses = network.num_addresses

        if network.version != 4:
            raise ValueError("Only IPv4 networks are supported")

        if total_addresses > 2:
            usable_hosts = total_addresses - 2
            first_usable = str(network.network_address + 1)
            last_usable = str(network.broadcast_address - 1)
        else:
            usable_hosts = 0
            first_usable = None
            last_usable = None

        return {
            "network": str(network),
            "network_address": str(network.network_address),
            "broadcast_address": str(network.broadcast_address),
            "subnet_mask": str(network.netmask),
            "total_addresses": total_addresses,
            "usable_hosts": usable_hosts,
            "first_usable_ip": first_usable,
            "last_usable_ip": last_usable,
            "is_private": network.is_private
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )