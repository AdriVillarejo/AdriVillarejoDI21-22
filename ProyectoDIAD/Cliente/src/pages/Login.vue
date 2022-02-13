<template>
  <q-page class="bg-light-blue window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input square filled clearable v-model="Usuario" type="email" label="Usuario" />
              <q-input square filled clearable v-model="Contraseña" type="password" label="Contaseña" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn unelevated color="light-blue-7" size="lg" class="full-width" label="Login" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">¿No tienes cuenta?
              <a href="#/Registrarse"> Create una cuenta!! </a>
            </p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      Usuario: '',
      Contraseña: ''
    }
  }
}
</script>

<style>
.q-card {
  width: 360px;
}
</style>
