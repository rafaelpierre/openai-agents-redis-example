# OpenAI Agents Redis Example

This project demonstrates how to integrate [openai-agents-redis](https://pypi.org/project/openai-agents-redis/) using Docker containers.

More details about **openai-agents-redis** can be found in its [repo](https://github.com/rafaelpierre/openai-agents-redis).

## Requirements

* [Docker](https://docker.io)
* [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

## Getting Started

To run the project, follow these steps:

1. Start [Redis](https://redis.io) and [RedisInsight](https://redis.io/insight/) using Docker Compose:
    ```bash
    docker compose up
    ```
2. Build the CLI container:
    ```bash
    docker build -t openai-agents-cli .
    ```
3. Run the CLI container in interactive mode, ensuring it uses the same Docker network as the other containers (e.g., `openai-agents-redis-example_agent-net`):
    ```bash
    docker run -it \
        --network openai-agents-redis-example_agent-net \
        -e AZURE_OPENAI_ENDPOINT="..." \
        -e AZURE_OPENAI_API_VERSION="..." \
        -e AZURE_OPENAI_DEPLOYMENT="..." \
        -e AZURE_OPENAI_KEY="..." \
        openai-agents-cli
    ```

## Visualizing Session Data

The `docker-compose.yml` file includes services for the OpenAI agents application and a Redis container for storing session data.

[RedisInsight](https://redis.io/insight/), a free tool from [Redis](https://redis.io), can be used to connect to the Redis container and visualize session data. To use RedisInsight, launch the application and connect to the RedisInsight instance using the container's host and port (typically `localhost:5540` if mapped).

This allows you to inspect keys, view stored session information, and monitor interactions in real time.