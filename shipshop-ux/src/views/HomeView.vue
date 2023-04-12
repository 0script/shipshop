<template>
  <div class="home container">

    <section  
      class="hero is-medium is-dark mb-6" 
      :style="{
        'background-image':'url(https://www.mendix.com/wp-content/uploads/iStock-1309800161-scaled.jpg)',
        'background-repeat': 'no-repeat',
        'background-size':'contain',
        'background-attachment': 'fixed',
        'background-position': 'center' 
        }"
    >
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to shipshop
        </p>
        <p class="subtitle">
          Upgrade and switch phone and computer
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size02 has-text-centered">
          Latest Product
        </h2>
      </div>

      <products-list
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      >
      </products-list>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import ProductsList from '@/components/ProductsList.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    ProductsList
  },
  data(){
    return{
      latestProducts:[]
    }
  },
  mounted(){
    this.getLatestProducts()
  },
  methods:{
    getLatestProducts(){
      
      axios
        .get('/api/v1/latest-products')
        .then(response=>{
          this.latestProducts=response.data
        })
        .catch(error=>{
          console.log('ERROR DURING REQUEST')
          console.log(error)
        })
    }
  }
}
</script>
