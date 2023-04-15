<template>
  <div id="app">
    <nav class="navbar is-dark">

      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>ShipShop</strong>
        </router-link>

        <a 
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

        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/#/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input is-normal" placeholder="What are you lookning for" name="q" />
                </div>
                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <font-awesome-icon icon="fa-solid fa-search" />
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">

          <router-link to="/phone" class="navbar-item">Phone</router-link>
          <router-link to="/computer" class="navbar-item">Computer</router-link>
          <router-link to="/accessory" class="navbar-item">Accessory</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link v-if="$store.state.isAuthenticated" to="/my-account" class="button is-light">
                My Account
              </router-link>
              <router-link v-else to="/log-in" class="button is-light">
                Log In
              </router-link>

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
    <div 
      class="is-loading-bar has-text-centered"
      v-bind:class="{'is-loading':$store.state.isLoading}"
      >
        <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view></router-view>
    </section>
  
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>

  import axios from 'axios'

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

      const token=this.$store.state.token

      if(token){
        axios.defaults.headers.common['Authorization']='Token '+token
      }else{
        axios.defaults.headers.common['Authorization']=''
      }
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

  .lds-dual-ring{
    display:inline-block;
    width: 80px;
    height: 80px;
  }

  .lds-dual-ring::after{
    content: "";
    display: block;
    widows: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color:#ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;

  }

  @keyframes lds-dual-ring{
    
    0%{
      transform:rotate(0deg);
    }
    100%{
      transform:rotate(360deg);
    }
  }

  .is-loading-bar{
    height: 0;
    overflow: hidden;

    --webkit-transition: all 0.3s;
    transition: all 0.3s;

    &.is-loading{
      height: 80px;
    }
  }
</style>
