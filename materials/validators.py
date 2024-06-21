import re

from rest_framework import serializers


class LinkToVideoValidator:

    def __call__(self, value):
        reg_link = r"^(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?"
        print(value)
        if not re.match(reg_link, value):
            raise serializers.ValidationError("Link to video have to be youtube link!")
