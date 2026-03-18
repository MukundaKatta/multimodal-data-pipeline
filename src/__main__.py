"""CLI for multimodal-data-pipeline."""
import sys, json, argparse
from .core import MultimodalDataPipeline

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline for processing text, image, audio, and video data for AI training")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = MultimodalDataPipeline()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.learn(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"multimodal-data-pipeline v0.1.0 — ETL pipeline for processing text, image, audio, and video data for AI training")

if __name__ == "__main__":
    main()
