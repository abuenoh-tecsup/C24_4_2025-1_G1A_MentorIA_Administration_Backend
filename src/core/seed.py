from core.seeders.academic import seed_academic
from core.seeders.authentication import seed_authentication
from core.seeders.courses import seed_courses
from core.db_utils import clear_all_tables, reset_auto_increment_all_apps

def run_seed():
    print("Eliminando todos los datos...")
    clear_all_tables()

    print("Reseteando AUTO_INCREMENT...")
    reset_auto_increment_all_apps()

    print("Seedando datos iniciales...")
    seed_academic()
    seed_authentication()
    seed_courses()

    print("Seed completo.")
