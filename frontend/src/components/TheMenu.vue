<template>

  <div v-if="stateSideBar == 'inactive'" class="menu-toggle-button" @click="stateSideBar = 'active'">
    <v-icon icon="mdi-menu" size="36"/>
  </div>

  <div class="menu-sidebar" :class="stateSideBar">


    <div class="menu-options mt-3 text-center">


      <v-menu location="end" open-on-hover>
        <template v-slot:activator="{ props }">
          <div class="d-flex flex-column align-center pt-2 pb-2 p-1" v-bind="props">
            <v-icon icon="mdi-file" size="20"></v-icon>
            <span>Reportes</span>
          </div>
        </template>

        <v-list density="compact" variant="plain" class="my-list pt-2 pb-2">
          <RouterLink to="#">
            <v-list-item>
              Equipos en bodega
            </v-list-item>
          </RouterLink>
          <RouterLink to="#">
            <v-list-item>
              Listado de equipos
            </v-list-item>
          </RouterLink>

        </v-list>
      </v-menu>


    </div>
  </div>
</template>

<script setup>

import {RouterLink} from "vue-router";
import useMenu from "@/composables/useMenu";

const {stateSideBar} = useMenu();

</script>

<style lang="scss">
@import "@/assets/styles/variables.scss";

.menu-sidebar {

  width: 8rem;
  height: 100vh;
  position: fixed;
  top: 0;
  z-index: 999;
  background: $menu-color;
  font-size: 16px;
}

.menu-sidebar a, .menu-sidebar div {
  color: white;
}

.menu-options {
  text-decoration: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.menu-options a:hover, .menu-options div:hover {
  color: #E0E5F1;
  background-color: #474F7A;
  //border-radius: 10px;
}

.my-list {
  justify-content: center;
  align-items: center;
  text-decoration: none;
  background-color: #3C486B !important;
}

.my-list a {

  color: #F0F0F0 !important;
}

.my-list .v-list-item:hover {
  color: white !important;
  background-color: #82B1FF;
}

.inactive {
  left: -8rem;
  animation: linear;
  animation-name: hideMenu;
  animation-duration: 0.4s;
}

@keyframes hideMenu {
  0% {
    left: 0;
    transform: translateX(0);
  }

  100% {
    left: -6rem;
    transform: translateX(-6rem);
  }
}

.active {
  left: 0;
  animation: linear;
  animation-name: showMenu;
  animation-duration: 0.4s;
}

@keyframes showMenu {
  0% {
    left: -6rem;
    transform: translateX(-6rem);
  }

  100% {
    left: 0;
    transform: translateX(0);
  }
}
</style>