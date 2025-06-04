FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code
COPY . .

# STDIO does not expose any ports, so no EXPOSE needed

# Run the MCP server using STDIO transport
CMD ["python", "main.py"]