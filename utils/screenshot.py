import os
from pathlib import Path
from pages.base_page import BasePage


BASELINES_DIR = Path("baselines")
DIFFS_DIR = Path("diffs")


def get_baseline_path(browser_name: str, page_name: str) -> Path:
    """Returns the path where the baseline screenshot should be stored."""
    folder = BASELINES_DIR / browser_name
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{page_name}.png"


def get_diff_path(browser_name: str, page_name: str) -> Path:
    """Returns the path where the diff image should be saved."""
    folder = DIFFS_DIR / browser_name
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{page_name}_diff.png"


def capture_baseline(page_obj: BasePage, url: str, browser_name: str, page_name: str):
    """
    Navigates to the URL and saves a baseline screenshot.
    Only runs if the baseline does not already exist.
    """
    path = get_baseline_path(browser_name, page_name)

    if path.exists():
        print(f"  [baseline] already exists, skipping → {path}")
        return str(path)

    page_obj.navigate(url)
    page_obj.capture_screenshot(str(path))
    print(f"  [baseline] created → {path}")
    return str(path)


def capture_current(page_obj: BasePage, url: str, browser_name: str, page_name: str) -> str:
    """
    Navigates to the URL and saves the current (live) screenshot.
    Always overwrites to get the latest state.
    """
    folder = Path("reports") / "current" / browser_name
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{page_name}_current.png"

    page_obj.navigate(url)
    page_obj.capture_screenshot(str(path))
    print(f"  [current] captured → {path}")
    return str(path)
