from django.apps import apps
from django.db import connection

def reset_auto_increment_all_apps():
    app_configs = [app for app in apps.get_app_configs() if not app.name.startswith('django.contrib')]
    with connection.cursor() as cursor:
        for app_config in app_configs:
            for model in app_config.get_models():
                table_name = model._meta.db_table
                try:
                    cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
                except Exception:
                    pass
