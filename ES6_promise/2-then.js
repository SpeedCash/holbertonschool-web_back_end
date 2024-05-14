function handleResponseFromAPI(promise) {
    return promise
        .then(() => {
            // Handle successful resolution
            return {
                status: 200,
                body: 'success'
            };
        })
        .catch(() => {
            // Handle rejection
            return new Error();
        })
        .finally(() => {
            // Log on every resolution
            console.log('Got a response from the API');
        });
}

// Export the function as required by the project specifications
export default handleResponseFromAPI;
