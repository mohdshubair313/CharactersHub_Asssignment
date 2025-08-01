<template>
  <div class="space-y-1">
    <h1 class="text-3xl md:text-4xl font-bold text-white">
      {{ title }} <span class="text-gray-400 font-normal">({{ year }})</span>
    </h1>
    <p class="text-sm text-gray-300">
      {{ release }} • {{ genre }} • {{ runtime }}
    </p>
  </div>
</template>

<script setup>
defineProps({ title: String, year: String, release: String, genre: String, runtime: String });
</script>
