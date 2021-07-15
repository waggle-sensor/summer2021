from extract_payload import extract_payload
from extract_payload import init_logging
import json

f = open("payload_v1.json", "r")

j = json.load(f)

extract_payload(j)
# init_logging()