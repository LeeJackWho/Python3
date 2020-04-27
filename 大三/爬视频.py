import requests
import datetime
# 在点击立即播放之前记得将浏览器调成开发者模式（F12），选择Network栏，方便我们查找正确的视频地址，Network一栏里面就会出现视频地址，这个时候我们点击复制Request URL就可以成功复制视频的地址了
url = "http://www.ffa9.cn/cf.aspx?action=cycadget&ad_class=7&userid=21&lowunionusername=&clickstate=2&adshowtype=AdCode_sjdb&ad_size=640x200&showsel=1&newadsel=1&maxadid=&prohibit=627"
# 视频的url地址
html = requests.get(url)
# content返回的的数据（注意，是二进制类型哦！）
html = html.content
start_down_time = datetime.datetime.now()
print('开始下载,时间：{}'.format(start_down_time))
# 因为是二进制数据，所以必须要要采用wb的形式来写入
with open(r'E:\视频\叶问4.mp4', 'wb') as f:
 f.write(html)
end_time = datetime.datetime.now()
print('电影下载结束,时间：{}'.format(end_time))