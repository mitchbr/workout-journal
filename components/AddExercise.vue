<template>
  <div class="add-workout-details">
    <ol>
      <li v-if="selectedWorkout === 'Lift'">
        <div class="add-workout-details-form lifting">
          <v-responsive
            class="mx-auto"
            max-width="75"
          >
            <v-text-field label="Weight"></v-text-field>
          </v-responsive>
          lb
          <v-responsive
            class="mx-auto"
            max-width="50"
          >
            <v-text-field label="Reps"></v-text-field>
          </v-responsive>
          r
          <v-btn size="small">Add</v-btn>
        </div>
      </li>
      <li v-if="selectedWorkout === 'Climb'">
        <div class="add-workout-details-form climb">
          <v-select
            label="Type"
            :items="['Boulder', 'Ropes']"
          ></v-select>
          <v-responsive
            class="mx-auto"
            max-width="250"
          >
            <v-text-field label="Location"></v-text-field>
          </v-responsive>
        </div>
      </li>
      <li v-if="selectedWorkout === 'Run'">
        <div class="add-workout-details-form run">
          <v-responsive
            class="mx-auto"
            max-width="250"
          >
            <v-text-field></v-text-field>
          </v-responsive>
          Miles
        </div>
      </li>
      <li v-if="selectedWorkout === 'Other'">
        <div class="add-workout-details-form lifting">
          <v-responsive
            class="mx-auto"
            max-width="250"
          >
            <v-text-field label="Note"></v-text-field>
          </v-responsive>
        </div>
      </li>
    </ol>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>