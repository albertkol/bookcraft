from bookcraft.helpers import (
    get_files,
    get_page,
    get_pages,
    next_chars_matches,
    previous_chars_matches,
)


def test_get_files(tmp_path):
    (tmp_path / "page-1.txt").write_text("hello")
    (tmp_path / "page-2.txt").write_text("world")
    result = get_files(str(tmp_path))
    assert set(result) == {"page-1.txt", "page-2.txt"}


def test_get_page_reads_content(tmp_path):
    (tmp_path / "page-1.txt").write_bytes(b"line one\nline two")
    result = get_page(str(tmp_path), 1)
    assert result == ["line one", "line two"]


def test_get_page_returns_none_when_missing(tmp_path):
    result = get_page(str(tmp_path), 99)
    assert result is None


def test_get_pages_returns_single_page(tmp_path):
    (tmp_path / "page-1.txt").write_bytes(b"hello")
    result = get_pages(str(tmp_path), 1)
    assert result == ["hello"]


def test_get_pages_returns_multiple_pages(tmp_path):
    (tmp_path / "page-1.txt").write_bytes(b"page one")
    (tmp_path / "page-2.txt").write_bytes(b"page two")
    result = get_pages(str(tmp_path), 1, 2)
    assert len(result) == 2
    assert result[0] == ["page one"]
    assert result[1] == ["page two"]


def test_get_pages_skips_missing(tmp_path):
    (tmp_path / "page-1.txt").write_bytes(b"only page")
    result = get_pages(str(tmp_path), 1, 2)
    assert len(result) == 1


def test_previous_chars_matches_wraps_to_previous_line():
    memory = [["hello", "world"]]
    result = previous_chars_matches(["hello"], i=1, j=0, memory=memory)
    assert result == "hello"


def test_previous_chars_matches_returns_none_when_no_match():
    memory = [["hello", "world"]]
    result = previous_chars_matches(["xyz"], i=1, j=0, memory=memory)
    assert result is None


def test_next_chars_matches_crosses_line():
    memory = [["hello", "world"]]
    match, count = next_chars_matches(["o wo"], i=0, j=4, memory=memory)
    assert match == "o wo"
    assert count == 3  # len - 1 because breaks_line


def test_next_chars_matches_crosses_page():
    memory = [["hello"], ["world"]]
    match, count = next_chars_matches(["o wo"], i=0, j=4, memory=memory)
    assert match == "o wo"


def test_next_chars_matches_end_of_book():
    memory = [["hi"]]
    match, count = next_chars_matches(["hi there"], i=0, j=0, memory=memory)
    assert match is None
    assert count == 0
