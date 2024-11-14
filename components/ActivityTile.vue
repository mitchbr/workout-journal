<template>
  <v-row align="center" justify="start">
    <v-col cols="auto">
      <div class="text-h6">
        {{ props.activity.title }}
      </div>
    </v-col>
    <v-col v-if="props.activity.title !== 'Rest'" cols="auto">
      <v-btn>
        Add Exercise
      </v-btn>
    </v-col>
  </v-row>
</template>

<script lang="ts" setup>
  const props = defineProps({
    activity: { type: Object, default:  () => ({title: "Rest"}) },
  })
</script>

<style>

</style>