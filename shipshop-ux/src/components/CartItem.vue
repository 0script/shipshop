<template>

    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>Rwf{{ item.product.price }}</td>
        <td>{{ item.quantity }}</td>
        <td>{{ getItemTotal() }}Rwf</td>
        <td><button class="delete"></button></td>
    </tr>
</template>

<script>

    export default{
        name:'CartItem',
        props:{
            initialItem:Object
        },
        data(){
            return{
                item:this.initialItem
            }
        },
        mounted(){
            console.log(this.item.product.name)
        },
        methods:{
            getItemTotal(){
                return this.item.quantity * this.item.product.price
            }
        }
    }
</script>