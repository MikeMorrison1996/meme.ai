import { Keypair } from '@solana/web3.js';

/**
 * createNewWallet
 * @returns {object} An object containing the public key and secret key (hex-encoded).
 */
export const createNewWallet = () => {
    // Generate a new key pair.
    const wallet = Keypair.generate();
    return {
        publicKey: wallet.publicKey.toString(),
        // Note: In production, you should NEVER expose the secretKey.
        secretKey: Buffer.from(wallet.secretKey).toString('hex'),
    };
};
