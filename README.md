# OpenAI Agents Redis Example

This project demonstrates how to integrate OpenAI agents with Redis using Docker containers.

## Getting Started

To run the project, follow these steps:

1. Start the required services using Docker Compose:
    ```bash
    docker compose up
    ```
2. Build the CLI container:
    ```bash
    docker build -t openai-agents-cli .
    ```
3. Run the CLI container, ensuring it uses the same Docker network as the other containers (e.g., `openai-agents-redis-example_agents-net`):
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

The `docker-compose.yml` file includes services for the OpenAI agents application and a Redis container for storing session data. RedisInsight, a free tool from Redis, can be used to connect to the Redis container and visualize session data. To use RedisInsight, launch the application and connect to the Redis instance using the container's host and port (typically `localhost:6379` if mapped). This allows you to inspect keys, view stored session information, and monitor interactions in real time.