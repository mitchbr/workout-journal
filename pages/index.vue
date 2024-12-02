<template>
  <div class="container">
    <div class="title">
      <h1>{{ dateToDisplay(startDate) }} to {{ dateToDisplay(calcDate(startDate, 6)) }}</h1>
    </div>

    <WorkoutsList :start-date=startDate />

    <div class="bottom-controls">
      <div class="nav-button">
        <v-btn :to="{ path: '', query: { start_date: calcPrevDate() } }">
          <v-icon>
            mdi-menu-left
          </v-icon>
        </v-btn>
      </div>
      <div class="nav-button">
        <v-btn :to="{ path: '' }">
          Today
        </v-btn>
      </div>
      <div class="nav-button">
        <v-btn :to="{ path: '', query: { start_date: calcNextDate() } }">
          <v-icon>
            mdi-menu-right
          </v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  export default Vue.extend({
    name: 'IndexPage',
    computed: {
      startDate() {
        // TODO: Validate date format
        const queryStartDate = this.$route.query.start_date
        let startDate;
        if (typeof queryStartDate === 'string') {
          startDate = new Date(queryStartDate)
        } else {
          const currDate = new Date()
          startDate = new Date()
          const daysDiff = currDate.getDay() - 1
          // Finds most recent Monday
          startDate.setDate(currDate.getDate() - (daysDiff > 0 ? daysDiff : (daysDiff * -6)))
        }
        return startDate
      }
    },
    watch: {
      '$route' () {
        this.fetchWorkoutData()
      }
    },
    mounted() {
      this.fetchWorkoutData()
    },

    methods: {
      dateToDisplay(value: Date) {
        const year = value.toLocaleDateString('en', {year: '2-digit'})
        return `${value.getMonth()+1}/${value.getDate()}/${year}`
      },
      calcDate(startDate: Date, offset: number) {
        const resDate = new Date(startDate)
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
      },
      fetchWorkoutData() {
        (this as any).$store.dispatch('getWorkouts', (this as any).startDate);
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