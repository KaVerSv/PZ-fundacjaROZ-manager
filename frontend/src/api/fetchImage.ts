async function fetchImage(url: string): Promise<string> {
    try {
        // Make the fetch request to get the image data
        const response = await fetch(url,{
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem("token")}`,
            },
        });
        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`Failed to fetch image: ${response.statusText}`);
        }

        // Convert the image data to a Blob object
        const imageBlob = await response.blob();

        // Create a URL for the Blob object
        return URL.createObjectURL(imageBlob);
    } catch (error) {
        // Handle any errors
        console.error('Error fetching image:', error);
        throw error;
    }
}

export default fetchImage;