from dnry.config import IConfigFactory, IConfigSection
from dnry.config.in_memory import InMemorySource
from pyioc3 import StaticContainerBuilder

from dnry.srvhost.builder import SrvHostBase, SrvHostBuilder, ISrvHostContext, ISrvHost


class Service:
    def __init__(self, config: IConfigSection):
        self.__greeting = config.get("Greeting") or "Hello"

    def greet(self, name: str):
        print(f"{self.__greeting}, {name}!")


class Host(SrvHostBase):
    def run(self):
        """ Scoped request Example:

        Note: this here is the service locator patter - This should be avoided.
        This is generally considered a bad practice but at the same time it is
        a very valid way to scope a request. Think of http requests where each
        request that comes in pulls its own dependency graph. If you do use
        this pattern, it should only happen at the top of your application.
        """
        print("Press CTRL+C to exit...")
        while True:
            name = input("Type your name: ")
            greeter: Service = self.service_provider.get(Service)
            greeter.greet(name)


def setup_config(ctx: ISrvHostContext, conf: IConfigFactory):
    conf.add_source(InMemorySource({"Greeting": "Hello"}))


def setup_services(ctx: ISrvHostContext, services: StaticContainerBuilder):
    services.bind(ISrvHost, Host)
    services.bind(Service, Service)


if __name__ == "__main__":
    SrvHostBuilder("Long running") \
        .config_configuration(setup_config) \
        .config_services(setup_services) \
        .build() \
        .run()
