# other imports
import logging

module_logger = logging.getLogger(__name__)

# other variables and methods

# example class
class Foo:
    x: int

    def __init__(self, x: int):
        self.x = x
        self.class_logger = logging.getLogger(__name__)
        self.a = self.bar()
        self.class_logger.info("Finished initializing a Foo class instance")

    def bar(self) -> int:
        self.class_logger.info("Foo.bar method is called when initializing an instance")
        return self.x * 2

# example function
def module_func():
    module_logger.info("Logging from module_func in classfile211")
