/**
 * Returns a promise that rejects with an error message indicating the provided file cannot be processed.
 *
 * @param {string} filename - The name of the file to process.
 * @returns {Promise<never>} A promise that rejects with an error specific to the file.
 */
export default function uploadPhoto(filename) {
    // Return a promise that is immediately rejected with an error including the filename
    return Promise.reject(new Error(`${filename} cannot be processed`));
}
