# OWASP LAHORE Hero Image Assets

The homepage (`/index.md`) uses `owasp-lahore-hero.jpg` from this folder as
its hero background. That final image is produced by stitching the two
event photos together.

## Files expected here

| File                      | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| `OWASP-6.jpg`             | LEFT half — "Global Expertise. Stronger Together." group photo   |
| `OWASP-7.jpg`             | RIGHT half — group photo with OWASP LAHORE + tkxel logos         |
| `owasp-lahore-hero.jpg`   | GENERATED — combined side-by-side panoramic hero                 |
| `combine_hero.py`         | Script that produces `owasp-lahore-hero.jpg` from the two halves |

## How to generate the hero image

1. Save the two source photos as `OWASP-6.jpg` and `OWASP-7.jpg` in this
   directory (`assets/images/content/owasp-lahore/`).
2. Run:

   ```bash
   cd assets/images/content/owasp-lahore
   python3 combine_hero.py
   ```

   (Requires `Pillow`: `pip3 install Pillow` if it is not installed.)

3. Commit all three files (`OWASP-6.jpg`, `OWASP-7.jpg`,
   `owasp-lahore-hero.jpg`) and push.

The homepage will render the combined image as a full-width background.
