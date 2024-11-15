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
        <v-btn size="small" @click="addWorkout(props.workoutIndex)">Add</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts" setup>
  const props = defineProps({
    workoutIndex: {
      type: Number,
      required: true
    },
  })
</script>

<script lang="ts">
  export default {
    data () {
      return {
        selectedWorkout: "",
      }
    },
    methods: {
      addWorkout (workoutIndex: number) {
        if ((this as any).selectedWorkout !== "") {
          (this as any).$store.commit('setWorkoutSchedule', {"title": (this as any).selectedWorkout, "index": workoutIndex-1})
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
