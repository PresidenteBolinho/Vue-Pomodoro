<template>
  <div class="card">
    <div class="card-body">
      <form>
        <h2>Acesse sua conta:</h2>
        <div class="form-group">
          <label class="form-label">Usuário</label>
          <input
            type="user"
            class="form-control"
            v-model="usuario"
            placeholder="Usuário"
          />
        </div>
        <div class="form-group">
          <label class="form-label">Senha</label>
          <input type="password" v-model="senha" class="form-control" />
        </div>
        <br />
        <button
          type="submit"
          @click.prevent="handleSubmit()"
          class="btn btn-primary"
        >
          Acessar
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      usuario: "",
      senha: "",
    };
  },
  methods: {
    async handleSubmit() {
      await axios.post("login", {
        usuario: this.usuario,
        senha: this.senha,
      });
    },
  },
};
</script>
