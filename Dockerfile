FROM python:3.7-slim
# Install the Flask package via pip
RUN pip install flask==1.0.2

#copy source file
COPY ./src/* /app/

# Change the working directory
WORKDIR /app/

# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["app.py"]