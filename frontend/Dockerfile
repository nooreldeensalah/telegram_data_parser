FROM node:18-slim

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vite app (for production, use 'build' instead of 'dev')
CMD ["npm", "run", "dev"]
