# Energy Resilience Under Prolonged Grid Outages
### Which Source Holds When the Grid Doesn't?
*Case study: ATÜ campus, Adana (Türkiye). Research workspace of TOPBASCH Systems Lab. Author: Ahmet Selahaddin Topbaş ([LinkedIn](https://www.linkedin.com/in/ahmet-selahaddin-topbas/)). Status: **v0.2, work in progress, no results yet**. Earlier work by the same lab: the [Léargas SI](https://github.com/Ahmet-Selahaddin-Topbas/leargas-si) analytical framework and three whitepapers.*

---
### ご挨拶 (Greeting)
このリポジトリを訪れてくださり、ありがとうございます。トルコ・アダナのATÜキャンパスを例に、「電力網が長時間止まったとき、どのエネルギー源が、どの条件で、何時間まで持ちこたえるか」を調べる研究の記録です。モデル、資料、毎週の作業記録、考察ノートをすべて公開しています。現在は途中経過で、結果はまだありません。
*(Japanese text written by the author with an AI assistant.)*

---
## The question
If the grid fails for a long time, which source (generator, solar, battery, hydrogen chain) holds the critical services of a campus, under which condition, and for how many hours? Hydrogen is tested, not assumed to win.

## How this repository is organised (read in 3 minutes)
| Folder | What it holds |
|---|---|
| `1_models/` | The outage-scan model (`ersim.py`), the site configuration, the notebook, self-tests, model versions |
| `2_data_sources/` | Data register, literature register, campus site register and diagram (category level), synthetic inputs |
| `3_process_journal/` | **What we did**, one dated file per week. Entries are never deleted; corrections are new entries |
| `4_minarai_notes/` | **Why we did it** and what changed in our thinking. *Minarai* (見習い) means apprentice |
| `5_article_of_output/` | The research report in progress |
| `pre_hypothesis/` | What we expected before seeing results. v1.0 is frozen; revisions are added as new dated files (template included) |
| `next_version_roadmap.md` | Ideas deliberately kept outside this version |
| `AI_USE.md` | How AI tools were used |

## What the model does (and does not)
It starts a grid outage at **every hour of the year** and follows it hour by hour for up to 14 days, for four what-if source options with equal stored energy, serving three tiers of critical load (labs and servers, dining, classroom cooling). Results are read as survival share, unserved energy and regret against outage duration, in base and heat-wave conditions, with a resupply variant for the generator.
It does **not** model equipment failures, inverter or tank effects, costs or optimisation. The model *supports* decisions; it does not make them. Campus data are not yet available: **all numbers are placeholders or synthetic and are labelled as such** (the figures in `1_models/figures/` are illustrative, not results).

## Run it
Open `1_models/M02_outage_scan_v0.2.ipynb` in Google Colab (File > Open notebook > GitHub), or run `python 1_models/tests/run_selftest.py` for the self-tests.

## Originality statement (limited search)
In a search limited to Scopus and the web on 30 October 2026, no work offering this combination was seen. This is not proof of novelty. Closest work: Lee (2026, *Int. J. Hydrogen Energy* 264, 156805): fixed 48 h outage, random starts, island, example load.

## Privacy and data policy
Only category-level site information is published. Raw data, other people's e-mails and personal details are not stored here. People are named only with their consent.

## Licence
Code (`1_models/*.py`, the notebooks and the tests): MIT, see `LICENSE`. Documents, figures, registers and data tables: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Works cited in the registers keep their own licences.
