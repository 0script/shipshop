import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret,faCartShopping,faSearch,faSearchPlus } from '@fortawesome/free-solid-svg-icons'

import axios from 'axios'
axios.defaults.baseURL='http://localhost:8000'

/* add icons to the library */
library.add(faUserSecret,faCartShopping,faSearch,faSearchPlus)


createApp(App)
    .component('font-awesome-icon', FontAwesomeIcon)
    .use(store)
    .use(router,axios)
    .mount('#app')
