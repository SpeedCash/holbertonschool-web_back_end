// 7-has_array_values.js
export default function hasValuesFromArray(set, arr) {
    return arr.every(value => set.has(value));
  }
  