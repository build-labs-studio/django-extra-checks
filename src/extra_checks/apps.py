from django.apps import AppConfig


class ExtraChecksConfig(AppConfig):
    name = "extra_checks"

    def ready(self) -> None:
        super(ExtraChecksConfig, self).ready()
        from . import checks  # noqa
        from .controller import registry

        registry.finish()
