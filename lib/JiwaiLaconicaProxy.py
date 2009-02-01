from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log

from urllib import quote as urlquote

class Client(proxy.ProxyClient):

    def handleStatus(self, version, status, message):
        self.status = int(status)
        proxy.ProxyClient.handleStatus(self, version, status, message)

    def handleResponsePart(self, buffer):
        if self.status == 200 and self.rest.find('/account/verify_credentials.xml') == 0:
            buffer = self.jiwaiVerifyCredentialsHook()
        proxy.ProxyClient.handleResponsePart(self, buffer)

    def jiwaiVerifyCredentialsHook(self):
        return '<?xml version="1.0" encoding="UTF-8"?>' + "\n" + '<authorized>true</authorized>';

class ClientFactory(proxy.ProxyClientFactory):
    
    protocol = Client 
    

class Resource(proxy.ReverseProxyResource):

    proxyClientFactoryClass = ClientFactory

    def __init__(self, host, port, path, reactor=reactor):
        proxy.ReverseProxyResource.__init__(self, host, port, path, reactor)

    def getChild(self, path, request):
        if path == 'api':
            return Resource(self.host, self.port, self.path)
        return Resource(self.host, self.port, self.path + '/' + urlquote(path, safe=""))

    def render(self, request):
        request.setHost(self.host, self.port)
        return proxy.ReverseProxyResource.render(self, request)
        


