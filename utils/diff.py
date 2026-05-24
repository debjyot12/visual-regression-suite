from pathlib import Path
from PIL import Image, ImageChops, ImageEnhance


def compute_diff(baseline_path: str, current_path: str, diff_output_path: str) -> float:
    """
    Compares two screenshots pixel by pixel.

    Steps:
      1. Opens both images with Pillow
      2. Resizes current to match baseline dimensions (handles minor size shifts)
      3. Computes pixel difference using ImageChops
      4. Amplifies diff so small changes are visible in red
      5. Calculates the mismatch percentage

    Returns:
        mismatch_percent (float) — 0.0 means identical, 1.0 means fully different
    """
    baseline = Image.open(baseline_path).convert("RGB")
    current = Image.open(current_path).convert("RGB")

    # Resize current to baseline dimensions if they differ
    if baseline.size != current.size:
        print(f"  [diff] resizing current {current.size} → {baseline.size}")
        current = current.resize(baseline.size, Image.LANCZOS)

    # Raw pixel difference
    raw_diff = ImageChops.difference(baseline, current)

    # Amplify the diff so even small changes are clearly visible
    amplified = ImageEnhance.Brightness(raw_diff).enhance(5.0)

    # Save the diff image
    Path(diff_output_path).parent.mkdir(parents=True, exist_ok=True)
    amplified.save(diff_output_path)
    print(f"  [diff] saved → {diff_output_path}")

    # Calculate mismatch percentage
    total_pixels = baseline.width * baseline.height * 3  # RGB channels
    diff_pixels = sum(raw_diff.tobytes())
    mismatch_percent = diff_pixels / (total_pixels * 255)

    return round(mismatch_percent, 6)


def is_within_threshold(mismatch_percent: float, threshold: float) -> bool:
    """Returns True if the mismatch is within the acceptable threshold."""
    return mismatch_percent <= threshold
