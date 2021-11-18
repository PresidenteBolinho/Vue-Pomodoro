<template>
  <div>
    <form v-on:submit.prevent="adicionarTarefa()">
      <label for="nova-tarefa">Adicionar tarefa: </label>
      <input
        v-model="novoTextoTarefa"
        id="nova-tarefa"
        placeholder="Ex.: Fazer o almoço"
        style="margin-right: 10px"
      />
      <button>Adicionar</button>
    </form>
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
      tarefas: [{
        id: 1,
        title: 'teste'
      }],
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
