# Project Overview

This project leverages Apache Spark, Hadoop MapReduce, Docker, and Python to perform big data analysis, aiming to provide insights into cybersecurity threats and network vulnerabilities. Through the use of MapReduce algorithms for data processing and Spark for in-memory data analytics, the project aims to identify and visualize patterns in large datasets, such as logs indicating failed SSH login attempts or potential web vulnerabilities.

## Setup and Usage

### Docker and Apache Spark Setup

A Docker container based on the `bitnami/spark:3.5-debian-12` image is utilized for running Spark in an isolated environment. The Docker setup includes a Dockerfile and docker-compose.yml for building and running the Spark service. An entrypoint script, `entrypoint.sh`, is used to initiate the Spark service automatically upon container startup.

### Data Generation and Analysis

Python scripts are employed to generate simulated log data, mimicking SSH login attempts and web access logs. These logs are then processed using custom MapReduce algorithms to identify patterns such as failed login attempts and potential web vulnerabilities. The analysis results are visualized using Plotly, providing a graphical representation of the data to support cybersecurity analysis and decision-making.

### Environment Configuration

The project supports different environment configurations, allowing for flexibility in deployment and testing. Depending on the environment (local or production), additional utilities can be installed within the container to facilitate development and debugging.

## Features

- **Data Processing**: Utilizes Hadoop MapReduce for efficient processing of large datasets.
- **In-Memory Analysis**: Leverages Apache Spark for fast in-memory data analytics.
- **Visualization**: Employs Plotly for generating insightful visualizations of the analysis results.
- **Dockerized Environment**: Provides a containerized setup for ease of deployment and environment consistency.
- **Flexible Environment Setup**: Supports environment-specific configurations to tailor the setup for development or production use.

## Prerequisites

- Docker and docker-compose
- Python 3.x
- Access to a Linux-based environment or a virtual machine for Docker and Hadoop/Spark setup

## Installation and Running

1. **Build the Docker Container**
   Navigate to the project directory and run `docker-compose up` to build and start the Spark container.

2. **Data Generation**
   Execute the Python scripts to generate simulated log data for analysis.

3. **Run MapReduce Jobs**
   Submit MapReduce jobs through Hadoop streaming to process the generated log data.

4. **Visualization**
   Use the provided Python scripts to generate visualizations from the processed data.

## Contribution

Contributions to the project are welcome. Please follow the standard GitHub pull request process to submit your contributions. Ensure to adhere to the coding standards and provide documentation for your code.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.