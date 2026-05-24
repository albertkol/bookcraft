import sys
from unittest.mock import patch

import pytest

from bookcraft.cli import main


def test_cli_exits_without_args():
    with patch.object(sys, "argv", ["bookcraft"]):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0


def test_cli_calls_generate():
    with patch("bookcraft.cli.generate") as mock_generate:
        with patch.object(
            sys,
            "argv",
            [
                "bookcraft",
                "craft",
                "--books",
                "./books/",
                "--settings",
                "settings.yaml",
                "--fonts",
                "fonts.yaml",
                "--keywords",
                "keywords.yaml",
                "--output",
                "output.pdf",
            ],
        ):
            main()
        mock_generate.assert_called_once_with(
            books_path="./books/",
            settings_path="settings.yaml",
            fonts_path="fonts.yaml",
            keywords_path="keywords.yaml",
            output_path="output.pdf",
            mode="craft",
        )
