const express = require('express');
const routes = require('./routes/index');

const app = express();

// Utiliser les routes
app.use('/', routes);

// Le serveur écoute sur le port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

export default app;
