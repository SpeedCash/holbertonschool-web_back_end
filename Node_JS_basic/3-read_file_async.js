const fs = require('fs');

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
      console.log(`Number of students: ${totalStudents}`);

      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const count = fields[field].length;
          const list = fields[field].join(', ');
          console.log(`Number of students in ${field}: ${count}. List: ${list}`);
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
