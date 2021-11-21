<template>
  <div>
    <h1 :class="vuexModo">{{ vuexMsg }}</h1>
    <button class="btn btn-primary" @click="mudarTema()">{{ msg }}</button>
  </div>
</template>

<script>

export default {
  name: "Ping",
  data() {
    return {
      msg: "Mudar tema",
    };
  },
  methods: {
    mudarTema() {
      if (this.vuexModo == "claro") {
        this.$store.commit('mudancaModo', 'escuro')
        this.$store.commit('novaMsg', 'Tema escuro ativado')
      } else if (this.vuexModo == "escuro") {
        this.$store.commit('mudancaModo', 'claro')
        this.$store.commit('novaMsg', 'Tema claro ativado')
      }
    }
  },
  computed: {
    vuexMsg() {
      return this.$store.getters.getMsg
    },
    vuexModo() {
        return this.$store.getters.getModo
    }
  },
};
</script>


<style>
</style>