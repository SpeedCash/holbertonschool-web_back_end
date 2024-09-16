const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');
    
    // Enlever l'en-tête et filtrer les lignes vides
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
 } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
