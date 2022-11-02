"""
Django command to wait for database to be availabke.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for databse."""
    
    def handle(self, *args, **options):
        pass
    