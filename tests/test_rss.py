from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_rss_relative_link_is_resolved() -> None:
    """Some feeds (e.g. DRAMeXchange) ship relative <link> paths.

    Scraper must resolve them to absolute URLs against the feed's source URL
    so pydantic HttpUrl validator accepts them.
    """
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>/WeeklyResearch/Post/2/12756.html</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://www.dramexchange.com/rss.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    assert str(items[0].url) == "https://www.dramexchange.com/WeeklyResearch/Post/2/12756.html"


def test_rss_naive_date_is_normalized_to_utc() -> None:
    """Feeds with timezone-less <pubDate> (e.g. 'Tue, 08 Jul 2025 10:00:00')

    must be coerced to UTC-aware so the since-comparison doesn't blow up
    with 'can't compare offset-naive and offset-aware datetimes'.
    """
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Tue, 08 Jul 2025 10:00:00</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2025, 7, 8, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    assert items[0].published_at.tzinfo is not None
    assert items[0].published_at == datetime(2025, 7, 8, 10, 0, tzinfo=timezone.utc)


def test_rss_sends_browser_user_agent() -> None:
    """RSS scraper must send a Mozilla UA so WAF-protected feeds (e.g.
    Electronics Weekly) return 200 instead of 403.
    """
    response = MagicMock()
    response.text = """<?xml version="1.0" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item><guid>x</guid><title>T</title>
        <link>https://example.com/x</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
      </item></channel></rss>"""
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)

    asyncio.run(scraper.fetch(datetime(2026, 4, 24, tzinfo=timezone.utc)))

    call_kwargs = client.get.call_args.kwargs
    ua = call_kwargs.get("headers", {}).get("User-Agent", "")
    assert "Mozilla" in ua, f"Expected Mozilla UA, got {ua!r}"
