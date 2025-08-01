<template>
  <div class="bg-[#0d1b2a] min-h-screen">
    <SkeletonLoader v-if="loading" />
    <MovieDetail v-else />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SkeletonLoader from './components/SkeletonLoader.vue';
import MovieDetail from './views/MovieDetail.vue';

const loading = ref(true);

onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 2000); // Simulated delay
});
</script>
