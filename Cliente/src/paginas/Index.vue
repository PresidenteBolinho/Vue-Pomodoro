<template>
  <main-layout>
      <Pomodoro />
  </main-layout>
</template>

<script>
import MainLayout from '../layouts/Main.vue'
import Pomodoro from '../components/Pomodoro.vue'
import axios from 'axios'

export default {
    name: 'Sobre',
    components: {
        MainLayout,
        Pomodoro
    },
    async created() {
        const response = await axios.get('usuario')

        console.log(response)
    }
}
</script>
