# Model card: outage-scan model (ersim) v0.2
**Purpose.** Compare what-if source options by how long they keep critical campus services running when the grid fails, started at every hour of the year.
**Inputs.** `site_config.json` (tiers, sources, nodes, indicators, scenario parameters); optional `campus_hourly_load.csv` (`K1_kW,K2_kW,K3_kW`, 8760 rows). Current values: **placeholder / synthetic**.
**Outputs.** Survival share vs duration; duration × condition map; regret table; unserved energy; diesel-CO2 and electrolysis-water indicators.
**Dispatch each hour.** Solar direct, battery, hydrogen fuel cell, generator. All stores start full. Partial service continues after the first shortfall so unserved energy can be counted.
**Service levels.** K1 only; K1+K2; K1+K2+K3 (chosen in advance; dynamic shedding is a candidate for a later version).
**Conditions.** Base; heat wave (+8 °C, outages starting in the hottest 7 days). Generator variants: no resupply; resupply at hour 72.
**Nodes.** A campus item is a node with a status (`unknown`, `exists`, `absent`, `planned`, `map label only`). `null` load means "not modelled". Nodes with status `exists` and parameters build an extra option, "Existing campus assets".
**Metrics.** Survival share is an equal-weight share of start hours, not the probability of a real outage. Autonomy = hours before the first shortfall (capped at 336 h).
**Checks.** 29 self-tests: zero and huge load, store bounds, energy limits, monotonic survival, battery doubling, resupply never worse, unserved ≤ demand.
**Known limits.** No equipment failure; no inverter, ramp or tank-pressure effects; no cost; no emissions beyond diesel burned; synthetic temperature and solar; electrolysis water use is taken as 9 kg per kg of hydrogen (the stoichiometric minimum; real systems need more).
**Figures.** The images in `figures/` are produced from synthetic inputs and say so in their titles; they are not results.
**Not for.** Any statement about real ATÜ performance until real data are loaded and marked `verified`.
