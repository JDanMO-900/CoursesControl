<template>

  <v-container class="my-container">

    <div class="pa-3 ma-2">
      <!--  Dialog-->
      <v-btn variant="outlined" class="bg-cyan-darken-2 text-white" @click="openAddDialog"
             prepend-icon="mdi-plus-circle"

      >
        Agregar área
      </v-btn>


    </div>

    <div class=" pa-6 mb-4">
      <v-card
          title="Area"
          class="table-title"
          flat
      >

        <template v-slot:text>
          <v-text-field
              v-model="search"
              label="Buscar"
              prepend-inner-icon="mdi-magnify"
              variant="outlined"
              hide-details
              single-line
          ></v-text-field>
        </template>

        <v-data-table
            :headers="headers"
            :items="areas"
            :search="search"
            class="my-table"
            sort-desc

        >
          <template v-slot:[`item.actions`]="{ item }">

            <v-icon size="20" class="mr-2 text-red-accent-4" @click="openDeleteDialog(item)"
                    icon="mdi-delete-alert"></v-icon>
            <v-icon size="20" class="mr-2 text-light-blue-darken-4" @click="openEditDialog(item)"
                    icon="mdi-circle-edit-outline"></v-icon>


          </template>

        </v-data-table>
      </v-card>
    </div>

  </v-container>

  <!--  dialog-add-->
  <v-dialog
      v-model="addDialog"
      max-width="600"
      transition="dialog-bottom-transition"
  >

    <v-card
    >

      <v-card-title class="text-h6 text-white bg-cyan-darken-4 text-center">


        <span>Agregar nueva área</span>
      </v-card-title>
      <v-card-text>
        <v-row dense>
          <v-col
              cols="12"
              md="12"
              sm="12"
          >
            <v-text-field
                clearable
                label="Coloque el área"
                variant="solo-filled"
                :counter="50"
                required
                class="bg-white"
                v-model="edit_area.name"
                :errors="v$.edit_area.name.$errors.map(e => e.$message)"
            ></v-text-field>

          </v-col>

        </v-row>

      </v-card-text>

      <v-divider></v-divider>
      <v-divider
          :thickness="4"
          class="border-opacity-20"

      ></v-divider>

      <v-card-actions class="text-h6 text-white ">
        <v-spacer></v-spacer>

        <v-btn
            text="Cerrar"
            class="bg-red-accent-3"
            append-icon="mdi-close-circle-outline"
            variant="plain"
            @click="addDialog = false"
        ></v-btn>

        <v-btn
            class="bg-green-accent-3 text-white"
            text="Guardar"
            variant="plain"
            append-icon="mdi-file-plus-outline"
            @click="createArea()"
            :loading="isLoading"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <!--  dialog-add-->

  <!--  delete-dialog-->
  <template>
    <div class="text-center pa-4">
      <v-dialog
          v-model="deleteDialog"
          max-width="450"

          persistent
      >
        <template v-slot:activator="{ props: activatorProps }">
          <v-btn v-bind="activatorProps">
            Open Dialog
          </v-btn>
        </template>

        <v-card

        >
          <v-card-title class="bg-cyan-darken-4">
            <v-icon class="text-amber-darken-3">
              mdi-alert
            </v-icon>
            ¿Está seguro de eliminar el área?


          </v-card-title>
          <v-card-text class="text-center">
            Esta acción eliminará el área <strong class="text-red"><u>{{ to_delete.name }}</u></strong>.
            <br/>
            <strong>El registro ya no será visible en la lista.</strong>
          </v-card-text>
          <v-divider
              :thickness="4"
              class="border-opacity-20"

          ></v-divider>


          <template v-slot:actions>
            <v-spacer></v-spacer>


            <v-btn @click="deleteDialog = false"
                   class="bg-light-blue-lighten-2"
                   variant="plain"
                   append-icon="mdi-close-circle-outline"
            >
              Cerrar
            </v-btn>

            <v-btn
                @click="deleteArea(this.to_delete)"
                class="bg-red-accent-3 text-white"
                append-icon="mdi-delete-empty-outline"
                variant="plain"
                :loading="isLoading"
            >
              Eliminar
            </v-btn>
          </template>
        </v-card>
      </v-dialog>
    </div>
  </template>

  <!--  delete-dialog-->

  <!--  edit dialog-->
  <v-dialog
      v-model="editDialog"
      max-width="600"
      transition="dialog-top-transition"
  >

    <v-card
    >

      <v-card-title class="text-h6 text-white bg-cyan-darken-4 text-center">

        <v-icon size="20" class="mr-1">mdi-file-edit-outline</v-icon>
        <span>Editar área</span>

      </v-card-title>
      <v-card-text>
        <v-row dense>
          <v-col
              cols="12"
              md="12"
              sm="12"
          >
            <v-text-field clearable label="Coloque el área" variant="solo-filled" :counter="50"
                          required class="bg-white" v-model="edit_area.name"></v-text-field>

          </v-col>

        </v-row>

      </v-card-text>

      <v-divider></v-divider>
      <v-divider
          :thickness="4"
          class="border-opacity-20"

      ></v-divider>

      <v-card-actions class="text-h6 text-white ">
        <v-spacer></v-spacer>

        <v-btn
            text="Cerrar"
            class="bg-red-accent-3"
            variant="plain"
            append-icon="mdi-close-circle-outline"
            @click="editDialog = false"
        ></v-btn>

        <v-btn
            class="bg-green-accent-3 text-white"
            text="Editar"
            variant="plain"
            append-icon="mdi-pencil-plus-outline"
            :loading="isLoading"
            @click="updateArea(this.to_edit)"

        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <!--  edit dialog-->

  <!--  alert dialog-->
  <v-dialog
      v-model="alertDialog"
      max-width="600"
  >
    <v-alert
        density="compact"
        type="warning"
    >
      <v-title>
        Alerta:
      </v-title>

      <v-text>
        {{ this.error_message }}

      </v-text>

    </v-alert>


    <v-btn
        text="Cerrar"
        class="bg-red-accent-3"
        variant="plain"
        append-icon="mdi-close-circle-outline"
        @click="alertDialog = false"
    ></v-btn>


  </v-dialog>

  <!--  alert dialog-->


