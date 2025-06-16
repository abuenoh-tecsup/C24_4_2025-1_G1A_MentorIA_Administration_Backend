from core.seeders.academic import seed_academic
from core.seeders.authentication import seed_authentication
from core.seeders.courses import seed_courses
from core.db_utils import reset_auto_increment_all_apps

def run_seed():
    # Ejecuta los seeders de cada app
    seed_academic()
    seed_authentication()
    seed_courses()
    
    # Resetea los AUTO_INCREMENT de todas las tablas
    reset_auto_increment_all_apps()
