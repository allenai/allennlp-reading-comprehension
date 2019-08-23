"""
Reading comprehension is loosely defined as follows: given a question and a passage of text that
contains the answer, answer the question.

These submodules contain models for things that are predominantly focused on reading comprehension.
"""

from allennlp_rc.models.bidaf import BidirectionalAttentionFlow
from allennlp_rc.models.bidaf_ensemble import BidafEnsemble
from allennlp_rc.models.dialog_qa import DialogQA
from allennlp_rc.models.naqanet import NumericallyAugmentedQaNet
from allennlp_rc.models.qanet import QaNet
