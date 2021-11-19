<template>
  <div id="app" :class="modo">
    <router-view :modo="modo"></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap");

* {
  font-family: "Inter", sans-serif;
  color: #2c3e50;
}
</style>
