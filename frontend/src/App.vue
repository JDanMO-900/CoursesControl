<template>
  <v-app>
<!--    <TheMenu/>-->
    <v-main>
      <router-view/>
    </v-main>
    <TheFooter/>

  </v-app>


</template>

<script>
// import TheMenu from "@/components/TheMenu.vue";
import TheFooter from "@/components/TheFooter.vue";

export default {
  name: 'App',
  components: {
    TheFooter
    // TheMenu,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

.v-application {
  background-color: #003049;
}
</style>