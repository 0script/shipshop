<template>

    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log Out</button>
            </div>

            <hr />

            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>

                

                <order-summary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order"
                >
                </order-summary>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import OrderSummary from '@/components/OrderSummary.vue'

    export default{
        name:'MyAccountView',
        components:{
            OrderSummary,
        },
        data(){
            return{
                orders:[]
            }
        },
        mounted(){
            this.getMyOrders()
        },
        methods:{
            logout(){
                
                axios.defaults.headers['Authorized']=''

                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')

                this.$store.commit('removeToken')

                this.$router.push('/')
            },
            async getMyOrders(){
                this.$store.commit('setIsLoading',true)
                
                await axios.get('/api/v1/orders')
                    .then(response=>{
                        this.orders=response.data
                    })
                    .catch(error =>{
                        console.log(error)
                    })

                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>