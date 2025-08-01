<template>
  <div class="skeleton-wrapper">
    <!-- Poster -->
    <div class="skeleton-poster"></div>

    <!-- Info -->
    <div class="skeleton-info">
      <div class="skeleton-title"></div>
      <div class="skeleton-subtitle"></div>
      <div class="skeleton-meta"></div>

      <div class="skeleton-buttons">
        <div class="skeleton-circle"></div>
        <div class="skeleton-button"></div>
      </div>

      <div class="skeleton-tagline"></div>

      <div class="skeleton-overview-title"></div>
      <div class="skeleton-line w-5/6"></div>
      <div class="skeleton-line w-2/3"></div>

      <div class="skeleton-crew mt-6">
        <div class="skeleton-line w-2/4"></div>
        <div class="skeleton-line w-3/4"></div>
        <div class="skeleton-line w-2/3"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skeleton-wrapper {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  max-width: 1280px;
  margin: 0 auto;
  background-color: #0d1b2a; /* exact background match */
}

.skeleton-poster {
  width: 300px;
  height: 440px;
  background: linear-gradient(90deg, #1e2a3a 25%, #243446 50%, #1e2a3a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
  border-radius: 16px;
}

.skeleton-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-top: 0.5rem;
}

.skeleton-title,
.skeleton-subtitle,
.skeleton-meta,
.skeleton-tagline,
.skeleton-overview-title,
.skeleton-line {
  height: 18px;
  border-radius: 6px;
  background: linear-gradient(90deg, #1e2a3a 25%, #243446 50%, #1e2a3a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
}

.skeleton-title {
  width: 70%;
  height: 28px;
}

.skeleton-subtitle {
  width: 50%;
}

.skeleton-meta {
  width: 40%;
}

.skeleton-buttons {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 0.5rem;
}

.skeleton-circle {
  width: 40px;
  height: 40px;
  border-radius: 9999px;
  background: linear-gradient(90deg, #1e2a3a 25%, #243446 50%, #1e2a3a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
}

.skeleton-button {
  width: 120px;
  height: 36px;
  border-radius: 9999px;
  background: linear-gradient(90deg, #1e2a3a 25%, #243446 50%, #1e2a3a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
}

.skeleton-tagline {
  width: 30%;
  height: 16px;
}

.skeleton-overview-title {
  width: 100px;
  height: 20px;
  margin-top: 1.5rem;
}

.skeleton-line {
  margin-top: 0.4rem;
}

.skeleton-crew .skeleton-line {
  margin-top: 0.6rem;
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}
</style>
