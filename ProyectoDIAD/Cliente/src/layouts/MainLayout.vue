<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>
          Qualificacions APP
          </q-toolbar-title>

          <div>{{ fechaValenciano }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Login',
    caption: 'Iniciar sesion',
    icon: 'login',
    link: '#/Login'
  },
  {
    title: 'About',
    caption: 'Sobre nosotros',
    icon: 'info',
    link: '#/About'
  }
]
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
  computed: {
    fechaValenciano () {
      const fechas = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
      const fecha = new Date().toLocaleDateString('ca-Es', fechas)
      return fecha.toLocaleUpperCase()
    }
  }
})
</script>
