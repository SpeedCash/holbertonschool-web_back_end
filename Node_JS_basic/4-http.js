const http = require('http');

// Création du serveur HTTP
const app = http.createServer((req, res) => {
  res.statusCode = 200;  // Réponse avec un code 200 (succès)
  res.setHeader('Content-Type', 'text/plain');  // Type de contenu : texte brut
  res.end('Hello Holberton School!');  // Envoie de la réponse
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;  // Exportation du serveur
