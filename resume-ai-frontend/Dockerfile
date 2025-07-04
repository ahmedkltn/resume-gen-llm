FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy all source files
COPY . .

# Expose the port Next.js runs on
EXPOSE 3000

# Build the Next.js application
RUN npm run build

# Start the production server
CMD ["npm", "run", "start"]