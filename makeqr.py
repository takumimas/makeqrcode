import urllib.request
import urllib.parse
value_text = input("URL or Text >")
file_name = input("file name(don't have to input '.png') >")
url = "http://chart.apis.google.com/chart?cht=qr&chs=130x130&chl="+value_text
with urllib.request.urlopen(url) as res:
    ans = res.read()
    file_name = file_name + ".png"
    wr = open(file_name,mode="wb")
    wr.write(ans)
    wr.close()