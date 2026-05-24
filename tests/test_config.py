import pytest
from pydantic import ValidationError

from bookcraft.config import Config
from bookcraft.schema import Settings


def test_is_dark_false_for_craft(config):
    assert config.is_dark is False


def test_is_dark_true_for_dark_switch(config):
    config.switch = "c-dark-"
    assert config.is_dark is True


def test_is_ra_false_for_craft(config):
    assert config.is_ra is False


def test_is_ra_true_for_ra_switch(config):
    config.switch = "ra-"
    assert config.is_ra is True


def test_page_returns_page_config(config):
    assert config.page.top_margin == 18
    assert config.page.margin_size == 40


def test_default_height(config):
    assert config.default_height == 20


def test_roles_accessible_by_name(config):
    assert config.roles["W. M."].light == [200, 200, 200]
    assert config.roles["S. W."].dark == [100, 150, 200]


def test_invalid_settings_raises():
    with pytest.raises(ValidationError):
        Settings(title="not-a-dict", books=[], colour={}, text={}, roles={}, page={})
