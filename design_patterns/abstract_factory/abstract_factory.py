from abc import ABC, abstractmethod
from sys import platform

class Service(ABC):
  @abstractmethod
  def readData(self):
    pass
  
  @abstractmethod
  def writeData(self):
    pass


class ConcreteServiceImpl1(Service):
  def readData(self):
    return "Reading data from MySQL database"

  def writeData(self):
    return "Writing data to MySQL database"


class ConcreteServiceImpl2(Service):
  def readData(self):
    return "Read data from MongoDB database"

  def writeData(self):
    return "Writing data to MongoDB database"


class ServiceFactory(ABC):
    @abstractmethod
    def makeSvc(self):
        return Service()


class ServiceFactoryImpl1(ServiceFactory):
    def makeSvc(self):
      return ConcreteServiceImpl1()


class ServiceFactoryImpl2(ServiceFactory):
    def makeSvc(self):
      return ConcreteServiceImpl2()


class Application():
  def __init__(self, factory):
    self.factory = factory

  def run_app(self):
    service = self.factory.makeSvc()
    result = service.readData()
    print(result)


# Since the client (Application) is only exposed to abstract interfaces, 
# what creates the actual factory objects? Usually, the application creates a 
# concrete factory object at the initialization stage. Just before that, 
# the application must select the factory type depending on the configuration
# or the environment settings.
db = "MySQL"

if db == "MySQL":
  factory = ServiceFactoryImpl1()
elif db == "MongoDB":
  factory = ServiceFactoryImpl2()
else:
  raise NotImplementedError(f"Not implemented for database: {db}")


app = Application(factory)
app.run_app()
