import os
import logging
import logging.config
from datetime import datetime
from application.module2.submodule1 import classfile211
from application.module1 import file11
from application.module2 import file21

module_logger = logging.getLogger(__name__)

def main():
    current_datetime = datetime.now().strftime('%b%d_%H%M')
    logging.config.fileConfig(
          'logging.config',
          defaults={'logfilepath': os.getenv('LOG_FILE_PATH', f"{current_datetime}.log")}
      )

    module_logger.info("Logging from main")

    some_func()

# example function in mainfile
def some_func():
    module_logger.info("Logging from some_func in mainfile")
    # do other stuff

    # call module_func in file11
    file11.module_func()

    # create Foo object
    classfile211.Foo(x=5)

    # call module_func in classfile211
    classfile211.module_func()

    # call module_func in file21
    file21.module_func()
