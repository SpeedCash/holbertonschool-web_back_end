import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

/**
 * Handles profile signup by attempting to sign up a user and upload a photo concurrently.
 * Returns the results of both operations regardless of their individual success or failure.
 *
 * @param {string} firstName - User's first name.
 * @param {string} lastName - User's last name.
 * @param {string} fileName - The file name of the photo to upload.
 * @returns {Promise<Array>} A promise that resolves to an array of results from each operation.
 */
export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([
        signUpUser(firstName, lastName),
        uploadPhoto(fileName)
    ]).then(results => results.map(result => ({
        status: result.status,
        value: result.reason || result.value
    })));
}
