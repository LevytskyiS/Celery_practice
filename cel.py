import time

from tasks import add

result = add.delay(2, 3)
print(result.state)
time.sleep(7)
print(result.ready())
print(result.result)
