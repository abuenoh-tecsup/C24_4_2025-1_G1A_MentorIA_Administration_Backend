from django.core.management.base import BaseCommand
from core.seed import run_seed

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Starting database seed...")
        run_seed()
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
