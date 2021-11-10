<template>
  <div id="App">
    <router-view></router-view>
  </div>
  <!-- <div class="form-check form-switch">
    <label>{{ textoTemaEscuro }}</label>
    <input
      class="form-check-input"
      type="checkbox"
      role="switch"
      id="flexSwitchCheckDefault"
      v-model="eTemaEscuro"
      @click="mudarTema()"
    />
    <Pomodoro class="container" />
  </div> -->
</template>

<script>
// import Pomodoro from "./components/Pomodoro.vue";

export default {
  name: "App",
  data() {
    return {
      eTemaEscuro: false,
      textoTemaEscuro: "Tema claro",
    };
  },
  methods: {
    mudarTema() {
      if (this.eTemaEscuro) {
        this.textoTemaEscuro = "Tema claro";
      } else {
        this.textoTemaEscuro = "Tema escuro";
      }
    },
  },
  components: {
    // Pomodoro,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

@import url("https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap");

#tema-escuro {
  background-color: black;
}

#app {
  height: 100vh;
}

label {
  font-family: "Inter", sans-serif;
}

#relogio {
  font-size: 88px;
}

li {
  list-style-type: none;
}

button {
  margin: 1px;
}
</style>
