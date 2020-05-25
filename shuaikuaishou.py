import uiautomator2 as u2
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.button import Button
import time
import random

class test(App):
    def build(self):
        d = u2.connect('127.0.0.1:62001')  # connect to device
# d = u2.connect('KWG7N16727003146')mi9pro
        height = d.info['displayHeight']
        width = d.info['displayWidth']
        print(d.info)
        d.app_start('com.kuaishou.nebula', "com.yxcorp.gifshow.HomeActivity")
        d.toast.show('启动快手极速版')
        print('启动快手极速版')
# 模拟器
#d.xpath('//*[@resource-id="com.kuaishou.nebula:id/recycler_view"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
#d.toast.show('点击第2视频')
#print('点击第2视频')
        print('正在看视频...')
        start = time.perf_counter()
        page = 0
        while True:
            page += 1
            d.swipe(width/2, 3*height/4, width/2, height/4, 0.2)
            d.toast.show('已看 {} 个'.format(page))
            time.sleep(10 + random.randint(5, 12))  # 一个10+n秒
            readtime = time.perf_counter() - start
            if readtime > 5 * 3600:
                break
        print('共看了 {} 个，用时 {}'.format(page, readtime / 3600))
        return Button()

if __name__=='__main__':
    test().run()