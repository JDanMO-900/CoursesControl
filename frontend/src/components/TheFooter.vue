<template>
  <v-footer class="d-flex flex-column my-low-footer"  rounded="lg">
<!--    <div class="d-flex w-100 align-center px-4 py-2">-->
<!--      <strong>Get connected with us on social networks!</strong>-->


<!--    </div>-->

    <div class="px-4 py-3 bg-cyan-darken-2 text-center w-100 rounded-lg">
      {{ new Date().getFullYear() }} — <strong>Site made by Daniel</strong>
    </div>
  </v-footer>
</template>

<script setup>

</script>

<style scoped>
.my-low-footer {
  background-color: #003049;
  color: #ffffff;
}
</style>
