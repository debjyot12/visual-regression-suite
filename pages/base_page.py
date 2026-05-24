from playwright.sync_api import Page


class BasePage:
    """
    Base Page Object Model class.
    All page classes will inherit from this.
    Handles common actions like navigation, waiting, and screenshots.
    """

    def __init__(self, page: Page, viewport: dict):
        self.page = page
        self.viewport = viewport

    def navigate(self, url: str):
        """Navigate to a URL and wait for the page to fully load."""
        self.page.set_viewport_size(self.viewport)
        self.page.goto(url, wait_until="networkidle", timeout=30000)

    def capture_screenshot(self, path: str):
        """Take a full-page screenshot and save it to the given path."""
        self.page.screenshot(path=path, full_page=True)
        print(f"  [screenshot] saved → {path}")

    def get_page_title(self) -> str:
        return self.page.title()

