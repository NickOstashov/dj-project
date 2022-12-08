import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import HeaderNav from "@/components/HeaderNav"

import "vue-select/dist/vue-select.css"

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle';

const app = createApp(App)
app.component("HeaderNav",HeaderNav)
app.use(router).mount('#app')
