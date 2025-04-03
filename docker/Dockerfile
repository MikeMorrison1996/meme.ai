FROM python:3.11-slim

# Install system dependencies for solana + Rust
RUN apt-get update && \
    apt-get install -y curl build-essential pkg-config libssl-dev libffi-dev python3-dev perl && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    . "$HOME/.cargo/env"

# Set workdir and copy code
WORKDIR /app
COPY . .

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
