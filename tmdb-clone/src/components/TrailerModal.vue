<template>
  <div>
    <button
      @click="$emit('open')"
      class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded shadow-md transition"
    >
      ▶️ Play Trailer
    </button>
  </div>
</template>

<script setup>
defineEmits(['open']);
</script>
