"""Tests for Pipeline."""
import pytest
from src.pipeline import Pipeline

def test_init():
    obj = Pipeline()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = Pipeline()
    result = obj.ingest_text(input="test")
    assert result["processed"] is True
    assert result["operation"] == "ingest_text"

def test_multiple_ops():
    obj = Pipeline()
    for m in ['ingest_text', 'ingest_image', 'ingest_audio']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = Pipeline()
    r1 = obj.ingest_text(key="same")
    r2 = obj.ingest_text(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = Pipeline()
    obj.ingest_text()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = Pipeline()
    obj.ingest_text(x=1)
    obj.ingest_image(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
