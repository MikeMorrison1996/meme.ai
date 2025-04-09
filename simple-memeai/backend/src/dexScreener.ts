// backend/src/dexScreener.ts
import axios from 'axios';

const DEXSCREENER_TOKEN_PROFILES_URL = 'https://api.dexscreener.com/token-profiles/latest/v1';

/**
 * fetchCoinData
 * Fetch the latest token profiles from DexScreener and transform the response.
 * @returns {Promise<any>} An object containing arrays for icons, tokenAddresses, descriptions, urls, and the full tokens array.
 */
export const fetchCoinData = async (): Promise<any> => {
    try {
        const response = await axios.get(DEXSCREENER_TOKEN_PROFILES_URL);
        const rawData: any[] = response.data; // assuming the response is an array

        // Transform rawData into separate arrays
        const icons = rawData.map(token => token.icon || '');
        const tokenAddresses = rawData.map(token => token.tokenAddress || '');
        const descriptions = rawData.map(token => token.description || token.tokenAddress || '');
        const urls = rawData.map(token => token.url || '');

        // Return an object with the arrays and the raw tokens for flexibility
        return {
            icons,
            tokenAddresses,
            descriptions,
            urls,
            tokens: rawData
        };
    } catch (error) {
        console.error('Error fetching token profiles:', error);
        throw new Error('Failed to fetch token profiles');
    }
};
