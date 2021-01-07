from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(title="This is a title", msg="This is a message",
                 icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)