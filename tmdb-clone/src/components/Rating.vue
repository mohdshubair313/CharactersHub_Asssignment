<template>
  <div class="rating">
    {{ Math.round(Number(rating) * 10) }}<span class="text-xs">%</span>
  </div>
</template>

<script setup>
defineProps({ rating: String });
</script>
