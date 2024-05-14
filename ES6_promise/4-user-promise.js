// Import necessary functions or dependencies if needed (not applicable here)

/**
 * Returns a promise that resolves with user's first and last names.
 * This function simulates a successful signup operation.
 *
 * @param {string} firstName - The first name of the user.
 * @param {string} lastName - The last name of the user.
 * @returns {Promise<Object>} A promise that resolves with an object containing user details.
 */
function signUpUser(firstName, lastName) {
    // Creating and returning a promise that immediately resolves with user details
    return Promise.resolve({
        firstName: firstName,
        lastName: lastName
    });
}

// Export the function to make it available for import in other files
export default signUpUser;
