import os
from django.core.management.base import BaseCommand
from core.seed import run_seed

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **options):
        enable_seed = os.environ.get('ENABLE_SEED', 'false').lower()

        if enable_seed != 'true':
            self.stdout.write(self.style.WARNING("Seeding is disabled. Set ENABLE_SEED=true to enable."))
            return

        self.stdout.write("Starting database seed...")
        run_seed()
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
