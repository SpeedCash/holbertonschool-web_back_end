// 1-block-scoped.js

export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      // Ici, nous utilisons des variables distinctes avec 'let'
      task = true;
      task2 = false;
    }
  
    return [task, task2];
  }
  