</template>

<script>
import apiClient from "@/services/api";
import useVuelidate from "@vuelidate/core";
import {required, maxLength, helpers} from "@vuelidate/validators";

export default {
  name: "AreaList",

  data() {
    return {
      areas: [],
      v$: null,
      error_message: "",

      editedIndex: -1,
      edit_area: {
        name: ""
      },
      default_item: {
        name: ""
      }
      ,

      addDialog: false,
      deleteDialog: false,
      editDialog: false,
      alertDialog: false,

      isLoading: false,

      to_delete: null,
      to_edit: "",
      valid: false,

      search: '',
      headers: [
        {
          title: 'Nombre del área',
          align: 'start',
          sortable: true,
          value: 'name',

        },

        {title: "Actions", value: "actions", sortable: true,}

      ],

    }
  },
  validations() {
    return {
      edit_area: {
        name: {
          required: helpers.withMessage("El campo nombre es obligatorio", required),
          maxLength: helpers.withMessage("Máximo 50 caracteres", maxLength(50)),
        }
      }
    }
  }

  ,

  methods: {

    async fetchAreas() {
      try {
        const response = await apiClient.get("/api/area/");
        this.areas = response.data;
      } catch (error) {
        console.error("Error fetching areas:", error);
      }
    },
    async createArea() {
      this.v$.$touch();

      if (this.v$.$invalid) {
        this.error_message = (this.v$.edit_area.name.$errors[0].$message);
        this.alertDialog = true;
        return;
      }

      try {
        this.isLoading = true;

        const response = await apiClient.post("/api/area/", this.edit_area);
        this.areas.push(response.data);
      } catch (error) {
        if (error.response && error.response.data) {
          const errors = error.response.data;
          if (errors.name) {
            this.error_message = errors.name[0];
            this.alertDialog = true;

          }
        } else {
          console.error("unexpected error", error)
        }

      } finally {
        await this.fetchAreas();
        this.edit_area.name = "";
        await new Promise(resolve => setTimeout(resolve, 500));
        this.isLoading = false;
        this.addDialog = false;
      }

    },


    async updateArea(area) {

      if (this.editedIndex > -1) {
        const edited = Object.assign(
            this.areas[this.editedIndex],
            this.edit_area
        );
        try {
          const response = await apiClient.put(`/api/area/${edited.id}/`, edited);
          const index = this.areas.findIndex(a => a.id === area.id);
          this.isLoading = true;
          if (index !== -1) {
            this.areas[index] = response.data;
          }


        } catch (error) {

          if (error.response && error.response.data) {
            const errors = error.response.data;
            if (errors.name) {
              this.error_message = errors.name[0];
              this.alertDialog = true;

            }
          } else {
            this.error_message = ("unexpected error: " + error)
          }

        } finally {
          await this.fetchAreas();
          await new Promise(resolve => setTimeout(resolve, 500));
          this.isLoading = false;
          this.editDialog = false;

        }
      }


    },

    async deleteArea(area) {
      try {
        await apiClient.delete(`/api/area/${area.id}/`);
        this.areas = this.areas.filter(areaToDelete => areaToDelete.id !== area.id);
        this.isLoading = true;

      } catch (error) {
        if (error.response && error.response.data) {
          const errors = error.response.data;
          if (errors.name) {
            this.error_message = errors.name[0];
            this.alertDialog = true;

          }
        } else {
          this.error_message = ("unexpected error: " + error)
        }
      } finally {
        await this.fetchAreas()
        await new Promise(resolve => setTimeout(resolve, 500));
        this.isLoading = false;

        this.deleteDialog = false;
      }
    },

    openAddDialog() {
      this.edit_area = Object.assign({}, this.default_item);
      this.addDialog = true;
    },
    openDeleteDialog(to_delete) {
      this.to_delete = to_delete;
      this.deleteDialog = true;
    },
    openEditDialog(item) {
      // editedIndex guarda el id del arreglo creado localmente
      this.editedIndex = this.areas.indexOf(item);
      // En este caso el id del arreglo local es el mismo que el id de la base de datos
      this.edit_area = Object.assign({}, item);
      this.editDialog = true;
    },


  },
  created() {
    this.v$ = useVuelidate();
  },
  mounted() {
    this.fetchAreas();
  },


}

</script>

<style scoped>
.red-text {
  color: red;
}

.green-text {
  color: green;
}

.my-table {
  border: 0.125rem solid white;
  border-radius: 0.5rem;
  overflow: hidden;
}

::v-deep(.my-table thead) {
  background-color: #0097a7;
  color: white;
}

::v-deep(.my-table th:hover .v-data-table-header__content) {
  font-weight: 700 !important;
  color: white !important;

}


.table-title {
  border: 2px dashed #ffffff !important;;
  background-color: #003049;
  color: white;


}

.my-container {
  background-color: #003049;
  color: white;
}


</style>