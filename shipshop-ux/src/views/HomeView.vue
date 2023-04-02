<template>
  <div class="home container">

    <section class="hero is-medium is-dark mb-6">
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

      <div 
        class="column is-3"
        v-for="product in latestProducts"
        v-bind:key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="product.get_thumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">Rwf{{ product.price }}</p>
          View Detail
        </div>
      </div>

    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
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

<style scoped>
  .image{
    margin-top:-1.25rem;
    margin-left:-1.25rem;
    margin-right:1.25rem;
  }
</style>