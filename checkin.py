import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
# sever = os.environ["SERVE"]
sever = 'on'

# 填写server酱sckey,不开启server酱则不用填
#sckey = os.environ["SCKEY"]
#'SCU89402Tf98b7f01ca3394*********************************'
sckey = 'SCU119278Tea1616c91bf685bdf392c934662d67795f8f1d39443ea'

# 填入glados账号对应cookie
#cookie = os.environ["COOKIE"]
#'__cfduid=d3459ec306384ca67a65170f8e2a5bd************; _ga=GA1.2.766373509.1593*****72; _gid=GA1.2.1338236108.***********72; koa:sess=eyJ1c2VySW*********************aXJlIjoxNjE4OTY5NTI4MzY4LCJfbWF4QWdl****0=; koa:sess.sig=6qG8SyMh*****LBc9yRviaPvI'
cookie = '__cfduid=d3f2347c38b60610c3ac88dc1fb5111e01602695401; _ga=GA1.2.1395069274.1600081218; _gid=GA1.2.268684821.1603213960; koa:sess=eyJ1c2VySWQiOjUxNDEyLCJfZXhwaXJlIjoxNjI2MjE5NjgzMDcyLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=wqiGhyN0DfipAEatyLXwaAjVBC8'



def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
