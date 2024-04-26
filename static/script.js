// JavaScript code for search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-bar input[type="text"]');
    const searchButton = document.querySelector('.search-bar button');

    searchButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission

        const searchTerm = searchInput.value.trim().toLowerCase();
        const posts = document.querySelectorAll('.post');

        posts.forEach(function(post) {
            const postTitle = post.querySelector('h3').textContent.toLowerCase();
            const postContent = post.querySelector('p').textContent.toLowerCase();

            if (postTitle.includes(searchTerm) || postContent.includes(searchTerm)) {
                post.style.display = 'block';
            } else {
                post.style.display = 'none';
            }
        });
    });
});
