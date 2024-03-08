import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import './assets/main.css'

const myapp = createApp(App)
const pinia = createPinia()

myapp.use(pinia)
createApp(App).mount('#app')

// Importa el archivo JavaScript de Bootstrap desde node_modules
import "../node_modules/bootstrap/dist/js/bootstrap.js"
// Importa el archivo CSS de Bootstrap desde node_modules
import "../node_modules/bootstrap/dist/css/bootstrap.min.css"