<template>
  <div
    class="container rounded justify-content-center"
    :class="[{ 'bg-secondary': eTemaEscuro, 'text-white': eTemaEscuro }]"
  >
    <form
      v-on:submit.prevent="adicionarTarefa()"
      class="justify-content-center"
    >
      <label for="nova-tarefa" class="col-md-3">Adicionar tarefa: </label>
      <input
        v-model="novoTextoTarefa"
        id="nova-tarefa"
        placeholder="Ex.: Fazer o almoço"
        class="col-md-6 rounded"
        style="margin-right: 10px"
      />
      <button
        class="btn col-md-2"
        :class="eTemaEscuro ? 'btn-outline-light' : 'btn-primary'"
      >
        Adicionar
      </button>
    </form>
    <hr />
    <item-tarefas
      v-for="(tarefa, index) in tarefas"
      :key="tarefa.id"
      :title="tarefa.title"
      @remove="tarefas.splice(index, 1)"
    />
  </div>
</template>

<script>
import ItemTarefas from "./Item-Tarefas.vue";

export default {
  name: "lista-tarefas",
  components: { ItemTarefas },

  data() {
    return {
      tarefas: [],
      novoTextoTarefa: "",
      IdTarefa: 1,
    };
  },
  methods: {
    adicionarTarefa() {
      if (this.novoTextoTarefa != "") {
        this.tarefas.push({
          id: this.IdTarefa++,
          title: this.novoTextoTarefa,
        });
        this.novoTextoTarefa = "";
      } else alert("O campo não pode estar vazio.");
    },
  },
};
</script>

<style>
</style>