<template>

    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>Rwf{{ item.product.price }}</td>
        <td>

            <a @click="decrementQuantity(item)">- </a>{{ item.quantity }}<a @click="incrementQuantity(item)"> +</a>
        </td>
        <td>{{ getItemTotal() }}Rwf</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>

    export default{
        name:'CartItem',
        props:{
            initialItem: {
                type: Object,
                default: {}
            }
        },
        data(){
            return{
                item:this.initialItem
            }
        },
        methods:{
            getItemTotal(){
                return this.item.quantity * this.item.product.price
            },
            decrementQuantity(item){
                item.quantity-=1

                if(item.quantity===0){
                    this.$emit('removeFromCart',item)
                }

                this.updateCart()
            },
            incrementQuantity(item){
                item.quantity+=1
                this.updateCart()
            },
            updateCart(){
                localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
            },
            removeFromCart(item){
                this.$emit('removeFromCart',item)
                this.updateCart()
            }
            
        }
    }
</script>