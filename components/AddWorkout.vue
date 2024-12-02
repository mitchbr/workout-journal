<template>
  <div class="add-workout">
    <v-row align="center" justify="start">
      <v-col cols="auto">
          <v-select
          v-model="selectedWorkout"
          label="Workout Type"
          :items="['Lift', 'Climb', 'Run', 'Other']"
        ></v-select>
      </v-col>
      <v-col cols="auto">
        <v-btn @click="changeAddForm(-1)">Cancel</v-btn>
      </v-col>
      <v-col cols="auto">
        <v-btn size="small" @click="addWorkout(workoutDate)">Add</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
  export default {
    props: {
      workoutDate: {
        type: Date,
        required: true
      },
      startDate: {
        type: Date,
        required: true
      },
    },
    data () {
      return {
        selectedWorkout: "",
      }
    },
    methods: {
      addWorkout (workoutDate: Date) {
        if ((this as any).selectedWorkout !== "") {
          (this as any).$store.dispatch('addWorkout', {"title": (this as any).selectedWorkout, workoutDate})
            .then(() => {
              (this as any).$store.dispatch('getWorkouts', (this as any).startDate)
            })
        }
      },
      changeAddForm(currentDay: number){
        (this as any).$store.dispatch('updateSelectedDate', currentDay)
      }
    }
  }
</script>

<style>
  .add-workout-controls {
    display: flex;
    gap: 1rem;
  }

  .add-workout-details-form {
    display:flex;
    align-items: center;
  }
</style>
