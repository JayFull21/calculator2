from unittest.mock import patch
from calculator.__main__ import run


def test_main_runs(monkeypatch):
    with patch("calculator.repl.run") as mock_run:
        run()
        mock_run.assert_called_once()