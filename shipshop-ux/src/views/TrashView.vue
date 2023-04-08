<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Search
                </h1>
                <h2 class="is-size-5 has-text-grey">
                    Search Term : "{{ q }}"
                </h2>
            </div>

            <products-list
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
            >
            </products-list>

        </div>

    </div>
</template>

<script>

    import axios from 'axios'
    import ProductsList from '@/components/ProductsList.vue'

    export default{
        name: 'TrashView',
        components:{
            ProductsList
        },
        props:{
            q: String
        },  
        data(){
            return{
                products:[],
            }
        },mounted(){
            document.title='ShipShop: Search'

            // let uri=window.location.search.substring(1)
            // let params=new URLSearchParams(uri)

            console.log('search view')

            // if(params.get('query')){
            //     this.query=params.get('query')
            //     this.perfomrSearch()
            // }
        },
        methods:{
            perfomrSearch(){

            }
        }
    }
</script>