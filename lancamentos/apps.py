from django.apps import AppConfig


class LancamentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lancamentos'

    # signals do python
    def ready(self, *args, **kwargs):
        import lancamentos.signals
        s_ready = super().ready(*args, **kwargs)
        return s_ready
