import time
import random
from csvManager import csvManager

logger = csvManager("log_temp.csv","wb","ENABLE")

logger.writeHeader()

while 1:
    Temperature = random.randint(-40,100)
    logger.writeValue(Temperature)
    time.sleep(2)