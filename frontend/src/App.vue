<template>
  <div id="app">
    <nav class="navbar is-dark">

      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>ShipShop</strong>
        </router-link>

        <a href="#" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">

          <router-link to="/phone"></router-link>
          <router-link to="/electronics"></router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i>
                </span>
                <span>Cart</span>
              </router-link>

            </div>
          </div>



        </div>
      </div>



    </nav>


    <section class="section">

    </section>
  
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
</style>
