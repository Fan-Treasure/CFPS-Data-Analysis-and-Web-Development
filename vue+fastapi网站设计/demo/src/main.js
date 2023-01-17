import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'//引入axios
import * as echarts from "echarts"
import 'echarts-gl'
import VueSession from 'vue-session'
Vue.use(VueSession)
Vue.prototype.$echarts = echarts
Vue.prototype.$axios = axios;//把axios挂载到vue上

Vue.use(ElementUI);
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')