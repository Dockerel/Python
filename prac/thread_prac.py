import time
import requests
import threading


def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


sum(1, 10000000)

t = threading.Thread(target=sum, args=(1, 10000000))
t.start()

print("Main Thread\n")


##################################################


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), 'chars')


t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()

print("### End ###")


##################################################


class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')


t = HtmlGetter('http://google.com')
t.start()

print("### End ###")


##################################################


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')


# 데몬 쓰레드 : 백그라운드에서 실행되는 쓰레드로 메인 쓰레드가 종료되면 즉시 종료되는 쓰레드
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.daemon = True
t1.start()

print("### End ###")

# (실행결과)
# $ python thrd2.py
# ### End ###
