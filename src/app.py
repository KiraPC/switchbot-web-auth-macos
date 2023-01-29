import struct
from multiprocessing.connection import Client

from AppKit import NSAppleEventManager, NSObject, NSApp, NSApplication, NSLog
from PyObjCTools import AppHelper


class AppDelegate(NSObject):
    def applicationWillFinishLaunching_(self, _):
        NSLog("switchbot.py finish launching")
        manager = NSAppleEventManager.sharedAppleEventManager()
        event_handle = "openURL:withReplyEvent:"
        event_class = event_id = struct.unpack(">l", b"GURL")[0]
        NSLog("switchbot.py send event")

        NSLog(f"switchbot.py event_class {event_class}")
        manager.setEventHandler_andSelector_forEventClass_andEventID_(self, event_handle, event_class, event_id)

    def openURL_withReplyEvent_(self, event, _):
        NSLog("switchbot.py handling event")
        descriptor = struct.unpack(">l", b"----")[0]
        NSLog(f"switchbot.py descriptor {descriptor}")
        url = event.descriptorForKeyword_(descriptor).stringValue()
        NSLog("switchbot.py creating client")
        client = Client(('127.0.0.1', 6000))
        NSLog(f"switchbot.py send url: {url}")
        client.send(url)
        client.close()
        NSApp().terminate_(self)


if __name__ == '__main__':
    NSLog("switchbot.py start")
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    NSLog("switchbot.py run eventloop")
    AppHelper.runEventLoop()
