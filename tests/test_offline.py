"""Deterministic tests; no LLM service or external network connection required."""
import json
import unittest
from pathlib import Path

from core.memory import SimpleMemory
from envs.public_goods import PublicGoodsEnv, PublicGoodsConfig
from eval.metrics import social_welfare, bias_corrected_score

ROOT = Path(__file__).resolve().parents[1]

class TestCoreWithoutAPI(unittest.TestCase):
    def test_memory_retrieval(self):
        memory = SimpleMemory()
        memory.add_event("The lab contributed compute hours for maintenance")
        memory.add_event("A negotiation concerned shared equipment")
        found = memory.retrieve("contributed compute maintenance", k=1)
        self.assertEqual(len(found), 1)
        self.assertIn("maintenance", found[0].text)

    def test_public_goods_step(self):
        agent_ids = ["A", "B", "C", "D"]
        env = PublicGoodsEnv(agent_ids, PublicGoodsConfig(), seed=7)
        observations = env.reset()
        self.assertEqual(set(observations), set(agent_ids))
        result = env.step({a: {"action": 6} for a in agent_ids})
        self.assertEqual(result.info["round_total"], 24)
        self.assertEqual(result.info["actions"]["A"], 6)
        self.assertGreaterEqual(social_welfare(result.rewards), 0)

    def test_calibration_identity(self):
        self.assertAlmostEqual(bias_corrected_score(0.4, 1.0, 1.0), 0.4)

    def test_survey_schema(self):
        survey = json.loads((ROOT / "data" / "surveys.json").read_text(encoding="utf-8"))
        self.assertEqual(set(survey["traits"]), {"O", "C", "E", "A", "N"})
        self.assertTrue(len(survey["items"]) >= 5)

if __name__ == "__main__":
    unittest.main()
