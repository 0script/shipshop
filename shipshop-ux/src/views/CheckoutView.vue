<template>

    <div class="page-checkout">
        <div class="columns is-multiline">

            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
        </div>

        <div class="column is-12">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Totla</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                    >
                        <th>{{ item.product.name }}</th>
                        <th>Rwf{{ item.product.price }}</th>
                        <th>{{ item.quantity }}</th>
                        <th>{{ getItemTotal(item).toFixed(2) }}</th>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <th colspan="2">Total</th>
                        <th>{{ cartTotalLength }}</th>
                        <th>{{ cartTotalPrice }}</th>
                    </tr>


                </tfoot>
            </table>
        </div>

        <div class="column is-12">

            <h2 class="subtitle">Shiping Detail</h2>
            <p class="has-text-grey mb-4">* All Fields Are Required</p>
            
            <div class="columns is-multiline">

                <div class="column is-6">

                    <div class="field">
                        <label >First Name*</label>
                        <div class="control">
                            <input type="text" class="input" v-model="first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Last Name*</label>
                        <div class="control">
                            <input type="text" class="input" v-model="last_name">
                        </div>
                    </div>
                    <div class="field">
                        <label >Email*</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                    </div>
                </div>

                <div class="column is-6">

                    <div class="field">
                        <label >Phone*</label>
                        <div class="control">
                            <input type="tel" class="input" v-model="phone">
                        </div>
                    </div>
                    <div class="field">
                        <label>Address*</label>
                        <div class="control">
                            <input type="text" class="input" v-model="address">
                        </div>
                    </div>
                    <div class="field">
                        <label >Place*</label>
                        <div class="control">
                            <input type="text" class="input" v-model="place">
                        </div>
                    </div>
                </div>
                
                <div class="column is-12">
                    <div class="notification is-danger mt-4" v-if="errors.length">
                        <p 
                            v-for="error in errors"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>
                    <hr />

                    <div id="card-element mb-5"></div>
                    <template v-if="cartTotalLength">
                        <button class="button is-dark" @click="submitForm">Pay With Stripe</button>
                    </template>
                </div>

    

            </div>
        </div>
    </div>
</template>

<script>

    import axios from 'axios'

    export default{
        name:'Checkout',
        data(){
            return{
                cart:{
                    items:[]
                },
                stripe:{},
                card:{},
                first_name:'',
                last_name:'',
                email:'',
                phone:'',
                address:'',
                place:'',
                errors:[]
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
            },
            getItemTotal(item){
                return item.quantity * item.product.price
            },
            submitForm(){
                
                this.errors=[]

                if(this.first_name===''){
                    this.errors.push('First Name is required !')
                }

                if(this.last_name===''){
                    this.errors.push('Last Name is required !')
                }

                if(this.email===''){
                    this.errors.push('Email is required !')
                }

                if(this.phone===''){
                    this.errors.push('Phone number is required !')
                }

                if(this.address===''){
                    this.errors.push('Address is required !')
                }

                if(this.place===''){
                    this.errors.push('Place is required !')
                }
            }
        }
    }
</script>