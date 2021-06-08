import docker 
from io import BytesIO
from docker import APIClient

dockerfile = "/Users/abayomi/Desktop/Projects/edge-plugins/plugin-metsense/"

def build_plugin():
    client = docker.from_env()

    f = BytesIO(dockerfile.encode('utf-8'))
    cli = APIClient(base_url='unix://var/run/docker.sock')
    # response = [line for line in cli.build(path=dockerfile, rm=True, tag='yourname/volume')]
    # print(response)
    for line in cli.build(path=dockerfile, rm=True, tag='yourname/volume'):
        print(line)

build_plugin()

