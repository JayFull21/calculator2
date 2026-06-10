from unittest.mock import patch
import runpy


def test_main_entry_point():
    with patch("calculator.repl.run") as mock_run:
        runpy.run_module("calculator", run_name="__main__")
        mock_run.assert_called_once()