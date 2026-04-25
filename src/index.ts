import defaultDeckHtml from '../aseva-sales-deck.html';
import staffingworldDeckHtml from '../prospect-staffingworld-deck.html';
import monsterEnergyDeckHtml from '../prospect-monster-energy-deck.html';

const HTML_HEADERS = {
  'Content-Type': 'text/html;charset=UTF-8',
  'Cache-Control': 'public, max-age=86400',
};

// Add prospect deck imports and routes here:
// import acmeDeckHtml from '../prospect-acme-deck.html';
// '/acme': acmeDeckHtml,
const routes: Record<string, string> = {
  '/': defaultDeckHtml,
  '/staffingworld': staffingworldDeckHtml,
  '/monster-energy': monsterEnergyDeckHtml,
};

export default {
  fetch(request: Request) {
    const url = new URL(request.url);
    const html = routes[url.pathname] ?? routes['/'];
    return new Response(html, { headers: HTML_HEADERS });
  },
};
