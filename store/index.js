export const state = () => ({ 
  workoutSchedule: [
    {"date": "Monday", "activities": []}, 
    {"date": "Tuesday", "activities": []}, 
    {"date": "Wednesday", "activities": []}, 
    {"date": "Thursday", "activities": []}, 
    {"date": "Friday", "activities": []}, 
    {"date": "Saturday", "activities": []}, 
    {"date": "Sunday", "activities": []}],
  selectedDate: "",
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
