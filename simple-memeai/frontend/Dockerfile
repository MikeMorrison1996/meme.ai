# simple-memeai/frontend/Dockerfile
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy package.json (if you have one; if not, it’s optional)
COPY package*.json ./

# Install dependencies (if any) - for a static frontend this might be minimal; we're using http-server
RUN npm install --production http-server

# Copy the frontend files
COPY . .

# Expose port 8080 (or the port you wish to use)
EXPOSE 8080

# Start an HTTP server to serve the static frontend files
CMD ["npx", "http-server", ".", "-p", "8080"]
