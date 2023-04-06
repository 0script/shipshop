<template>
  <div id="app">
    <nav class="navbar is-dark">

      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>ShipShop</strong>
        </router-link>

        <a 
          href="#" 
          class="navbar-burger" 
          aria-label="menu" 
          aria-expanded="false" 
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div 
        class="navbar-menu" 
        id="navbar-menu"
        :class="{'is-active':showMobileMenu}"
      >
        <div class="navbar-end">

          <router-link to="/phone" class="navbar-item">Phone</router-link>
          <router-link to="/electronics" class="navbar-item">Computer</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <font-awesome-icon icon="fa-solid fa-cart-shopping" />
                </span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>

            </div>
          </div>



        </div>
      </div>
    </nav>

    <section class="section">
      <router-view></router-view>
    </section>
  
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data(){
      return{
        showMobileMenu:false,
        cart:{
          items:[]
        }
      }
    },
    beforeCreate(){
      this.$store.commit('initializeStore')
    },
    mounted(){
      this.cart=this.$store.state.cart
    },
    computed:{
      cartTotalLength(){
        let totalLength=0

        for(let i=0;i<this.cart.items.length;i++){
          totalLength+=this.cart.items[i].quantity
        }
        return totalLength
      }
    }
  }
</script>


<style lang="scss">
  @import '../node_modules/bulma';
</style>
