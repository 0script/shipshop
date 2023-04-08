<template>

    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log Out</button>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default{
        name:'MyAccountView',
        methods:{
            logout(){
                
                axios.defaults.headers['Authorized']=''

                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')

                this.$store.commit('removeToken')

                this.$router.push('/')
            }
        }
    }
</script>