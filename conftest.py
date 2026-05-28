import json
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

CONFIG_PATH = Path(__file__).parent / "config" / "targets.json"

def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def config():
    """Session-scoped fixture — loads targets.json once for all tests."""
    return load_config()

@pytest.fixture(scope="session")
def viewport(config):
    """Returns the viewport size from config."""
    return config["viewport"]

@pytest.fixture(scope="session")
def threshold(config):
    """Returns the acceptable pixel mismatch threshold from config."""
    return config["threshold"]

@pytest.fixture(scope="session")
def targets(config):
    """Returns the list of target pages to test."""
    return config["targets"]

# ── Browser fixtures (one per browser) ──────────────────────────────────────
@pytest.fixture(scope="function")
def chromium_page(viewport):
    """Launches a fresh Chromium browser for each test function."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        yield page, "chromium"
        browser.close()

@pytest.fixture(scope="function")
def firefox_page(viewport):
    """Launches a fresh Firefox browser for each test function."""
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        yield page, "firefox"
        browser.close()

@pytest.fixture(scope="function")
def webkit_page(viewport):
    """Launches a fresh WebKit (Safari engine) browser for each test function."""
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True)
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        yield page, "webkit"
        browser.close()
