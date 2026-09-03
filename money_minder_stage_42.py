# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MoneyMinder
import os

def _colorize(text, code):
    return f"\033[{code}m{text}\033[0m"

def _colorize_reset(text):
    return f"\033[0m{text}\033[0m"

DISABLE_COLOR = os.environ.get("MONEYMINDER_NO_COLOR", "").lower() in ("1", "true", "yes")

def print_moneyminder(text):
    if DISABLE_COLOR:
        print(text)
        return
    print(_colorize(text, "32"))

def print_moneyminder_header(text):
    if DISABLE_COLOR:
        print("=" * 60)
        print(text)
        print("=" * 60)
        return
    print(_colorize("=" * 60, "37"))
    print(_colorize(text, "36"))
    print(_colorize("=" * 60, "37"))

def print_moneyminder_success(text):
    if DISABLE_COLOR:
        print(f"✓ {text}")
        return
    print(_colorize(f"✓ {text}", "32"))

def print_moneyminder_error(text):
    if DISABLE_COLOR:
        print(f"✗ {text}")
        return
    print(_colorize(f"✗ {text}", "31"))

def print_moneyminder_warning(text):
    if DISABLE_COLOR:
        print(f"⚠ {text}")
        return
    print(_colorize(f"⚠ {text}", "33"))

def print_moneyminder_info(text):
    if DISABLE_COLOR:
        print(f"> {text}")
        return
    print(_colorize(f"> {text}", "36"))
