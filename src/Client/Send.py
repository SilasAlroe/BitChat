import json
import random
import threading
import time

class Send (threading.Thread):
    def __init__(self,sock,data,target):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.target = target
        global confirmed
    def run(self):
        ident=random.randint(1, 1000000000)
        while True:
            success=False
            print "Trying to send message with id: "+str(ident)
            udata=json.loads(self.data)
            udata["id"]=ident
            self.data=json.dumps(udata)
            self.sock.sendto(self.data,self.target)
            print "Sent message with id: "+str(ident)
            time.sleep(2)
            for i in confirmed:
                if i==ident:
                    success=True
                    confirmed.remove(ident)
            if success:
                print "Sending of: "+str(ident)+" confirmed by remote computer"
                break