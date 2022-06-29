from webdav3.client import Client
import os
import yaml

params = yaml.safe_load(open("authentication.yaml"))

login = params["login"]
password = params["password"]

remote_directory = "cv/Human detection model/data/raw"
root = "/remote.php/dav/files/" + login

options = {
 'webdav_hostname': "https://cloud.matway.com",
 'webdav_login': login,
 'webdav_password': password,
 'webdav_root': root
}
client = Client(options)

if not os.path.isdir("data/raw"):
     os.mkdir("data/raw")
local_directory = os.getcwd() + "/data/raw"

client.pull(remote_directory = remote_directory, local_directory = local_directory)