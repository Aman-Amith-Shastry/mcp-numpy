FROM python:3.11-slim

WORKDIR /app

# Install MCP server package and numpy
RUN pip install --no-cache-dir mcp-numpy -r requirements.txt

# (Optional) If you have custom code, copy it in:
# COPY . .

# Expose the port (replace 8080 with your server’s port if different)
EXPOSE 8080

# Start the MCP server (replace with the actual command if different)
CMD ["mcp-numpy", "--host", "0.0.0.0", "--port", "8080"]