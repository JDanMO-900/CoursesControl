<template>

  <v-container class="my-container">

    <div class="pa-3 ma-2">
      <!--  Dialog-->
      <v-btn variant="outlined" class="bg-cyan-darken-2 text-white" @click="openAddDialog"
             prepend-icon="mdi-plus-circle"

      >
        Agregar curso
      </v-btn>


    </div>

    <div class=" pa-6 mb-4">
      <v-card
          title="Cursos"
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
            :items="courses"
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


        <span>Agregar nuevo curso</span>
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
                label="Coloque el curso"
                variant="solo-filled"
                :counter="100"
                required
                class="bg-white"
                v-model="edit_courses.name"
                :error-messages="v$?.edit_courses?.name?.$errors?.map(e => e.$message) || []"

            ></v-text-field>

          </v-col>

        </v-row>
        <v-row dense>
          <v-col
              cols="12"
              md="12"
              sm="12"
          >
            <v-text-field
                clearable
                type="number"
                label="Coloque la duración del curso"
                variant="solo-filled"
                required
                class="bg-white"
                :min="0"
                :max="1000"
                v-model="edit_courses.duration"
                :error-messages="v$?.edit_courses?.duration?.$errors?.map(e => e.$message) || []"
                @blur="v$.edit_courses.duration.$touch()"

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
            @click="createCourse()"
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
            ¿Está seguro de eliminar el curso?


          </v-card-title>
          <v-card-text class="text-center">
            Esta acción eliminará el curso <strong class="text-red"><u>{{ to_delete.name }}</u></strong>.
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
                @click="deleteCourse(this.to_delete)"
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
        <span>Editar curso</span>

      </v-card-title>
      <v-card-text>
        <v-row dense>
          <v-col
              cols="12"
              md="12"
              sm="12"
          >
            <v-text-field clearable label="Coloque el curso" variant="solo-filled" :counter="1000"
                          required class="bg-white" v-model="edit_courses.name"></v-text-field>

          </v-col>

        </v-row>
        <v-row dense>
          <v-col
              cols="12"
              md="12"
              sm="12"
          >
            <v-text-field
                clearable
                type="number"
                label="Coloque la duración del curso"
                variant="solo-filled"
                required
                class="bg-white"
                v-model="edit_courses.duration"
                :error-messages="v$?.edit_courses?.duration?.$errors?.map(e => e.$message) || []"
                @blur="v$.edit_courses.duration.$touch()"

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
            @click="updateCourse(this.to_edit)"

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
import {required, maxLength, helpers, numeric, maxValue, minValue} from "@vuelidate/validators";

export default {
  name: "CourseView",

  data() {
    return {


      courses: [],
      error_message: "",

      editedIndex: -1,
      edit_courses: {
        name: "",
        duration: null
      },
      default_item: {
        name: "",
        duration: null

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
          title: 'Nombre del curso',
          align: 'start',
          sortable: true,
          value: 'name',

        },
        {
          title: 'Duración (Horas)',
          sortable: true,
          value: 'duration',

        },

        {title: "Actions", value: "actions", sortable: true,}

      ],

    }
  },
  validations() {
    return {
      edit_courses: {
        name: {
          required: helpers.withMessage("El campo nombre es obligatorio", required),
          maxLength: helpers.withMessage("Máximo 50 caracteres", maxLength(50)),
        },
        duration: {
          required: helpers.withMessage("El campo duración es obligatorio", required),
          numeric: helpers.withMessage("El campo duración debe ser un número", numeric),
          maxValue: helpers.withMessage("Máximo permitido: 100", maxValue(1000)),
          minValue: helpers.withMessage("Minimo permitido: 0", minValue(0)),
        }
      }
    }
  }

  ,

  methods: {

    async fetchCourses() {
      try {
        const response = await apiClient.get("/api/course/");
        this.courses = response.data;
      } catch (error) {
        console.error("Error fetching courses:", error);
      }
    },
    async createCourse() {
      this.v$.$touch();

      if (this.v$.$invalid) {
        this.error_message = this.v$?.edit_courses?.name?.$errors?.[0]?.$message || "Campos inválidos";
        this.alertDialog = true;
        return;
      }

      try {
        this.isLoading = true;


        const response = await apiClient.post("/api/course/", this.edit_courses);
        this.courses.push(response.data);
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
        await this.fetchCourses();
        this.v$?.edit_courses?.$reset();
        this.edit_courses.name = "";
        this.edit_courses.duration = null;
        await new Promise(resolve => setTimeout(resolve, 500));
        this.isLoading = false;
        this.addDialog = false;
      }

    },


    async updateCourse(course) {

      if (this.editedIndex > -1) {
        const edited = Object.assign(
            this.courses[this.editedIndex],
            this.edit_courses
        );
        try {
          const response = await apiClient.put(`/api/course/${edited.id}/`, edited);
          const index = this.courses.findIndex(a => a.id === course.id);
          this.isLoading = true;
          if (index !== -1) {
            this.courses[index] = response.data;
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
          await this.fetchCourses();
          await new Promise(resolve => setTimeout(resolve, 500));
          this.isLoading = false;
          this.editDialog = false;

        }
      }


    },

    async deleteCourse(course) {
      try {
        await apiClient.delete(`/api/course/${course.id}/`);
        this.courses = this.courses.filter(courseToDelete => courseToDelete.id !== course.id);
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
        await this.fetchCourses()
        await new Promise(resolve => setTimeout(resolve, 500));
        this.isLoading = false;

        this.deleteDialog = false;
      }
    },

    openAddDialog() {
      this.edit_courses = Object.assign({}, this.default_item);
      this.addDialog = true;

    },
    openDeleteDialog(to_delete) {
      this.to_delete = to_delete;
      this.deleteDialog = true;
    },
    openEditDialog(item) {
      // editedIndex guarda el id del arreglo creado localmente
      this.editedIndex = this.courses.indexOf(item);
      // En este caso el id del arreglo local es el mismo que el id de la base de datos
      this.edit_courses = Object.assign({}, item);
      this.editDialog = true;
    },


  },

  mounted() {
    this.fetchCourses();
  },

  setup() {
    return {v$: useVuelidate()};
  },
  created() {
    this.v$ = useVuelidate();
  },
  watch: {
    'edit_courses.duration'(newVal) {
      if (newVal > 1000) {
        this.edit_courses.duration = 1000;
      } else if (newVal <= 0) {
        this.edit_courses.duration = 0;
      }
    }

  }


};
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