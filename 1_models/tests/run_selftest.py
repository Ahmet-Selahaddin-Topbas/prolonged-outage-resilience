"""Run the model self-tests from the command line:  python tests/run_selftest.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import ersim
cfg = ersim.load_config(os.path.join(os.path.dirname(__file__), "..", "site_config.json"))
tests = ersim.selftest(cfg)
print(f"{sum(ok for _, ok in tests)} of {len(tests)} tests passed")
