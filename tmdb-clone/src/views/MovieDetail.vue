<template>
  <div class="movie-detail">
    <div class="container">
      <!-- Poster -->
      <div class="poster">
        <PosterImage :poster="movie.Poster" />
      </div>

      <!-- Content -->
      <div class="content">
        <MovieInfo
          :title="movie.Title"
          :year="movie.Year"
          :release="movie.Released"
          :genre="movie.Genre"
          :runtime="movie.Runtime"
        />

        <div class="rating-and-trailer">
          <Rating :rating="movie.imdbRating" />
          <TrailerModal @open="showTrailer = true" />
          <!-- Trailer Modal -->
          <div
            v-if="showTrailer"
            class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-50"
          >
            <div class="relative w-full max-w-3xl mx-auto aspect-video">
              <iframe
                :src="trailerUrl"
                frameborder="0"
                allow="autoplay; encrypted-media"
                allowfullscreen
                class="w-full h-full rounded"
              ></iframe>
              <button
                @click="showTrailer = false"
                class="absolute top-2 right-2 bg-white text-black rounded-full px-3 py-1"
              >
                ✖
              </button>
            </div>
          </div>
        </div>


        <p class="tagline">Obviously.</p>

        <div class="overview">
          <h2>Overview</h2>
          <p>{{ movie.Plot }}</p>
        </div>

        <CrewList
          :director="movie.Director"
          :writer="movie.Writer"
          :actors="movie.Actors"
        />
      </div>
    </div>
  </div>
</template>


<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import PosterImage from '../components/PosterImage.vue';
import MovieInfo from '../components/MovieInfo.vue';
import Rating from '../components/Rating.vue';
import TrailerModal from '../components/TrailerModal.vue';
import CrewList from '../components/CrewList.vue';

const movie = ref({});
const trailerUrl = ref('');
const showTrailer = ref(false); // for modal control

const fetchTrailer = async (title) => {
  const apiKey = import.meta.env.GOOGLE_API_KEY;
  const query = `${title} official trailer`;
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(query)}&key=${apiKey}&type=video&maxResults=1`;

  try {
    const response = await axios.get(url);
    const videoId = response.data.items[0]?.id.videoId;
    if (videoId) {
      trailerUrl.value = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
    }
  } catch (err) {
    console.error('Failed to fetch trailer:', err);
  }
};

onMounted(async () => {
  const res = await fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124');
  movie.value = await res.json();
  await fetchTrailer(movie.value.Title); // fetch trailer once movie is fetched
});
</script>
