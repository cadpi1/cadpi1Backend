#requires input of ukccookie
import sys
import requests

cookie = {'ukcsid':sys.stdin.read()}

url='http://ukclimbing.com/logbook/export/logbook_xls.php'

r=requests.get(url = url, cookies=cookie)
open('spreadsheet.xls', 'wb').write(r.content)
