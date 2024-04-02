<!-- FormularioPersona.vue -->
<template>
  <!-- Contenedor principal del componente -->
  <div id="formulario-persona">
    <!-- Formulario con campos para ingresar información de una persona -->
    <form @submit.prevent="enviarFormulario">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <label>Nombre</label>
              <input
                ref="nombre"
                v-model="persona.nombre"
                type="text"
                class="form-control"
                data-cy="name"
                :class="{ 'is-invalid': procesando && nombreInvalido }"
                @focus="resetEstado"
                @keypress="resetEstado"
              >
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Apellido</label>
              <input
                v-model="persona.apellido"
                type="text"
                class="form-control"
                data-cy="surname"
                :class="{ 'is-invalid': procesando && apellidoInvalido }"
                @focus="resetEstado"
              >
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Email</label>
              <input
                v-model="persona.email"
                type="email"
                class="form-control"
                data-cy="email"
                :class="{ 'is-invalid': procesando && emailInvalido }"
                @focus="resetEstado"
              >
            </div>
          </div>
        </div>
        <br>
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <button
                class="btn btn-primary"
                data-cy="add-button"
              >
                Añadir persona
              </button>
            </div>
          </div>
        </div>
      </div>
      <br>
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <div
              v-if="error && procesando"
              class="alert alert-danger"
              role="alert"
            >
              Debes rellenar todos los campos!
            </div>
            <div
              v-if="correcto"
              class="alert alert-success"
              role="alert"
            >
              La persona ha sido agregada correctamente!
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
  

<script>
    // Importa las funciones ref y defineEmits desde la biblioteca Vue
    import { ref, defineEmits, computed } from 'vue';

    // Exportación del componente "FormularioPersona"
    export default {
        // Nombre del componente
        name: 'FormularioPersona',

        // Añade la opción "emits" para declarar los eventos emitidos por el componente
        emits: ['add-persona'],

        // Configuración del componente usando el sistema "setup"
        setup(props, ctx) {
            const procesando = ref(false);
            const correcto = ref(false);
            const error = ref(false);

            const nombre = ref(null);
            
            // Define emisiones personalizadas para este componente
            const emit = defineEmits();

            // Declaración de una variable reactiva "persona" con propiedades
            const persona = ref({
                nombre: '',
                apellido: '',
                email: '',
            });

            const enviarFormulario = () => {
                procesando.value = true;
                resetEstado();
                if (nombreInvalido.value || apellidoInvalido.value || emailInvalido.value) {
                    error.value = true;
                    return;
                }

                // Verificar si el correo electrónico es válido
                if (!validarEmail(persona.value.email)) {
                    return;
                }

                ctx.emit('add-persona', persona.value);
                nombre.value.focus();

                persona.value = {
                    nombre: '',
                    apellido: '',
                    email: '',
                };

                error.value = false;
                correcto.value = true;
                procesando.value = false;

            };

            const validarEmail = (email) => {
              // Expresión regular para validar el formato del correo electrónico
              const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
              return regex.test(email);
            };
                
            const resetEstado = () => {
                correcto.value = false;
                error.value = false;
            };

            const nombreInvalido = computed(() => persona.value.nombre.length < 1);
            const apellidoInvalido = computed(() => persona.value.apellido.length < 1);
            const emailInvalido = computed(() => persona.value.email.length < 1);

            // Retorno de las variables o funciones que el componente va a exponer
            return {
                persona,
                enviarFormulario,
                procesando,
                correcto,
                error,
                nombreInvalido,
                apellidoInvalido,
                emailInvalido,
                resetEstado,
                nombre,
            };
        },
    };
</script>

<style scoped>
    /* Estilos específicos del componente con el modificador "scoped" */
    form {
        margin-bottom: 2rem;
    }
</style>
