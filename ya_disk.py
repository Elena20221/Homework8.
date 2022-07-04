from pprint import pprint
import requests
import json

TOKEN=''
class YandexDisk:
    def __init__(self,token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': "OAuth {}".format(self.token)
        }


    def _get_upload_link(self,disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers =self.get_headers()
        params= {"path":disk_file_path,"overwrite":"true"}
        response =requests.get(upload_url,headers =headers,params = params )
        pprint(response.json())
        return response.json()





    def upload_file_to_disk(self, disk_file_path,filename):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        url = response_href.get("href","")
        response =requests.put(url,data=open(filename,'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__=='__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path="TEST/test.1.txt",filename = "test.py")


