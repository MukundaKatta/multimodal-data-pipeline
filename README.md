# Multimodal Data Pipeline

ETL pipeline for text, image, audio, video AI data

## Features

- Api
Pipeline
Processors - Audio
Processors - Image
Processors - Text
Processors - Video
Scheduler
Storage
Transforms

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/multimodal-data-pipeline.git
cd multimodal-data-pipeline
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
multimodal-data-pipeline/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
