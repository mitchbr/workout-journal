<template>
  <div>
    <ol>
      <li v-for="workoutDay in $store.state.workoutSchedule" :key="workoutDay.date" class="schedule-day">
        <div class="schedule-title">
          {{ workoutDay.date }}
          <v-btn @click="changeAddForm(`${ workoutDay.date }`)">Add</v-btn>
        </div>
          <ul class="schedule-activities__list">
            <li v-if="workoutDay.activities.length === 0 && workoutDay.date !== $store.state.selectedDate">
              <div class="rest">
                <ActivityTile />
              </div>
            </li>
            <li v-for="(activity, index) in workoutDay.activities" :key="index">
              <ActivityTile :activity=activity />
            </li>
            <li v-if="workoutDay.date === $store.state.selectedDate">
              <AddActivity />
            </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script lang="ts">
  export default {
    data () {
      return {}
    },
    methods: {
      changeAddForm(currentDay: string){
        this.$store.commit('setSelectedDate', currentDay)
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
    border-bottom: 3px solid grey;
    display: flex;
  }

  .schedule-activities__list {
    list-style-type: none;
    margin: 0;
    padding: 0;
    padding-left: 1rem;
  }

  .rest {
    font-style: italic;
  }
</style>
