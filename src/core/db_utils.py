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

def clear_all_tables():
    app_configs = [app for app in apps.get_app_configs() if not app.name.startswith('django.contrib')]

    with connection.cursor() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")  # ⚠️ Solo en MySQL
        for app_config in app_configs:
            for model in app_config.get_models():
                table_name = model._meta.db_table
                try:
                    cursor.execute(f"DELETE FROM {table_name};")
                except Exception as e:
                    print(f"Error al borrar datos de {table_name}: {e}")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
