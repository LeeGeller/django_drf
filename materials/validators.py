import re

from rest_framework import serializers


class LinkToVideoValidator:
    def __call__(self, link):
        reg_link = r"^(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?"
        if not re.match(reg_link, link):
            raise serializers.ValidationError("Link to video have to be youtube link!")
