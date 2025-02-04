import pytest
from django.test.runner import DiscoverRunner

class PytestTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        pytest_args = list(test_labels) if test_labels else []
        return pytest.main(pytest_args)
