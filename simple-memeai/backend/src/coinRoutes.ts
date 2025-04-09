// backend/src/coinRoutes.ts
import { Router, Request, Response } from 'express';
import { fetchCoinData } from './dexScreener';
import { createNewWallet } from './walletManager';

const router = Router();

/**
 * GET /api/coins
 * Fetch token profiles from DexScreener, parsed into multiple arrays.
 */
router.get('/', async (req: Request, res: Response): Promise<void> => {
    try {
        const coinData = await fetchCoinData();
        res.json(coinData);
    } catch (error) {
        console.error('Error in /api/coins:', error);
        res.status(500).json({ error: 'Unable to fetch coin data' });
    }
});

/**
 * GET /api/coins/create-wallet
 * Create a new Solana wallet for the user.
 */
router.get('/create-wallet', (req: Request, res: Response): void => {
    const wallet = createNewWallet();
    res.json(wallet);
});

/**
 * POST /api/coins/buy
 * Simulate buying a coin.
 */
router.post('/buy', (req: Request, res: Response): void => {
    const { coinId, walletPublicKey } = req.body;
    if (!coinId || !walletPublicKey) {
        res.status(400).json({ error: 'coinId and walletPublicKey are required' });
        return;
    }
    res.json({ success: true, coinId, walletPublicKey, message: 'Purchase simulated!' });
});

export default router;
