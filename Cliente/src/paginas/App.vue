<template>
  <main-layout>
      <Pomodoro class="container" />
  </main-layout>
</template>

<script>
import MainLayout from '../layouts/Main.vue'
import Pomodoro from '../components/Pomodoro.vue'

export default {
    components: {
        MainLayout,
        Pomodoro
    }
}
</script>

<style>

</style>