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
        <v-btn size="small" @click="addWorkout()">Add</v-btn>
      </v-col>
    </v-row>
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
  </div>
</template>

<script lang="ts">
  export default {
    data () {
      return {
        selectedWorkout: "",
      }
    },
    methods: {
      addWorkout () {
        if ((this as any).selectedWorkout !== "") {
          (this as any).$store.commit(
            'setWorkoutSchedule',
            {"title": (this as any).selectedWorkout, "date": (this as any).$store.state.selectedDate}
          )
          (this as any).$store.commit('setSelectedDate', -1)
        }
      },
      changeAddForm(currentDay: string){
        (this as any).$store.commit('setSelectedDate', currentDay)
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
