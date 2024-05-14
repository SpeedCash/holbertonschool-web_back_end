// Import functions that return promises from the utils.js module
import { uploadPhoto, createUser } from './utils';

/**
 * Handles the signup process by managing multiple asynchronous tasks.
 * This function uses Promise.all to wait for both uploading a photo and creating a user profile.
 * Upon successful resolution of both, it logs specific user details to the console.
 * If any of the promises fail, it logs an error message indicating the system is offline.
 */
function handleProfileSignup() {
    // Using Promise.all to handle multiple promises concurrently
    Promise.all([uploadPhoto(), createUser()])
        .then(([photoResponse, userResponse]) => {
            // When both promises resolve successfully, log the results
            console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
        })
        .catch(() => {
            // If any promise fails, log an error message
            console.log('Signup system offline');
        });
}

// Export the function to make it available for import in other files
export default handleProfileSignup;
