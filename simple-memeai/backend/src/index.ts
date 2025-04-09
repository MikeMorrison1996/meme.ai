import express from 'express';
import cors from 'cors';
import coinRoutes from './coinRoutes';

const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS for all routes
app.use(cors());

app.use(express.json());

// Optional: Define a root route to show a welcome message
app.get('/', (req, res) => {
    res.send('Welcome to the Meme.ai backend API! Try accessing /api/coins');
});

// Mount coinRoutes under /api/coins
app.use('/api/coins', coinRoutes);

app.listen(PORT, () => {
    console.log(`Backend server is running on port ${PORT}`);
});
