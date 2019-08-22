"""
Reading comprehension is loosely defined as follows: given a question and a passage of text that
contains the answer, answer the question.

These submodules contain models for things that are predominantly focused on reading comprehension.
"""

from allennlp_reading_comprehension.models.bidaf import BidirectionalAttentionFlow
from allennlp_reading_comprehension.models.bidaf_ensemble import BidafEnsemble
from allennlp_reading_comprehension.models.dialog_qa import DialogQA
from allennlp_reading_comprehension.models.naqanet import NumericallyAugmentedQaNet
from allennlp_reading_comprehension.models.qanet import QaNet
