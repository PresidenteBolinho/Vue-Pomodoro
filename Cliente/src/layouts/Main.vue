<template>
  <ul class="nav justify-content-end">
    <li class="nav-item">
      <v-link href="/" class="nav-link">Home</v-link>
    </li>
    <li class="nav-item">
      <v-link href="/sobre" class="nav-link">Sobre</v-link>
    </li>
    <li class="nav-item">
      <v-link href="/autenticacao" class="nav-link">Login</v-link>
    </li>
  </ul>

  <slot></slot>
</template>

<script>
import VLink from "../components/VLink.vue";

export default {
  components: {
    VLink,
  },
};
</script>

<style>
</style>