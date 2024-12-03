export const state = () => ({ 
  workoutSchedule: [
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}],
  selectedDate: -1,
  user_id: '047efff5-cb50-42df-9a57-b9fd91d90602', // TODO: Dynamically grab this
})

export const mutations = {
  setWorkoutSchedule(state, value){
    state.workoutSchedule[value.index].activities = [
      ...state.workoutSchedule[value.index].activities, 
      {"title": value.title, "id": value.id, "exercises": value.exercises}
    ] // TODO: use a spread operator instead of each field
  },
  resetWorkoutScheduleWeek(state) {
    state.workoutSchedule = [
      {"activities": []}, 
      {"activities": []}, 
      {"activities": []}, 
      {"activities": []}, 
      {"activities": []}, 
      {"activities": []}, 
      {"activities": []}]
  },
  setSelectedDate(state, value){
    state.selectedDate = value
  }
}

export const actions = {
  updateSelectedDate({ commit }, item){
    commit('setSelectedDate', item)
  },
  async addWorkout({ commit }, item){
    const body = {
          user_id: this.state.user_id,
          title: item.title,
          workout_date: item.workoutDate
        }
    const res = await this.$axios.post(
      `${this.$config.baseUrl}/workouts`, 
      body,
      {
        headers: {
        'auth-key': this.$config.apiKey,
        'username': 'name'
        },
        
    })
    console.log(res) // TODO: Do more with res
    commit('setSelectedDate', -1)
  },
  async addExercise({ _ }, item) {
    const body = {
      workout_id: item.workoutId,
      title: item.title,
      type: item.type,
      location: item.location,
      note: item.note,
      info: {
        ...(item.weight && {weight: item.weight}),
        ...(item.reps && {reps: item.reps}),
        ...(item.distance && {distance: item.distance}),
      },
    }

    const res = await this.$axios.post(
      `${this.$config.baseUrl}/exercises`, 
      body,
      {
        headers: {
        'auth-key': this.$config.apiKey,
        'username': 'name'
        },
        
    })
    console.log(res) // TODO: Do more with res
  },
  async getWorkouts({ commit }, startDate) {
    const workingDate = new Date(startDate)

    const startDateParam = `${startDate.getMonth()+1}/${startDate.getDate()}/${startDate.getFullYear()}`

    const workoutsRes = await this.$axios.get(
      `${this.$config.baseUrl}/workouts?start_date=${startDateParam}`,
      {
        headers: {
        'auth-key': this.$config.apiKey,
        'username': 'name'
      }
    })

    const workoutIds = workoutsRes.data.map((workout) => workout.id)
    const exercisesRes = await this.$axios.get(
      `${this.$config.baseUrl}/exercises?workout_id__in=${workoutIds.join(',')}`,
      {
        headers: {
        'auth-key': this.$config.apiKey,
        'username': 'name'
      }
    })
    const exercisesMap = {}
    for (const exercise of exercisesRes.data) {
      exercisesMap[exercise.workout_id] = [exercise, ...(exercisesMap[exercise.workout_id] ? exercisesMap[exercise.workout_id] : [])]
    }

    commit('resetWorkoutScheduleWeek')

    const workouts = []
    for (let i = 0; i < 7; i++) {
      workingDate.setDate(workingDate.getDate() + 1)
      workouts.push({"date": workingDate, "activities": []})
    }

    for (const workout of workoutsRes.data) {
      const workoutDate = new Date(workout.workout_date)
      // JS indexes Sunday == 0, we want Monday == 0
      const workoutIndex = workoutDate.getUTCDay() - 1 >= 0 ? workoutDate.getUTCDay() - 1 : 6
      commit('setWorkoutSchedule', {'index': workoutIndex, 'title': workout.title, 'id': workout.id, 'exercises': exercisesMap[workout.id]})
      commit('setSelectedDate', -1)
    }
  }
}
