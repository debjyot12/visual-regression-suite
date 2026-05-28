"""
Phase 1 — Visual Regression Tests (Chromium only)

How it works:
  - First run: baselines do NOT exist → test captures them and PASSES (baseline created)
  - Second run onwards: compares current screenshot vs baseline
    → PASS if mismatch is within threshold
    → FAIL if mismatch exceeds threshold (UI has changed)

To reset baselines: delete the baselines/ folder and re-run.
"""

import pytest
from pages.base_page import BasePage
from utils.screenshot import capture_baseline, capture_current, get_baseline_path, get_diff_path
from utils.diff import compute_diff, is_within_threshold


class TestVisualRegression:

    def test_wikipedia_homepage_chromium(self, chromium_page, targets, viewport, threshold):
        """Visual regression test for Wikipedia homepage on Chromium."""
        page, browser_name = chromium_page
        target = next(t for t in targets if t["name"] == "wikipedia_home")

        page_obj = BasePage(page, viewport)
        baseline_path = capture_baseline(page_obj, target["url"], browser_name, target["name"])
        current_path = capture_current(page_obj, target["url"], browser_name, target["name"])

        diff_path = str(get_diff_path(browser_name, target["name"]))
        mismatch = compute_diff(baseline_path, current_path, diff_path)

        print(f"\n  [result] {target['name']} | browser={browser_name} | mismatch={mismatch:.4%} | threshold={threshold:.2%}")

        assert is_within_threshold(mismatch, threshold), (
            f"Visual regression FAILED for '{target['name']}' on {browser_name}.\n"
            f"Mismatch: {mismatch:.4%} exceeds threshold: {threshold:.2%}\n"
            f"Diff image saved at: {diff_path}"
        )

    def test_books_catalogue_chromium(self, chromium_page, targets, viewport, threshold):
        """Visual regression test for Books to Scrape catalogue on Chromium."""
        page, browser_name = chromium_page
        target = next(t for t in targets if t["name"] == "books_catalogue")

        page_obj = BasePage(page, viewport)
        baseline_path = capture_baseline(page_obj, target["url"], browser_name, target["name"])
        current_path = capture_current(page_obj, target["url"], browser_name, target["name"])

        diff_path = str(get_diff_path(browser_name, target["name"]))
        mismatch = compute_diff(baseline_path, current_path, diff_path)

        print(f"\n  [result] {target['name']} | browser={browser_name} | mismatch={mismatch:.4%} | threshold={threshold:.2%}")

        assert is_within_threshold(mismatch, threshold), (
            f"Visual regression FAILED for '{target['name']}' on {browser_name}.\n"
            f"Mismatch: {mismatch:.4%} exceeds threshold: {threshold:.2%}\n"
            f"Diff image saved at: {diff_path}"
        )

    def test_example_dot_com_chromium(self, chromium_page, targets, viewport, threshold):
        """Visual regression test for Example.com on Chromium."""
        page, browser_name = chromium_page
        target = next(t for t in targets if t["name"] == "example_dot_com")

        page_obj = BasePage(page, viewport)
        baseline_path = capture_baseline(page_obj, target["url"], browser_name, target["name"])
        current_path = capture_current(page_obj, target["url"], browser_name, target["name"])

        diff_path = str(get_diff_path(browser_name, target["name"]))
        mismatch = compute_diff(baseline_path, current_path, diff_path)

        print(f"\n  [result] {target['name']} | browser={browser_name} | mismatch={mismatch:.4%} | threshold={threshold:.2%}")

        assert is_within_threshold(mismatch, threshold), (
            f"Visual regression FAILED for '{target['name']}' on {browser_name}.\n"
            f"Mismatch: {mismatch:.4%} exceeds threshold: {threshold:.2%}\n"
            f"Diff image saved at: {diff_path}"
        )
