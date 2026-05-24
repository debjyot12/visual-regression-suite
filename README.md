# Cross-Browser Visual Regression Suite

A Python + Playwright framework that detects UI changes across Chrome, Firefox, and WebKit by comparing screenshots pixel-by-pixel.

![CI](https://github.com/YOUR_USERNAME/visual-regression-suite/actions/workflows/regression.yml/badge.svg)

## Tech Stack
`Python` · `Playwright` · `pytest` · `Pillow` · `pytest-html` · `GitHub Actions`

## How It Works
1. **First run** — captures baseline screenshots for each target page and browser
2. **Subsequent runs** — captures live screenshots and diffs them against baselines
3. **Result** — PASS if pixel mismatch is within threshold, FAIL if UI has changed
4. **Diff images** — amplified red-channel diff saved to `diffs/` folder for visual inspection

## Project Structure
```
visual-regression-suite/
├── pages/          # Page Object Model (BasePage)
├── tests/          # pytest test files
├── utils/          # screenshot.py + diff.py engine
├── config/         # targets.json (URLs, viewport, threshold)
├── baselines/      # stored baseline screenshots (committed to git)
├── diffs/          # generated diff images (git-ignored)
├── reports/        # pytest-html reports (git-ignored)
└── .github/        # GitHub Actions CI workflow
```

## Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run Tests

```powershell
# First run — creates baselines
pytest -v

# Subsequent runs — compares against baselines
pytest -v
```

## Reset Baselines

```powershell
Remove-Item -Recurse -Force baselines
pytest -v
```

## Configuration

Edit `config/targets.json` to add/remove target URLs, change viewport, or adjust threshold:

```json
{
  "targets": [...],
  "threshold": 0.05,
  "viewport": { "width": 1280, "height": 720 }
}
```

## Roadmap
- [x] Phase 1 — Foundation: POM, conftest, baseline capture, pixel diff, HTML report
- [ ] Phase 2 — Multi-browser: Firefox + WebKit test matrix
- [ ] Phase 3 — Reporting: Allure integration, embedded diff images in report
- [ ] Phase 4 — CI/CD: GitHub Actions matrix strategy, daily scheduled runs
- [ ] Phase 5 — Polish: Config-driven URL list, environment support, Slack alerts
