// This JavaScript code is intended to be embedded within a Markdown file.
// It assumes the presence of a function (e.g., in a separate script)
// that can fetch and process data from m.cn.nytimes.com.

// Example usage (assuming you have a way to fetch the data):
// <script>
//   fetchNYTimesLinks();
// </script>

// <script async src="../assets/js/nytimes.js"></script>
// <div class="nytimes" ></div> 

function updateDivText(text) {
  const targetElement = document.querySelector('.nytimes');
  if (targetElement) {
    targetElement.innerHTML = text;
  } else {
    console.error('Target element with class "nytimes" not found.');
  }
}

function fetchNYTimesLinks() {
  const nytimesUrl = 'https://m.cn.nytimes.com';
  console.log('Fetching NYTimes links from:', nytimesUrl);
  updateDivText('Loading...');

  fetchHtmlContent(nytimesUrl)
    .then(html => {
      console.log('HTML content fetched successfully.');
      const links = extractLinks(html);
      updateDivText(`Found ${links.length} links on main page. Extracting links...`);

      Promise.all(links.map((link, index) => {
        updateDivText(`Processing link ${index + 1} of ${links.length}...`);
        return fetchHtmlContent(link.url)
          .then(html => {
            updateDivText(`Extracting NYTimes links from ${link.url}...`);
            return extractNYTimesLinks(html);
          })
          .then(nytimesLinks => {
            updateDivText(`Found ${nytimesLinks.length} NYTimes links in ${link.url}.`);
            return { ...link, nytimesLinks };
          })
          .catch(error => {
            console.error(`Error processing link ${link.url}:`, error);
            updateDivText(`Error processing link ${link.url}.`);
            return { ...link, nytimesLinks: [] };
          });
      }))
      .then(processedLinks => {
        updateDivText('Filtering links...');
        const allNYTimesLinks = processedLinks.flatMap(link => link.nytimesLinks);
        const filteredLinks = allNYTimesLinks.filter(link => link.text.includes('本文英文版'));
        updateDivText(`Found ${filteredLinks.length} links containing '本文英文版'. Generating list...`);
        const markdownList = generateMarkdownList(filteredLinks);

        updateDivText(''); // Clear loading message before inserting list
        const targetElement = document.querySelector('.nytimes');
        if (targetElement) {
          targetElement.innerHTML = markdownList;
        }
      })
      .catch(error => {
        console.error('Error processing links:', error);
        updateDivText('Error processing links.');
      });
    })
    .catch(error => {
      console.error('Error fetching or processing data:', error);
      updateDivText('<p>Error fetching data from NYTimes.</p>');
    });
}

async function fetchHtmlContent(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      console.error('HTTP error! status:', response.status);
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.text();
  } catch (error) {
    console.error("Could not fetch URL:", url, error);
    throw error;
  }
}


function extractLinks(html) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const links = [];

  const allLinks = doc.querySelectorAll('a');

  allLinks.forEach(link => {
    const url = link.href;
    if (url.startsWith('https://cn.nytimes.com/')) {
      links.push({
        url: url,
        text: link.textContent.trim()
      });
    }
  });

  return links;
}

function extractNYTimesLinks(html) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const links = [];

  const allLinks = doc.querySelectorAll('a');

  const titleElement = doc.querySelector('.article-area .article-content .article-header header h1');
  const title = titleElement ? titleElement.textContent.trim() : '';

  allLinks.forEach(link => {
    const url = link.href;
    if (url.startsWith('https://www.nytimes.com/')) {
      links.push({
        url: url,
        title: title,
        text: link.textContent.trim()
      });
    }
  });

  return links;
}


function generateMarkdownList(links) {
  let markdownList = '';
  if (links.length > 0) {
    markdownList = '<ul>\n';
    links.forEach(link => {
      markdownList += `  <li><a href="${link.url}">${link.title}</a></li>\n`;
    });
    markdownList += '</ul>\n';
  } else {
    markdownList = '<p>No links found.</p>';
  }
  return markdownList;
}

fetchNYTimesLinks();
