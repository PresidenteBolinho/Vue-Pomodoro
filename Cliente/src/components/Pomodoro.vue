<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <div
          class="btn-toolbar justify-content-center"
          role="toolbar"
          aria-label="Toolbar with button groups"
        >
          <button
            type="button"
            class="btn btn-primary"
            @click="tempoDePomodoro()"
          >
            Pomodoro
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click="tempoDePausaCurta()"
          >
            Pausa curta
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click="tempoDePausaLonga()"
          >
            Pausa longa
          </button>
        </div>
      </div>
      <div class="card-body">
        <div class="justify-content-center">
          <label id="relogio" class="row justify-content-center">{{
            relogio
          }}</label>
        </div>
      </div>
      <div class="card-footer">
        <div class="row justify-content-center">
          <button type="button" class="btn btn-success" @click="cronometrar()">
            {{ textoBotao }}
          </button>
        </div>
      </div>
    </div>
    <br />
    <lista-tarefas />
  </div>
</template>

<script>
import ListaTarefas from "./Lista-tarefas.vue";
import Alarme from "../assets/sounds/alarm.mp3";

export default {
  components: { ListaTarefas },
  name: "Pomodoro",

  data() {
    const pomodoroTempo = 25 * 60;
    const pausaCurta = 5 * 60;
    const pausaLonga = 15 * 60;
    const somAlarme = new Audio(Alarme);

    return {
      pomodoroTempo,
      pausaCurta,
      pausaLonga,
      tempoAtual: pomodoroTempo,
      textoBotao: "Começar!",
      intervalo: null,
      contagemPomodoros: 0,
      alarme: somAlarme,
    };
  },
  methods: {
    tempoDePomodoro() {
      clearInterval(this.intervalo);
      this.tempoAtual = this.pomodoroTempo;
      this.textoBotao = "Começar!";
    },
    tempoDePausaCurta() {
      clearInterval(this.intervalo);
      this.tempoAtual = this.pausaCurta;
      this.textoBotao = "Começar!";
    },
    tempoDePausaLonga() {
      clearInterval(this.intervalo);
      this.tempoAtual = this.pausaLonga;
      this.textoBotao = "Começar!";
    },
    cronometrar() {
      if (this.textoBotao === "Começar!" || this.textoBotao === "Recomeçar") {
        this.reducaoDoTempo();
        this.textoBotao = "Pausa";
      } else if (this.textoBotao === "Pausa") {
        this.paradaDoTempo();
        this.textoBotao = "Recomeçar";
      }
    },
    reducaoDoTempo() {
      this.intervalo = setInterval(() => {
        if (this.tempoAtual > 0) {
          this.tempoAtual -= 1;
        }
      }, 1000);
    },
    paradaDoTempo() {
      clearInterval(this.intervalo);
    },
    concluido() {
      if (this.tempoAtual <= 0) {
        // Clear interval
        clearInterval(this.intervalo);

        if (this.contagemPomodoros >= 4) {
          this.tempoAtual = this.pausaLonga;
          this.contagemPomodoros = 0;
        } else {
          this.tempoAtual = this.pausaCurta;
          this.contagemPomodoros++;
        }

        this.alarme.play();

        // Immediately disable button and set state
        this.textoBotao = "Começar!";
      }
    },
  },
  computed: {
    relogio() {
      const minutos = String(parseInt(this.tempoAtual / 60));
      const segundos = String(parseInt(this.tempoAtual % 60));
      const minutosRestantes = ("0" + minutos).slice(-2);
      const segundosRestantes = ("0" + segundos).slice(-2);

      if (minutosRestantes <= 0 && segundosRestantes <= 0) this.concluido();

      return `${minutosRestantes}:${segundosRestantes}`;
    },
  },
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap");

label {
  font-family: "Inter", sans-serif;
  color: #2c3e50;
}

#relogio {
  font-size: 88px;
}

li {
  list-style-type: none;
}

button {
  font-size: 18px;
  margin: 1px;
}
</style>
