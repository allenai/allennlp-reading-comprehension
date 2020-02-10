from flaky import flaky

from allennlp.common.testing import ModelTestCase

from tests import FIXTURES_ROOT

import allennlp_rc


class NumericallyAugmentedQaNetTest(ModelTestCase):
    def setUp(self):
        super().setUp()
        self.set_up_model(
            FIXTURES_ROOT / "naqanet" / "experiment.json", FIXTURES_ROOT / "data" / "drop.json"
        )

    @flaky(max_runs=3, min_passes=1)
    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)
