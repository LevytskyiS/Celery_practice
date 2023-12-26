import time

from tasks import add

result = add.delay(2, 3)
print(result.state)
time.sleep(3)
print(result.ready())
