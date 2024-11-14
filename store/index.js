export const state = () => ({ 
  workoutSchedule: [
    {"activities": [{"title": "Lift"}]}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}, 
    {"activities": []}],
  selectedDate: -1,
})

export const mutations = {
  setWorkoutSchedule(state, value){
    const index = state.workoutSchedule.findIndex((element) => element.date === value.date)
    state.workoutSchedule[index].activities.push({"title": value.title})
  },
  setSelectedDate(state, value){
    state.selectedDate = value
  }
}

export const actions = {
  addWorkout({ commit }, item){
    commit('setWorkoutSchedule', item)
  },
  updateSelectedDate({ commit }, item){
    commit('setSelectedDate', item)
  }
}
