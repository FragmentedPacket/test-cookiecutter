"""Plugin declaration for my_plugin."""

__version__ = "0.1.0"

from nautobot.extras.plugins import PluginConfig


class MyPluginConfig(PluginConfig):
    """Plugin configuration for the my_plugin plugin."""

    name = "my_plugin"
    verbose_name = "My Plugin"
    version = __version__
    author = "Network to Code, LLC"
    description = "My Plugin."
    base_url = "my-plugin"
    required_settings = []
    min_version = "1.0.0b3"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = MyPluginConfig  # pylint:disable=invalid-name
