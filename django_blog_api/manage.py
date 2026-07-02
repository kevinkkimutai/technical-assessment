#!/usr/bin/env python3
import os
import sys
from pathlib import Path


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parent
    venv_python = project_dir / ".venv" / "bin" / "python3"

    if venv_python.exists() and sys.executable != str(venv_python):
        os.execv(str(venv_python), [str(venv_python), str(project_dir / "manage.py")] + sys.argv[1:])

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
