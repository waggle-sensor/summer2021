from job import job
import json

f = open("metadata.json", "r")

x = json.load(f)
y = job(x)
f.close()



