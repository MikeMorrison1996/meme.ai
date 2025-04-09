![image](https://github.com/user-attachments/assets/3ec5faa4-40ab-42e9-a148-b6eae1c44a3a)

```markdown
# Meme.ai

Meme.ai is a real-time meme coin intelligence platform designed to simplify crypto data analysis for meme coin investors. This project demonstrates our ability to integrate live API data, containerize our full-stack application using Docker, and build a collaborative development environment.

## Overview

Meme.ai consists of two primary components:

- **Backend:**  
  A Node.js/Express API built with TypeScript that fetches live token profile data from the [DexScreener API](https://docs.dexscreener.com/api/reference). The backend parses the raw API response into structured arrays for easy frontend consumption and provides additional endpoints for wallet creation and simulated transactions.

- **Frontend:**  
  A dynamic dashboard created with HTML, CSS, and JavaScript. The frontend fetches data from the backend and displays token cards complete with icons, descriptions, and links to DexScreener.

- **Containerization:**  
  Both backend and frontend are containerized using Docker and orchestrated with Docker Compose, ensuring a consistent development and deployment environment.

## Project Structure

```
meme.ai/
├── backend/                 # Node.js/Express API (port 3000)
│   ├── src/
│   │   ├── index.ts         # Express server setup and middleware configuration
│   │   ├── dexScreener.ts   # Module to fetch & parse DexScreener API data
│   │   ├── coinRoutes.ts    # API endpoints for tokens, wallet creation, and buy simulation
│   │   └── walletManager.ts # Module to generate a new Solana wallet
│   ├── package.json         
│   ├── tsconfig.json        
│   └── Dockerfile           
├── frontend/                # Frontend dashboard (port 8080)
│   ├── index.html           # Main HTML file
│   ├── style.css            # Dashboard styling
│   ├── app.js               # JavaScript to fetch and display token data
│   ├── package.json         # (Optional) For local HTTP server configuration
│   └── Dockerfile           
└── docker-compose.yml       # Docker Compose configuration to run both services together
```

## Features

- **Live API Integration:**  
  The backend retrieves the latest token profiles from DexScreener, parsing the response into individual arrays (icons, token addresses, descriptions, etc.) and delivering a comprehensive JSON object to the frontend.

- **Data Parsing & Transformation:**  
  The raw JSON from DexScreener is processed into an easy-to-consume format that powers our dynamic token dashboard.

- **Docker & Docker Compose:**  
  The entire application is containerized using Docker. Docker Compose is used to run the backend (port 3000) and frontend (port 8080) concurrently, ensuring consistent environments across development and deployment.

- **Solana Wallet Integration (Simulated):**  
  A demo endpoint for generating a new Solana wallet is provided, demonstrating basic blockchain integration.

## Getting Started

### Prerequisites

- [Docker Desktop](https://docs.docker.com/get-docker/) (includes Docker Compose)
- (Optional) Node.js and npm for local development without Docker

### Running with Docker Compose

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MikeMorrison1996/meme.ai.git
   cd meme.ai
   ```

2. **Build and Start Containers**

   From the project root, run:

   ```bash
   docker-compose up --build
   ```

   This command will:
    - Build Docker images for both the backend and frontend.
    - Start the backend server on port **3000**.
    - Start the frontend server on port **8080**.

3. **Access the Application**

    - **Dashboard (Frontend):** [http://localhost:8080](http://localhost:8080)
    - **API Endpoint (Backend):** [http://localhost:3000/api/coins](http://localhost:3000/api/coins)

### Running Locally Without Docker (Optional)

#### Backend

1. Navigate to the backend folder:

   ```bash
   cd backend
   npm install
   npm run dev
   ```

   The backend server will start on port 3000.

#### Frontend

2. In a new terminal window/tab, navigate to the frontend folder and start a static server:

   ```bash
   cd ../frontend
   npx http-server -p 8080
   ```

   Open [http://localhost:8080](http://localhost:8080) in your browser.

## Future Enhancements

- **Detailed Token Views:**  
  Expand the dashboard to include a detailed view (or modal) for each token with charts (e.g., using Chart.js) and historical data.

- **Advanced Transaction Simulation:**  
  Integrate simulated buy functionality and real blockchain transaction flows with the Solana network.

- **Enhanced UI/UX:**  
  Implement filters, sorting, and responsive design improvements to refine the user experience.

- **Authentication & Security:**  
  Add user authentication and secure wallet management for production-level application security.

## Contributing

This project is a collaborative effort by the Meme.ai team. Contributions, suggestions, and pull requests are welcome. Please open issues or submit improvements as you see fit.

