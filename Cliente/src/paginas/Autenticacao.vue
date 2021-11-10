<template>
  <main-layout>
    <div id="Login">
      <form>
        <h2>Acesse sua conta:</h2>
        <div class="form-group">
          <label class="form-label">Email</label>
          <input
            type="email"
            id="emailAcesso"
            class="form-control"
            placeholder="email@email.com"
          />
        </div>
        <div class="form-group">
          <label class="form-label">Senha</label>
          <input type="password" id="senhaAcesso" class="form-control" />
        </div>
        <input type="submit" id="btn-form-acesso" class="btn btn-primary" />
      </form>
    </div>
    <hr>
    <div id="Cadastro">
      <form>
        <h2>Se registre agora:</h2>
        <div class="form-group">
          <label class="form-label">Email</label>
          <input
            type="email"
            id="emailRegistro"
            class="form-control"
            placeholder="email@email.com"
          />
        </div>
        <div class="form-group">
          <label class="form-label">Senha</label>
          <input type="password" id="senhaRegistro" class="form-control" />
        </div>
        <input type="submit" id="btn-form-registro" class="btn btn-info" />
      </form>
    </div>
  </main-layout>
</template>

<script>
import MainLayout from "../layouts/Main.vue";

export default {
  components: {
    MainLayout,
  },
};
</script>

<style>
</style>