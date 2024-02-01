import Vue from 'vue';
import App from './App.vue';
import sileo from 'sileo';
import './global.css';

// sileo.defaults.baseUrl = 'http://127.0.0.1:8000/';
Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount('#app');
