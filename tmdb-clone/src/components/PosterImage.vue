<template>
  <img
    :src="poster"
    alt="Movie Poster"
    class="w-40 md:w-60 rounded-lg shadow-lg"
  />
</template>

<script setup>
defineProps({ poster: String });
</script>
