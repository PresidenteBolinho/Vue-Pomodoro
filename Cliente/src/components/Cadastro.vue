<template>
  <div class="card">
    <div class="card-body">
      <form>
        <h2>Se registre agora:</h2>
        <div class="form-group">
          <label class="form-label">Primeiro nome</label>
          <input type="text" v-model="primeiro_nome" class="form-control" />
        </div>
        <div class="form-group">
          <label class="form-label">Segundo nome</label>
          <input type="text" v-model="segundo_nome" class="form-control" />
        </div>
        <div class="form-group">
          <label class="form-label">Usuário</label>
          <input type="text" v-model="usuario" class="form-control" />
        </div>
        <div class="form-group">
          <label class="form-label">Email</label>
          <input
            type="email"
            class="form-control"
            v-model="email"
            placeholder="email@email.com"
          />
        </div>
        <div class="form-group">
          <label class="form-label">Senha</label>
          <input type="password" v-model="senha" class="form-control" />
        </div>
        <div class="form-group">
          <label class="form-label">Confirmar senha</label>
          <input
            type="password"
            v-model="confirmar_senha"
            class="form-control"
          />
        </div>
        <br>
        <button class="btn btn-info" @click="handleSubmit">Registrar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      primeiro_nome: "",
      segundo_nome: "",
      usuario: "",
      email: "",
      senha: "",
      confirmar_senha: "",
    };
  },
  methods: {
    async handleSubmit() {
      await axios.post("registro", {
        primeiro_nome: this.primeiro_nome,
        segundo_nome: this.segundo_nome,
        usuario: this.usuario,
        email: this.email,
        senha: this.senha,
        confirmar_senha: this.confirmar_senha,
      });
    },
  },
};
</script>