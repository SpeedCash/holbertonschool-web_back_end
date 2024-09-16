const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const content = data.trim().split('\n').slice(1); // Enlever la première ligne (header)
      const students = content.filter(line => line).map(line => line.split(','));
      const fields = {};

      students.forEach((student) => {
        const field = student[3]; // La colonne 4 contient le champ (field)
        const firstname = student[0]; // La colonne 1 contient le prénom (firstname)

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
}

module.exports = { readDatabase };
