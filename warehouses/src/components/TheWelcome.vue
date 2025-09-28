
<template>
  <div class="welcome-item">
    <slot name="icon"></slot>
    <div class="details">
      <h3><slot name="heading"></slot></h3>
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.welcome-item {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
}

.details {
  flex: 1;
}

h3 {
  font-size: 1.2rem;
  margin-bottom: 0.4rem;
}
</style>
