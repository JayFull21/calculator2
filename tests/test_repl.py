import pytest
from calculator import repl


def test_quit(monkeypatch):
    inputs = iter(["quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()


def test_valid_addition(monkeypatch, capsys):
    inputs = iter(["+", "2", "3", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_valid_subtraction(monkeypatch, capsys):
    inputs = iter(["-", "10", "3", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Result: 7.0" in captured.out


def test_valid_multiplication(monkeypatch, capsys):
    inputs = iter(["*", "3", "4", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Result: 12.0" in captured.out


def test_valid_division(monkeypatch, capsys):
    inputs = iter(["/", "10", "2", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_invalid_operator(monkeypatch, capsys):
    inputs = iter(["x", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Input error" in captured.out


def test_invalid_number(monkeypatch, capsys):
    inputs = iter(["+", "abc", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Input error" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["/", "5", "0", "quit"])
    monkeypatch.setattr(repl, "_prompt", lambda msg: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Error" in captured.out