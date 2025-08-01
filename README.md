## Task:

### Implement an API endpoint for the scenario below:

- Imagine that a frontend design has been drafted to present data that we already have in our DB: `Posts` and `Comments`. 

  * The design is an infinite scrolling list of `Posts`.

- The list of `Posts` should be ordered by timestamp, latest first. 

- Some `Posts` will have `Comments`. 

- For each `Post` in this list, we want to show up to 3 `Comments` for that `Post` (`Comments` also sorted latest first).

  * For each `Post`: we will need to display a `Post`'s text, timestamp, `Comment` count, and author's username.

  * For `Comments`: we will need to display a `Comment`'s text, timestamp, and author's username.

- Include basic documentation on how to use your new endpoint.

### Follow-up Q: 
- Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post?
  * You can leave your answer anywhere in the project codebase that you deem appropriate.
 
    ** I comment this in my 
---

## To get started:

1. Set up a virtualenv for this project (The author used Python 3.10.14)

- Example: `pyenv local myvirtualenv` (or however you set up Python virtualenvs)

2. Install dependencies: `pip install -r requirements.txt`

3. Migrate database `python manage.py migrate`

4. Now head to apps/demo/views.py and complete the assignment!

- Run tests via `python manage.py test apps` or
- check server after running via `python manage.py runserver`

Backend Work completed

"""
GET /api/posts/

Returns a paginated list of posts.
Each post contains:
- post text
- timestamp
- author's username
- total comment count
- up to 3 latest comments with text, timestamp, and username

Query Params:
- page (int): page number
- page_size (int): items per page (optional)

Sample Response:
{
    "count": 25,
    "next": "...",
    "results": [
        {
            "id": "UUID...",
            "text": "Hello world!",
            "timestamp": "2025-07-30T12:00:00Z",
            "user": "john_doe",
            "comment_count": 5,
            "comments": [
                {
                    "text": "Nice post!",
                    "timestamp": "...",
                    "user": "jane"
                }
            ]
        }
    ]
}
"""

"""
GET /admin
We can do all the CRUD basic operations and can create all the posts
"""

"""I had designed this page to display crew details in an engaging, card-based layout that enhances both the UI and UX with a modern aesthetic. However, I didn’t include it in the assignment submission. I'm sharing the screenshot here to showcase the approach I had explored.
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/5380c0ac-db10-4747-bd8f-673942e1200c" />
"""

Here's your full `README.md` in clean **Markdown format** — ideal for GitHub or any assignment submission. You can copy and paste this directly into your project:

---

````markdown
# 🎬 Movie Detail Page - TMDB Inspired Layout

This is a frontend assignment project that replicates the **above-the-fold layout** of the _Guardians of the Galaxy Vol. 2_ detail page on TMDB. It is built using **Vue.js**, **CSS3**, and **responsive design principles** to ensure an elegant experience across devices (desktop, tablet, and mobile).

---

## 📸 Project Preview

Go to the tmdb-clone directory

---

## 🚀 Features

- 📱 Fully **responsive layout** (mobile, tablet, desktop)
- 🎞️ Movie poster, backdrop, title, tagline, genres, ratings, and overview
- 🔘 Styled “Play Trailer” button for interaction
- 📂 Modular and clean component-based Vue structure
- 🎨 Sleek UI/UX for modern streaming platforms

---

## 🧠 Technologies Used

- **Vue.js 3 (Composition API)**
- **YouTube Data API v3** for fetching trailers
- **Axios** for API calls
- **CSS3** for styling
- **Skeleton Loaders** for improved user experience

---

## ✨ Noteworthy Improvements

### 🔹 1. Skeleton Loader for Seamless UI Experience

A modern **skeleton loader** was implemented across the app to indicate content is loading. This improves the **perceived speed** of the app and provides a smoother experience instead of showing blank white screens.

```vue
<!-- Example -->
<SkeletonLoader v-if="isLoading" />
<MovieDetails v-else />
````

---

### 🔹 2. Interactive Trailer Button with YouTube Integration

When the user clicks on the **"Play Trailer"** button, a popup modal opens and automatically plays the corresponding movie trailer using the **YouTube Data API**. This was done by dynamically fetching the trailer video ID based on the movie title.

```js
// Example YouTube search logic
const fetchTrailer = async () => {
  const res = await axios.get(`https://www.googleapis.com/youtube/v3/search`, {
    params: {
      part: 'snippet',
      q: `${movieTitle} official trailer`,
      key: YOUTUBE_API_KEY,
      maxResults: 1,
      type: 'video',
    },
  });
  trailerVideoId.value = res.data.items[0]?.id.videoId;
};
```

---

## 📱 Responsiveness

Special attention was given to responsive design:

* 📏 Media queries for mobile, tablet, and large screens
* 🎯 Content adjusts layout, size, and visibility accordingly
* ✅ Perfect pixel spacing and alignment with TMDB reference

---

## 📂 Project Structure

```bash
├── public/
├── src/
│   ├── components/
│   ├── views/
│   ├── App.vue
│   └── main.js
├── .env
└── README.md
```

---

## 💡 AI Usage (If Applicable)

If AI tools were used (like ChatGPT, GitHub Copilot, etc.), they were utilized for:

* Optimizing component structures
* Writing or refining functions
* Suggesting UI best practices
* Reviewing final UI polish ideas

---

## 📽️ Loom Demo (Optional)

You can record a quick <5 min Loom video showing:

* Desktop to mobile view switch
* How trailer video loads dynamically
* Where skeleton loaders improve UX
* Any AI-assisted code explanations

---

## 📌 Installation Guide

```bash
npm install
npm run dev
```

---

## 📃 License

This project is submitted as part of a frontend assignment. Feel free to fork or use for learning purposes.

---

```

Let me know if you want to change the tone (more casual, more academic), or if you’d like help with the Loom video script too.
```



