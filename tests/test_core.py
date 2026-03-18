"""Tests for MultimodalDataPipeline."""
from src.core import MultimodalDataPipeline
def test_init(): assert MultimodalDataPipeline().get_stats()["ops"] == 0
def test_op(): c = MultimodalDataPipeline(); c.learn(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = MultimodalDataPipeline(); [c.learn() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = MultimodalDataPipeline(); c.learn(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = MultimodalDataPipeline(); r = c.learn(); assert r["service"] == "multimodal-data-pipeline"
