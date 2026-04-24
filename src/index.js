import deckHtml from '../aseva-sales-deck.html';

export default {
  fetch(request) {
    return new Response(deckHtml, {
      headers: {
        'Content-Type': 'text/html;charset=UTF-8',
        'Cache-Control': 'public, max-age=86400',
      },
    });
  },
};
