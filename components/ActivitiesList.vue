<template>
  <div>
    <ol>
      <li v-for="dateOffset in 7" :key="dateOffset" class="schedule-day">
        <div class="schedule-title">
          <v-row align="center" justify="space-between">
            <v-col cols="auto">
              <div class="text-h5">
                {{ dateToDisplay(calcDate(props.startDate, dateOffset-1)) }}
              </div>
            </v-col>
            <v-col cols="auto">
              <v-btn density="compact" size="x-small" @click="changeAddForm(dateOffset)">Add</v-btn>
            </v-col>
          </v-row>
        </div>
          <ul class="schedule-activities-list">
            <li v-if="$store.state.workoutSchedule[dateOffset-1].activities.length === 0 && dateOffset !== $store.state.selectedDate">
              <div class="rest">
                <ActivityTile />
              </div>
            </li>
            <li v-for="(activity, index) in $store.state.workoutSchedule[dateOffset-1].activities" :key="index">
              <ActivityTile :activity=activity />
            </li>
            <li v-if="dateOffset === $store.state.selectedDate">
              <AddActivity />
            </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script lang="ts" setup>
  const props = defineProps({
    startDate: { type: Date },
  })
</script>


<script lang="ts">
  export default {
    data () {
      return {}
    },
    methods: {
      changeAddForm(currentDay: number){
        (this as any).$store.commit('setSelectedDate', currentDay)
      },
      dateToDisplay(value: Date) {
        const days = [
          "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
        ]
        return `${days[value.getDay()]} ${value.getMonth()+1}/${value.getDate()}`
      },
      calcDate(startDate: Date, offset: number) {
        let dateVal = new Date(startDate)
        dateVal.setDate(startDate.getDate() + offset)
        return dateVal
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
    padding: 0.5rem;
  }

  .schedule-activities-list {
    list-style-type: none;
    margin: 0;
    padding: 0;
    padding-left: 1rem;
  }

  .rest {
    font-style: italic;
  }
</style>
