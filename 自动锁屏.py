from win10toast import ToastNotifier
import time
from ctypes import windll
# import win32api,win32con

alter_txt =u'''
将于10秒钟之后屏保，请及时保存工作内容，
并转动脖子，起来走走，喝点水
'''
sleep_time = 10
delay_time = 1800
while True:
    toaster = ToastNotifier()
    toaster.show_toast(u'休息一会儿', alter_txt, icon_path=None,threaded=True)
    time.sleep(sleep_time)
    # win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()
    time.sleep(60)
    while user32.GetForegroundWindow() == 0:  # 判断是否解锁了窗口
        time.sleep(60)
    time.sleep(1800)