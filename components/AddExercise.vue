<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template #activator="{ on, attrs }">
        <v-icon 
          v-bind="attrs"
          v-on="on"
        >
          mdi-plus-circle-outline
        </v-icon>
    </template>

      <v-card>
        <v-card-title class="text-h5">
          New {{ workout.title }} Info
        </v-card-title>
        
        <v-col cols="auto">

          <v-text-field v-model="inputTitle" label="Title" ></v-text-field>

          <v-select
            v-model="selectedExerciseType"
            label="Exercise Type"
            :items="exerciseType"
          ></v-select>

          <div v-if="selectedExerciseType === 'Weight & Reps'" >
            <v-col cols="auto">
              <v-row align="center" justify="space-around">
                <v-col cols="auto">
                  <v-row align="center" justify="start">
                      <v-responsive
                      max-width="150"
                    >
                      <v-text-field v-model="inputWeight" label="Weight"></v-text-field>
                    </v-responsive>
                    <p>lb</p>
                  </v-row>
                </v-col>
                <v-col cols="auto">
                  <v-row align="center" justify="start">
                    <v-responsive
                      max-width="150"
                    >
                      <v-text-field v-model="inputReps" label="Reps"></v-text-field>
                    </v-responsive>
                    <p>reps</p>
                  </v-row>
                </v-col>
              </v-row>
            </v-col>
          </div>
          <div v-if="selectedExerciseType === 'Distance'" >
            <v-col cols="auto">
              <v-row align="center" justify="space-around">
                <v-responsive
                  max-width="150"
                >
                  <v-text-field v-model="inputDistance" label="Distance"></v-text-field>
                </v-responsive>
                <p>Miles</p>
              </v-row>
            </v-col>
          </div>

          <v-divider></v-divider>

          <v-text-field v-model="inputLocation" label="Location" ></v-text-field>
          <v-text-field v-model="inputNote" label="Note"></v-text-field>

          <v-divider></v-divider>
        </v-col>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="secondary"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="primary"
            text
            @click="submitExercise"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
  export default {
    props: {
      workout: {
        type: Object,
        required: true
      },
    },
    data () {
      return {
        dialog: false,
        selectedExerciseType: "",
        exerciseType: [
          'Weight & Reps',
          'Distance',
          'Other',
        ],
        inputTitle: "",
        inputWeight: "",
        inputReps: "",
        inputDistance: "",
        inputLocation: "",
        inputNote: "",
      }
    },
    methods: {
      resetToDefaults() {
        const thisObj = this as any // TODO: WHY??
        thisObj.dialog = false
        thisObj.inputTitle = ""
        thisObj.inputWeight = ""
        thisObj.inputReps = ""
        thisObj.inputDistance = ""
        thisObj.inputLocation = ""
        thisObj.inputNote = ""
      },
      submitExercise() {
        const thisObj = this as any // TODO: Why???
        const exerciseData = {
          workoutId: thisObj.$props.workout.id,
          title: thisObj.inputTitle,
          type: thisObj.selectedExerciseType,
          weight: thisObj.inputWeight,
          reps: thisObj.inputReps,
          distance: thisObj.inputDistance,
          location: thisObj.inputLocation,
          note: thisObj.inputNote
        }

        thisObj.$store.dispatch('addExercise', exerciseData)
        // TODO: startDate add to store
          // .then(() => {
          //   (this as any).$store.dispatch('getWorkouts', (this as any).startDate)
          // })
        this.resetToDefaults()
        
      }
    }
  }
</script>

<style>

</style>