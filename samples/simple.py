from dnry.config import IConfigFactory
from dnry.config.in_memory import InMemorySource
from pyioc3 import StaticContainerBuilder

from dnry.srvhost.builder import SrvHostBase, ISrvHostContext, ISrvHost, SrvHostBuilder


class Host(SrvHostBase):
    def run(self):
        greeting = self.configuration.get("Greeting")
        name = self.configuration.get("Name")
        print(f"{greeting}, {name}!")


def setup_config(ctx: ISrvHostContext, conf: IConfigFactory):
    conf.add_source(InMemorySource({
        "Greeting": "Hello",
        "Name": "World"
    }))


def setup_services(ctx: ISrvHostContext, services: StaticContainerBuilder):
    services.bind(ISrvHost, Host)


if __name__ == "__main__":
    SrvHostBuilder("simple") \
        .config_configuration(setup_config) \
        .config_services(setup_services) \
        .build() \
        .run()
