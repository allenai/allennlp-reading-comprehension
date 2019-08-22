# pylint: disable=invalid-name,protected-access
import pathlib
import tempfile
from allennlp.common.testing import AllenNlpTestCase

TEST_DIR = tempfile.mkdtemp(prefix="allennlp_reading_comprehension_tests")

class AllenNlpReadingComprehensionTestCase(AllenNlpTestCase):  # pylint: disable=too-many-public-methods
    """
    A custom subclass of :class:`~unittest.TestCase` that disables some of the
    more verbose AllenNLP logging and that creates and destroys a temp directory
    as a test fixture.
    """
    PROJECT_ROOT = (pathlib.Path(__file__).parent / ".." / ".." / "..").resolve()  # pylint: disable=no-member
    MODULE_ROOT = PROJECT_ROOT / "allennlp_reading_comprehension"
    TOOLS_ROOT = MODULE_ROOT / "tools"
    TESTS_ROOT = MODULE_ROOT / "tests"
    FIXTURES_ROOT = TESTS_ROOT / "fixtures"
