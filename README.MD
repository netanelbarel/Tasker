# Tasker

Tasker is a task runner service that exposes a REST API, allowing clients to run various tasks.

## Supported Tasks

1. Sum two numbers
2. Query the OpenAI GPT-3 model
3. Reverse a string

## Getting Started

These instructions will guide you on how to run this service on your local machine.

### Prerequisites

You need to have the following installed:

1. Python 3.8
2. Docker
3. Docker Compose

### Running the Service

To run this service, follow these steps:

1. Clone this repository:

    ```
    git clone https://github.com/netanelbarel/Tasker.git
    ```

2. Navigate to the root directory:

    ```
    cd Tasker
    ```

3. Build and run the Docker image using Docker Compose:

    ```
    docker-compose up --build
    ```

The service should now be running at `http://localhost:5000`.

### API Usage


1. **Sum Two Numbers**

    To run a task to sum two numbers, for example 4 and 2, use the following command:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"type":"sum", "params":[4,2]}' http://localhost:5000/task
    ```

    The service will return a UUID for the task, which you can then use to retrieve the task's output:

    ```bash
    curl -X GET http://localhost:5000/task/{uuid}
    ```

2. **Query the OpenAI GPT-3 Model**

    To run a task to query the OpenAI GPT-3 model, for example to generate text from the prompt "Once upon a time", use the following command:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"type":"gpt", "params":["Once upon a time"]}' http://localhost:5000/task
    ```

    The service will return a UUID for the task, which you can then use to retrieve the task's output:

    ```bash
    curl -X GET http://localhost:5000/task/{uuid}
    ```

3. **Reverse a String**

    To run a task to reverse a string, for example "Hello Seemplicity", use the following command:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"type":"reverse", "params":["Hello Seemplicity"]}' http://localhost:5000/task
    ```

    The service will return a UUID for the task, which you can then use to retrieve the task's output:

    ```bash
    curl -X GET http://localhost:5000/task/{uuid}
    ```

## Design Decisions

- The service is implemented in Python using the Flask framework. Flask was chosen for its simplicity and flexibility. It is light and great for small applications like this one.
- The service uses UUIDs to identify tasks. UUIDs are globally unique, which makes them ideal for this purpose.
- The service uses Docker and Docker Compose for deployment. This makes it easy to deploy the service anywhere that Docker is installed.
- The service runs tasks asynchronously. When a client sends a request to run a task, the service immediately returns a UUID that identifies the task, and the task is run in the background. This allows the service to handle many tasks simultaneously, and ensures that clients don't have to wait for tasks to complete before receiving a response.
- For the GPT-3 task, I use OpenAI's Python library to interact with their API. Please ensure that you have the necessary API key and it is included in the `.env` file (Due to the billing requirement per query associated with the API key, calling "gpt" is not functional in this version.).

## Future Improvements

There are several ways that this service could be improved in the future:

1. **Task Persistence**: Currently, tasks and their outputs are stored in memory, which means they will be lost if the service is restarted. In the future, I could store tasks and their outputs in a database to make them persistent.
2. **Task Status**: Currently, the service does not provide a way to check the status of a task (whether it's pending, running, or completed). In the future, I could add a task status endpoint to the API.
3. **Error Handling**: Currently, the service does not provide detailed error messages when something goes wrong. In the future, I could improve the error handling to make it easier to diagnose and fix issues.
