# simple-memeai/backend/Dockerfile
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all source files
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the backend using your dev script (change to "start" if you prefer the built code)
CMD ["npm", "run", "dev"]
