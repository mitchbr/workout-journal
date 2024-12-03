<template>
  <div>
    <ol>
      <li v-for="dateOffset in 7" :key="dateOffset" class="schedule-day">
        <div class="schedule-title">
          <v-row align="center" justify="space-between">
            <v-col cols="auto">
              <div class="text-h5">
                {{ dateToDisplay(calcDate(startDate, dateOffset-1)) }}
              </div>
            </v-col>
            <v-col cols="auto">
              <v-icon @click="changeAddForm(dateOffset)">
                mdi-plus-circle-outline
              </v-icon>
            </v-col>
          </v-row>
        </div>
          <ul class="schedule-activities-list">
            <li v-if="workoutSchedule[dateOffset-1].activities.length === 0 && dateOffset !== $store.state.selectedDate">
              <div class="rest">
                <WorkoutTile />
              </div>
            </li>
            <li v-for="(workout, index) in workoutSchedule[dateOffset-1].activities" :key="index">
              <WorkoutTile :workout=workout :is-last-item="index === workoutSchedule[dateOffset-1].activities.length-1 && dateOffset !== $store.state.selectedDate" />
            </li>
            <li v-if="dateOffset === $store.state.selectedDate">
              <AddWorkout :workout-date="calcDate(startDate, dateOffset-1)" :start-date="startDate" />
            </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script lang="ts">
  export default {
    props: {
      startDate: {
        type: Date,
        required: true
      },
    },
    computed: {
      workoutSchedule() {
        return (this as any).$store.state.workoutSchedule
      }
    },
    methods: {
      changeAddForm(currentDay: number){
        (this as any).$store.dispatch('updateSelectedDate', currentDay)
      },
      dateToDisplay(value: Date) {
        const days = [
          "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
        ]
        return `${days[value.getDay()]} ${value.getMonth()+1}/${value.getDate()}`
      },
      calcDate(startDate: Date, offset: number) {
        const dateVal = new Date(startDate)
        dateVal.setDate(startDate.getDate() + offset)
        return dateVal
      },
      calcIsLastItem(index: number, workout: {activities: Object[]}) {
        return index === workout.activities.length-1
      }
    }
  }
</script>

<style>
  .schedule-day {
    list-style-type: none;
    margin: 0;
    padding: 0.5rem;
  }

  .schedule-title {
    /* border-bottom: 3px solid grey; */
    padding: 0.5rem;
  }

  .schedule-activities-list {
    border: 2px solid #1c1c1c;
    border-radius: 7px;
    background-color: #1c1c1c;
    list-style-type: none;
    margin: 0;
    padding: 0;
    padding-left: 1rem;
  }

  .rest {
    font-style: italic;
  }
</style>
