from django.db import models
import requests


def md_to_gfm(text):
    headers = {'Content-Type': 'text/plain'}
    data = text.encode('utf-8')
    r = requests.post('https://api.github.com/markdown/raw', headers=headers, data=data)

    return r.text.encode('utf-8')


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.title

    def gfm(self):
        return md_to_gfm(self.text)