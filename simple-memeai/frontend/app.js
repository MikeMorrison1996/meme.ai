async function loadCoins() {
    const coinListElem = document.getElementById('coin-list');
    try {
        const response = await fetch('http://localhost:3000/api/coins');
        console.log('Fetch response:', response);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data);

        // Clear the "Loading coins..." message
        coinListElem.innerHTML = '';

        // Check that data.tokens is an array
        if (data && Array.isArray(data.tokens)) {
            data.tokens.forEach(token => {
                const card = document.createElement('div');
                card.className = 'coin-card';

                if (token.icon) {
                    const img = document.createElement('img');
                    img.src = token.icon;
                    img.alt = token.tokenAddress || 'Token Icon';
                    img.className = 'coin-icon';
                    card.appendChild(img);
                }

                const details = document.createElement('div');
                details.className = 'coin-details';

                const desc = document.createElement('p');
                desc.textContent = token.description ? token.description : token.tokenAddress;
                details.appendChild(desc);

                if (token.url) {
                    const link = document.createElement('a');
                    link.href = token.url;
                    link.target = '_blank';
                    link.textContent = 'View on DexScreener';
                    details.appendChild(link);
                }

                card.appendChild(details);
                coinListElem.appendChild(card);
            });
        } else {
            coinListElem.textContent = 'No coin data found.';
        }
    } catch (err) {
        console.error('Error fetching coins:', err);
        coinListElem.textContent = 'Error loading coins: ' + err.message;
    }
}

document.addEventListener('DOMContentLoaded', loadCoins);
