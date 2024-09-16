const http = require('http');
const fs = require('fs');
const { parse } = require('path');

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

// Création du serveur HTTP
const app = http.createServer(async (req, res) => {
  const { url } = req;

  if (url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    
    const databasePath = process.argv[2];  // Le chemin vers la base de données CSV est passé en argument

    try {
      const studentData = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentData}`);
    } catch (err) {
      res.end('This is the list of our students\nCannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
