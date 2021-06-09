from rest_framework import serializers
class websiteSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField()
    description = serializers.CharField()
    url = serializers.CharField()
class WebsiteClass:
    def __init__(self,w):
        self.title= w.title
        self.id = w.id
        self.description = w.description
        self.url = str(w.url)

    @property 
    def data(self):
        return websiteSerializer(self).data

class PageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    img = serializers.CharField()
    description = serializers.CharField()

class PageClass:
    def __init__(self,o):
        self.id = o.id
        self.name= o.name
        self.img = "/static" + o.img.url
        self.description = o.description
    
    @property
    def data(self):
        return PageSerializer(self).data