FROM bitnami/spark:latest

# Set environment variables
ENV SPARK_MASTER_HOST='spark-master'
ENV SPARK_MASTER_PORT='7077'
ENV SPARK_HOME='/opt/bitnami/spark'

# Expose ports
EXPOSE 4040 7077 8080 6066
