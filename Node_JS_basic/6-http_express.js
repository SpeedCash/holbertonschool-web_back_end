const express = require('express');

// Créer l'application Express
const app = express();

// Route pour l'URL racine "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
