<template>
  <div>
    <h1 :class="vuexModo">{{ vuexMsg }}</h1>
    <button class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Ping",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      const path = "http://127.0.0.1:5000/ping";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  computed: {
    vuexMsg() {
      return this.$store.getters.getMsg
    },
    vuexModo() {
        return this.$store.getters.getModo
    }
  },
//   created() {
//     this.getMessage();
//   },
};
</script>


<style>
</style>