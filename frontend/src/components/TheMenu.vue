<template>

  <v-app-bar class="bg-cyan-darken-2">
    <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title>My files</v-toolbar-title>


  </v-app-bar>

  <v-navigation-drawer
      v-model="drawer"
      :location="$vuetify.display.mobile ? 'left' : undefined"
      temporary
  >
    <div class="menu-options mt-3 text-center">
      <RouterLink to="/area-list" class="d-flex flex-column align-center pt-2 pb-2 p-1">
        <v-icon icon="mdi-account-check" size="20"></v-icon>
        <span>Lista de áreas</span>
      </RouterLink>
    </div>

    <div class="menu-options mt-3 text-center">
      <RouterLink to="/group-list" class="d-flex flex-column align-center pt-2 pb-2 p-1">
        <v-icon icon="mdi-account-check" size="20"></v-icon>
        <span>Lista de grupos</span>
      </RouterLink>
    </div>

    <div class="menu-options mt-3 text-center">
      <RouterLink to="/course-list" class="d-flex flex-column align-center pt-2 pb-2 p-1">
        <v-icon icon="mdi-account-check" size="20"></v-icon>
        <span>Lista de Cursos</span>
      </RouterLink>
    </div>


  </v-navigation-drawer>


</template>

<script setup>
import {ref, watch} from 'vue'


const drawer = ref(false)
const group = ref(null)

watch(group, () => {
  drawer.value = false
})
</script>

<style scoped>

.menu-options a:hover, .menu-options div:hover {
  color: #E0E5F1;
  background-color: #474F7A;

}

.menu-options a {
  text-decoration: none;
  color: #003049;
}


</style>