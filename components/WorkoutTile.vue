<template>
  <div>
    <div v-if="workout.title === 'Rest'" class="rest-tile">
      <v-row align="center" justify="start">
        <v-col cols="auto">
          <div class="text-h6">
            {{ workout.title }}
          </div>
        </v-col>
      </v-row>
    </div>
    <div v-if="workout.title !== 'Rest'" class="workout-tile" :style="{ borderBottom: !isLastItem ? '1px solid grey' : '' }">
      <v-row align="center" justify="start">
        <v-col cols="auto">
          <div class="text-h6">
            {{ workout.title }}
          </div>
        </v-col>
        <v-col cols="auto">
          <AddExercise :workout=workout />
        </v-col>
      </v-row>
      <ul>
        <li v-for="(exercise, index) in workout.exercises" :key="index">
          <div class="text-h6">{{ exerciseTileText(exercise) }}</div>
          <div v-if="exercise.note" class="note-list-item text-h7">{{ exercise.note }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
  import { Exercise } from '../types';
  export default {
    props: {
      workout: {
        type: Object,
        default () {
          return {title: "Rest"}
        }
      },
      isLastItem: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      exerciseTileText (exercise: Exercise) {
        let exerciseText = ''
        exerciseText += exercise.title ? `${ exercise.title } ` : ''
        if (exercise.info.distance) {
          exerciseText += `${exercise.info.distance}mi `
        } else if (exercise.info.weight || exercise.info.reps) {
          exerciseText += exercise.info.weight ? `${exercise.info.weight}lb ` : ''
          exerciseText += exercise.info.reps ? `${exercise.info.reps}r ` : ''
        }
        exerciseText += exercise.location ? `@ ${exercise.location}` : ''
        return exerciseText
      }
    }
  }
</script>

<style>
  .workout-tile {
    margin-top: 0.5rem;
    margin-right: 1rem;
    padding: 0.5rem;
  }
  .note-list-item {
    font-style: italic;
    padding-left: 0.5rem;
  }
</style>