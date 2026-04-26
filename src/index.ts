import defaultDeckHtml from '../aseva-sales-deck.html';
import liveDeckHtml from '../aseva-sales-deck-live.html';
import staffingworldDeckHtml from '../prospect-staffingworld-deck.html';
import monsterEnergyDeckHtml from '../prospect-monster-energy-deck.html';
import localSmbDeckHtml from '../prospect-local-smb-deck.html';

const HTML_HEADERS = {
  'Content-Type': 'text/html;charset=UTF-8',
  'Cache-Control': 'no-store',
};

// Add prospect deck imports and routes here:
// import acmeDeckHtml from '../prospect-acme-deck.html';
// '/acme': acmeDeckHtml,
const routes: Record<string, string> = {
  '/': defaultDeckHtml,
  '/live': liveDeckHtml,
  '/staffingworld': staffingworldDeckHtml,
  '/monster-energy': monsterEnergyDeckHtml,
  '/local-smb': localSmbDeckHtml,
};

export default {
  fetch(request: Request) {
    const url = new URL(request.url);
    const html = routes[url.pathname] ?? routes['/'];
    return new Response(html, { headers: HTML_HEADERS });
  },
};
