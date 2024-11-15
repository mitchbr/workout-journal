<template>
  <div class="container">
    <div class="title">
      <h1>{{ dateToDisplay(startDate) }} to {{ dateToDisplay(calcDate(startDate, 6)) }}</h1>
    </div>

    <WorkoutsList :startDate=startDate />

    <div class="bottom-controls">
      <div class="nav-button">
        <v-btn :to="{ path: '', query: { start_date: calcPrevDate() } }">
          Previous
        </v-btn>
      </div>
      <div class="nav-button">
        <v-btn :to="{ path: '' }">
          Today
        </v-btn>
      </div>
      <div class="nav-button">
        <v-btn :to="{ path: '', query: { start_date: calcNextDate() } }">
          Next
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  export default Vue.extend({
    name: 'IndexPage',
    methods: {
      dateToDisplay(value: Date) {
        return `${value.getMonth()+1}/${value.getDate()}/${value.getFullYear()}`
      },
      calcDate(startDate: Date, offset: number) {
        let resDate = new Date(startDate)
        resDate.setDate(startDate.getDate() + offset)
        return resDate
      },
      calcNextDate() {
        const nextDate = this.calcDate(this.startDate, 7)
        const nextStr = `${nextDate.getMonth()+1}-${nextDate.getDate()}-${nextDate.getFullYear()}`
        return nextStr
      },
      calcPrevDate() {
        const prevDate = this.calcDate(this.startDate, -7)
        return `${prevDate.getMonth()+1}-${prevDate.getDate()}-${prevDate.getFullYear()}`
      }
    },
    computed: {
      startDate() {
        // TODO: Validate date format
        const queryStartDate = this.$route.query.start_date
        let startDate;
        if (typeof queryStartDate === 'string') {
          startDate = new Date(queryStartDate)
        } else {
          let currDate = new Date()
          startDate = new Date()
          let daysDiff = currDate.getDay() - 1
          // Finds most recent Monday
          startDate.setDate(currDate.getDate() - (daysDiff > 0 ? daysDiff : (daysDiff * -6)))
        }
        return startDate
      }
    }
  })
</script>

<style>
  .bottom-controls {
    margin: auto;
    display: flex;
    justify-content: center;
    padding: 0.5rem;
  }

  .title {
    padding: 0.5rem;
    display: flex;
    justify-content: center;
  }

  .nav-button {
    padding: 0.5rem;
  }
</style>