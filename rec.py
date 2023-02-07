import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'
respons = requests.get(url=url)

def super_heroes(heroes):
    hero = 'Hulk', 'Captain America', 'Thanos'
    dict_ = {}
    for heros in heroes:
        if heros['name'] in hero:
            dict_[heros['name']] = heros['powerstats']['intelligence']
    return(max(dict_.keys()))

pprint((super_heroes(respons.json())))

TOKEN =

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self,):
        return {'Countent-Type': 'applecation/json',
                'Authorization': 'OAuth {}'.format(self.token)
                                 }
    def _get_upload_link(self, disk_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params )
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        resoult = self._get_upload_link(disk_file_path=disk_file_path)
        url = resoult.get('href')
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Зачисленно')

if __name__ == '__main__':
    token = TOKEN
    uploader = YaUploader(token)
    resoult = uploader.upload_file_to_disk(disk_file_path="netology/test23.txt",
                             filename='test.txt')
    pprint(resoult)
