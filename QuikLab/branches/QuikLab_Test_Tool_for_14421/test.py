from case import tcpIpSmoke
# from casebase.QuikLab_Install import _checkInstall
from casebase.get_usage import get_usage
import threading
threads=[]
t1 = threading.Thread(target=tcpIpSmoke.unittest.main)
threads.append(t1)
t2 = threading.Thread(target=get_usage)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()