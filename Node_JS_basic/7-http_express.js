const express = require('express');
const fs = require('fs');

// Fonction pour lire et traiter le fichier CSV
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter(line => line);

      const totalStudents = students.length;
      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      let result = `Number of students: ${totalStudents}\n`;
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const count = fields[field].length;
          const list = fields[field].join(', ');
          result += `Number of students in ${field}: ${count}. List: ${list}\n`;
        }
      }

      resolve(result.trim());
    });
  });
}

// Créer l'application Express
const app = express();

// Route pour l'URL racine "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route pour "/students"
app.get('/students', async (req, res) => {
  const databasePath = process.argv[2];  // Le fichier CSV est passé en argument de la ligne de commande

  if (!databasePath) {
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  try {
    const studentData = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentData}`);
  } catch (err) {
    res.send('This is the list of our students\nCannot load the database');
  }
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
