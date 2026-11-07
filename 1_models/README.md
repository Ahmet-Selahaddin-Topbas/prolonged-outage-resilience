# 1_models: the outage-scan model

| File | What it is |
|---|---|
| `ersim.py` | The simulation engine. Starts an outage at every hour of the year and follows it up to 336 h for four what-if source options |
| `site_config.json` | Campus nodes and their status (`unknown`, `exists`, `absent`, `planned`, `map label only`). `null` means no data, never zero |
| `M02_outage_scan_v0.2.ipynb` | The notebook that runs the scan and draws the figures. Open in Google Colab |
| `tests/run_selftest.py` | 29 self-tests: `python tests/run_selftest.py` |
| `model_card.md` | What the model does, assumes and leaves out |
| `CHANGELOG.md` | Version history |
| `requirements.txt` | Python packages |
| `figures/` | Illustrative figures. All use placeholder inputs and are not results |
| `archive/` | Earlier model versions |

All inputs are placeholders or synthetic until campus data arrive.
