<template>
  <ul>
      <li><v-link href="/">Home</v-link></li>
      <li><v-link href="/sobre">Sobre</v-link></li>
      <li><v-link href="/foo">Under Construction</v-link></li>
      <li><v-link href="/autenticacao">Login</v-link></li>
  </ul>

  <slot></slot>
</template>

<script>
import VLink from '../components/VLink.vue'

export default {
    components: {
        VLink
    }
}
</script>