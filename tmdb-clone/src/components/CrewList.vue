<template>
  <div class="mt-6 space-y-2 text-sm text-white">
    <div><span class="font-semibold text-gray-300">Director:</span> {{ director }}</div>
    <div><span class="font-semibold text-gray-300">Writer:</span> {{ writer }}</div>
    <div><span class="font-semibold text-gray-300">Actors:</span> {{ actors }}</div>
  </div>
</template>

<script setup>
defineProps({ director: String, writer: String, actors: String });
</script>
