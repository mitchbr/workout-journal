<template>
  <div class="activity-tile">
    {{ props.activity.title }}
  </div>
</template>

<script lang="ts" setup>
  const props = defineProps({
    activity: { type: Object, default:  () => ({title: "Rest"}) },
  })
</script>

<style>

</style>