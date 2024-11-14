<template>
  <div class="container">
    <div class="title">
      <h1>Workout Journal</h1>
    </div>

    <ActivitiesList />

    <div class="bottom-controls">
      <div class="nav-button">
        <button>Previous</button>
      </div>
      <div class="nav-button">
        <button>Next</button>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  export default Vue.extend({
    name: 'IndexPage',
  })
</script>

<style>
  .bottom-controls {
    margin: auto;
    display: flex;
    justify-content: center;
    padding: 0.5rem;
  }

  .title {
    padding: 0.5rem;
    display: flex;
    justify-content: center;
  }

  .nav-button {
    padding: 0.5rem;
  }
</style>