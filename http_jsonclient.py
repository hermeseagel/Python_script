from urllib import request 
import json
host='http://ladv.de/api/mmetzger/ausDetail?id=884&wettbewerbe=true&all=true'
urlrequest=request.urlopen(host)
encoding=urlrequest.headers.get_content_charset()
obj = json.loads(urlrequest.read().decode(encoding))
print(obj)