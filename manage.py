#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sigmahacks2.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sigmahacks.settings")
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
