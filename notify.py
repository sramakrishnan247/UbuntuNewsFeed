import time
import notify2
from news import load

newsItems = load()
notify2.init("TopStories")
notification = notify2.Notification(None)
notification.set_urgency(notify2.URGENCY_NORMAL)
notification.set_timeout(10000)

for newsitem in newsItems:
    try:
        notification.update(newsitem['title'], newsitem['des'])
        notification.show()
        time.sleep(10)
    except:
        time.sleep(0)