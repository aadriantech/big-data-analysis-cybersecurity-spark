# Use the bitnami/spark base image
FROM bitnami/spark:3.5-debian-12

# Switch to root to install necessary items
USER root

# Install vim, net-tools, python and OS utilities
RUN apt-get update && apt-get install -y \
    vim \
    net-tools \
    python3 python3-pip \
    sudo \
    ncurses-bin && rm -rf /var/lib/apt/lists/*;

# Install Python Libraries
RUN pip install plotly pandas pyspark matplotlib seaborn scikit-learn openpyxl

# Copy the entrypoint script into the container at the root directory
COPY ./docker/entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Switch back to default user
USER 1001

# Specify the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "/opt/bitnami/scripts/spark/run.sh" ]
