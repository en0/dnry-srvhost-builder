from dnry.config import IConfigFactory
from pyioc3 import StaticContainerBuilder

from dnry.srvhost.builder.srv_host_builder import SrvHostBuilder, ISrvHostContext


def setup_config(ctx: ISrvHostContext, conf: IConfigFactory):
    # Add configuration files here
    pass


def setup_services(ctx: ISrvHostContext, services: StaticContainerBuilder):
    # Add other services here
    pass


if __name__ == "__main__":
    SrvHostBuilder("noop") \
        .config_configuration(setup_config) \
        .config_services(setup_services) \
        .build() \
        .run()
