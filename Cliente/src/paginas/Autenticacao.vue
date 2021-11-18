<template>
  <main-layout>
    <div class="container">
      <div class="row">
      <div class="col">
        <div>
          <login></login>
        </div>
      </div>
      <div class="col">
        <div>
          <cadastro></cadastro>
        </div>
      </div>
    </div>
    </div>
  </main-layout>
</template>

<script>
import MainLayout from "../layouts/Main.vue";
import Login from "../components/Login.vue";
import Cadastro from "../components/Cadastro.vue";

export default {
  components: {
    MainLayout,
    Login,
    Cadastro,
  },
};
</script>
