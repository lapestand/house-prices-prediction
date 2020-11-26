import time
import os
import requests
import shutil
from validator_collection import validators, checkers


class Crawler:
    def __init__(self):
        self.data_sources = ["sahibinden.com"]

    def get_from(self, source):
        if source == "sahibinden.com":
            self.from_sahibinden()

    def from_sahibinden(self):
        xml_source = "https://www.sahibinden.com/sitemap/search/real-estate.xml"
        self.download(xml_source, "crawler/sahibinden.com/", xml_source.split('/')[-1])
        urls = self.get_urls_from_xml(xml_source)

    def get_urls_from_xml(self, xml):
        return []

    def is_xml(self, in_file):
        if "xml" in in_file:
            with open(in_file, 'r') as f:
                data = re.sub(r'\s+', '', f.read())
                if re.match(r'^<.+>$', data):
                    return True
        return False

    def download(self, src: str, dst: str, name: str):
        if not os.path.exists(dst):
            os.makedirs(dst)

        dst = os.path.join(dst, name)

        src = validators.url(src)
        print(src)
        print("indiriliyor")
        response = requests.get(src, allow_redirects=True)
        print("indirildi")
        try:
            print("kaydediliyor")
            with open(dst, "wb") as dst_file:
                dst_file.write(response.content)
            print("kaydedildi")
        except:
            return False
