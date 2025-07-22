---
title: "Optimize Jekyll Site with Static Pages"
lang: en
layout: post
audio: false
translated: false
generated: true
---

### Understanding the Performance Issue

Your Jekyll site is currently rendering a single page (likely `index.html`) that loops over **all** posts across all languages using `{% for post in site.posts %}`. With 518 original posts translated into 9 languages (English, Simplified Chinese, Japanese, Spanish, Hindi, French, German, Arabic, Traditional Chinese), that's indeed around 4,662 posts in total. This generates a massive HTML file with thousands of `<li>` elements in the DOM.

The JavaScript then handles filtering and sorting client-side:
- It grabs all posts, filters by language or criteria (e.g., `lang-en`, `data-translated="false"` for originals).
- For date-desc sorting, it parses dates and sorts in the browser.
- This works for small sites but becomes inefficient here: loading 4,662 DOM nodes upfront causes slow page loads, high memory usage, and sluggish filtering (especially on mobile or slower devices).

Client-side processing is the bottleneck—Jekyll is static, so precomputing as much as possible on the build side is key to optimization.

### Optimization Strategy: Generate Separate Static Pages per Language/Filter

Instead of one monolithic page, use Jekyll's Liquid templating to generate **separate HTML files** for each major filter option (e.g., `index-en.html`, `index-zh.html`, `index-original.html`). This way:
- Each page only includes the relevant ~518 posts (or fewer for originals/picks), reducing file size and DOM elements dramatically.
- Filtering/sorting happens at build time (server-side via Liquid), not client-side.
- Navigation between views becomes a simple page load (faster than JS manipulation).
- You can still use a dropdown, but change it to redirect to the corresponding URL instead of filtering in place.

Benefits:
- Page load times drop significantly (e.g., `index-en.html` only loads 518 English posts).
- No need for complex JS filtering—simplify or remove much of the script.
- Easier to add pagination if needed (via `jekyll-paginate` gem) for the "All" view.
- Build time might increase slightly, but runtime performance improves a lot.
- Keeps the site static and SEO-friendly.

Drawbacks:
- More files in your output directory (but that's fine for hosting).
- "All" view would still be heavy unless paginated.

#### Step 1: Restructure Your Pages
Create a new layout template (e.g., `_layouts/post-list.html`) to reuse the common structure:
```liquid
---
layout: page
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    <!-- We'll compute this in Liquid -->
  </span>
  <select id="sort-select">
    <!-- Options here, but JS will handle redirects -->
  </select>
</div>

<ul class="post-list">
  {% for post in filtered_posts %}
  <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ post.top }}" data-translated="{{ post.translated }}" data-generated="{{ post.generated }}">
    <a href="{{ post.url }}">
      <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
      <span class="title">{{ post.title }}</span>
    </a>
  </li>
  {% endfor %}
</ul>

<!-- Footer remains the same -->

<script>
  // Simplified JS: just handle dropdown redirects, no filtering
  window.addEventListener('load', function () {
    const sortSelect = document.getElementById('sort-select');
    // ... (restore from localStorage, detect lang, etc.)

    sortSelect.addEventListener('change', function () {
      localStorage.setItem('sortOption', sortSelect.value);
      const [sortOption, langFilter] = sortSelect.value.split('|');
      let targetUrl = '';
      if (sortOption === 'author-picks') {
        targetUrl = '/index-picks.html';
      } else if (langFilter === 'all') {
        targetUrl = '/index-all.html';
      } else if (langFilter === 'original') {
        targetUrl = '/index-original.html';
      } else {
        targetUrl = `/index-${langFilter}.html`;
      }
      window.location.href = targetUrl;
    });
  });
</script>
```

Now, create individual pages that use this layout and pre-filter posts:

- **`index-en.html`** (and similarly for zh, ja, es, hi, fr, de, ar, hant):
  ```liquid
  ---
  layout: post-list
  permalink: /index-en.html
  lang: en
  filtered_posts: site.posts | where_exp: "post", "post.path contains '_posts/en/'" | sort: "date" | reverse
  ---
  ```

  - Use `| sort: "date" | reverse` for date-desc sorting at build time.
  - Compute post count in Liquid: `{% assign post_count = filtered_posts | size %}` `{% assign ai_count = filtered_posts | where: "translated", true | size %}` then set `<span id="post-number">{{ post_count }} posts ({{ ai_count }} by <a href="https://mistral.ai">AI</a>)</span>`.

- **`index-original.html`**:
  ```liquid
  ---
  layout: post-list
  permalink: /index-original.html
  lang: original
  filtered_posts: site.posts | where_exp: "post", "post.translated == false and post.generated == false" | sort: "date" | reverse
  ---
  ```

- **`index-picks.html`** (for author's picks):
  ```liquid
  ---
  layout: post-list
  permalink: /index-picks.html
  lang: picks
  filtered_posts: site.posts | where_exp: "post", "post.top > 0" | sort: "top" | reverse  # Assuming higher top = better
  ---
  ```

- **`index-all.html`** (this one might still be large):
  ```liquid
  ---
  layout: post-list
  permalink: /index-all.html
  lang: all
  filtered_posts: site.posts | sort: "date" | reverse
  ---
  ```
  - If it's too slow, add pagination: Install `jekyll-paginate` (add to `_config.yml`: `gems: [jekyll-paginate]`, `paginate: 50`), then use `paginator.posts` instead of `filtered_posts`.

- For the main `index.html`, you could redirect to a default (e.g., based on browser lang) or make it alias to `index-en.html`.

#### Step 2: Update Dropdown and Navigation
- Keep the `<select>` options as-is, but the JS change event now redirects to the pre-generated pages (as shown in the script above).
- To handle query params (your current `?sort=`), you can parse them on load to select the right option, but since we're using separate URLs, it's optional.
- Browser language detection stays the same, but map to URLs like `/index-en.html`.

#### Step 3: Additional Tweaks
- **Build Time Optimization**: If building takes too long, consider parallelizing translations/generation outside Jekyll (e.g., script to generate Markdown files in batches) or use incremental builds (`jekyll build --incremental`).
- **Pagination for Large Views**: For "All" or if any language grows, enable pagination. Example in `index-all.html`:
  ```liquid
  {% for post in paginator.posts %}
  <!-- loop -->
  {% endfor %}
  <!-- Pagination links -->
  {% if paginator.previous_page %}<a href="{{ paginator.previous_page_path }}">Previous</a>{% endif %}
  {% if paginator.next_page %}<a href="{{ paginator.next_page_path }}">Next</a>{% endif %}
  ```
- **Caching**: Host on GitHub Pages/Netlify with caching enabled. Compress images if posts have media.
- **Testing**: Start with one language (e.g., en) to prototype. Run `jekyll serve` and check page sizes (e.g., `index-en.html` should be much smaller).
- **Fallback for No Posts**: Already handled, but move to Liquid if possible.

This approach precomputes everything, reducing client-side work to almost zero. If you need more dynamic features, consider a JS framework like Next.js, but that might overkill for a blog.

If referencing Jekyll docs:
[Jekyll Filters](https://jekyllrb.com/docs/liquid/filters/)
[Jekyll Pagination](https://jekyllrb.com/docs/pagination/)