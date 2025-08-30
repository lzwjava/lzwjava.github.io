  window.addEventListener('load', function () {
    const sortSelect = document.getElementById('sort-select');
    const postNumber = document.getElementById('post-number');
    const postList = document.querySelector('.post-list');

    // Count and display posts
    const posts = document.querySelectorAll('.post-list li.post-item');
    const translatedCount = Array.from(posts).filter(post => post.dataset.translated === 'true').length;
    postNumber.innerHTML = `${posts.length} (${translatedCount} Translated by <a href="https://mistral.ai">AI</a>)`;

    // Restore from localStorage if available
    const savedLang = localStorage.getItem('selectedLanguage');
    if (savedLang) {
      sortSelect.value = savedLang;
    }

    // Event listener for dropdown changes
    sortSelect.addEventListener('change', function () {
      const selectedLang = sortSelect.value;

      // Save to localStorage
      localStorage.setItem('selectedLanguage', selectedLang);

      // Redirect to appropriate page
      if (selectedLang === 'en') {
        window.location.href = '/';
      } else {
        window.location.href = `/index-${selectedLang}.html`;
      }
    });

  });