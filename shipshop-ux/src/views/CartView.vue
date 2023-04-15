<template>

    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>

                        <!-- <div
                            v-for="item in cart.items"
                            :key="item.product.id"
                        >
                    
                            <cart-item :initialItem="item"></cart-item>

                        </div> -->
                        <cart-item
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            :initialItem="item"
                            v-on:removeFromCart="removeFromCart"
                            >
                        </cart-item>
                    </tbody>
                </table>
                <p v-else>You don't have any item in you cart !!!</p>
            </div>

            <div class="column is-12 box">

                <h2 class="subtitle">Summary</h2>
                <strong>Rwf {{ cartTotalPrice }}</strong> ,{{ cartTotalLength }} items
                <hr />
                <router-link to="/cart/checkout" class="button is-dartk">Checkout</router-link>
                </div>
            </div>
    </div>
</template>

<script>

    import axios from 'axios'
    import uniqueId from "lodash.uniqueid"
    import CartItem from  '@/components/CartItem.vue'

    export default {
        name: 'CartView',
        components:{
            CartItem
        },
        data(){
            return{
                cart:{
                    items:[]
                }
            }
        },
        mounted(){
            this.cart=this.$store.state.cart
        },
        computed:{
            cartTotalLength(){
                return this.cart.items.reduce((acc,curlVal)=>{
                    return acc+=curlVal.quantity
                },0 )
            },
            cartTotalPrice(){
                return this.cart.items.reduce((acc,curlVal)=>{
                    return acc+=curlVal.product.price*curlVal.quantity
                },0 )
            }
        },
        methods:{
            removeFromCart(item){
                this.cart.items=this.cart.items.filter(i=>i.product.id !== item.product.id)
            }
        }
    }
</script>