import requests
import time
# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie

#urlinput = (input("请输入网址："))
def single_fetch(
        url,
        cookie = "buvid3=004ADCD1-09D6-3468-B0F5-FCBD5538D1DC94541infoc; b_nut=1758435194; _uuid=D421EAB5-13DC-B984-82E4-7EA2BDFDC35E99017infoc; buvid_fp=c571a16601df75972b9eb8f62849981e; buvid4=4261F23D-37A8-5AD8-28B4-A4E0AD93408295416-025092114-kB3G51FOpkdPw7AFTd68PQ%3D%3D; enable_web_push=DISABLE; rpdid=|(J|Y|kmk~k~0J'u~l)RJlkk); theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; LIVE_BUVID=AUTO4117588620360942; CURRENT_QUALITY=80; PVID=3; home_feed_column=5; theme-switch-show=SHOWED; bp_t_offset_700158015=1142517234095095808; SESSDATA=f407d38d%2C1780403472%2C1d1e9%2Ac1CjC0nEycHqTpJRT0Ka7c2-zUR-nT5wdFPUqybNXid-40FWbYcqmtgqy63QEdalYFyxISVk1LckFQTGh6UE5SNGhqbS1VOWp2RGFFSm9rMUM2cUg3MGNIaWI0NldwNnVPRldwMHBvSm1qcFZvTDlTc05QYlNMM2RmRWxwQW9EZVNEa1RDMGluZF9BIIEC; bili_jct=6b3bfe6dbc1a3dcff19cca73d969d5e5; DedeUserID=3546963328895387; DedeUserID__ckMd5=307adc205c59d3cc; b_lsid=CDA1BA47_19AEC063E57; browser_resolution=1819-996; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjUxNTU2MjIsImlhdCI6MTc2NDg5NjM2MiwicGx0IjotMX0.7Dw_RhWyffZ03MWD-q1DxaUj0M8PqEOCzh5gK8nIHAs; bili_ticket_expires=1765155562; bp_t_offset_3546963328895387=1142710507623415808; sid=5wn1j6kl; CURRENT_FNVAL=4048"
):

    #前置条件，包括待爬取网址url和head
    head = {"User-Agent":"python-request/3.11.0"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            # User-Agent 用户代理, 表示浏览器/设备基本身份信息
            "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
            # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的s
            "Cookie": cookie}

    # 发送请求
    response = requests.get(url=url, headers=headers)
    html = response.text
    print(html)
    # 解析数据: 提取视频标题
    title = re.findall('title="(.*?)"', html)[0]
    print(title)
    # 提取视频信息
    info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
    # info -> json字符串转成json字典
    json_data = json.loads(info)

    #=============暂时用不到=================
    # 提取视频链接
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    print(video_url)
    #=======================================
        
    # 提取音频链接
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    print(audio_url)

    video_content = requests.get(url=video_url, headers=headers).content
    # 获取音频内容
    audio_content = requests.get(url=audio_url, headers=headers).content

    #=============暂时用不到=================
    with open('video\\' + title + '.mp4', mode='wb') as v:
        v.write(video_content)
    #=======================================

    # 保存数据
    with open('audio\\' + title + '.mp3', mode='wb') as a:
        a.write(audio_content)



# single_fetch(url="https://www.bilibili.com/video/BV1b2SgBvEHV")