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
    // TODO: Setting state of two vars probably isn't best practice
    state.workoutSchedule[value.index].activities = [...state.workoutSchedule[value.index].activities, {"title": value.title}]
    state.selectedDate = -1
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
