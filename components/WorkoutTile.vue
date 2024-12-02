<template>
  <div>
    <div class="rest-tile">
      <v-row v-if="workout.title === 'Rest'" align="center" justify="start">
        <v-col cols="auto">
          <div class="text-h6">
            {{ workout.title }}
          </div>
        </v-col>
      </v-row>
    </div>
    <div v-if="workout.title !== 'Rest'" class="workout-tile">
      <v-row v-if="workout.title !== 'Rest'" align="center" justify="start">
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
          <p>{{ exerciseTileText(exercise) }}</p>
          <ul v-if="exercise.note">
            <li><p>{{ exercise.note }}</p></li>
          </ul>
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
    border: 2px solid grey;
    border-radius: 7px;
    margin-top: 0.5rem;
    padding: 0.5rem;
  }
</style>