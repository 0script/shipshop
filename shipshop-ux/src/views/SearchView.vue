<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Search
                </h1>
                <h2 class="is-size-5 has-text-grey">
                    Search Term : "{{ query }}"

                </h2>
                <h3 class="is-size-4 hast-text-black"
                    v-if="products.length===0"
                >
                    No Result For {{ query }}
                </h3>
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
import { toast } from 'bulma-toast'

    export default{
        name: 'SearchView',
        components:{
            ProductsList
        },  
        data(){
            return{
                products:[],
                query:''
            }
        },mounted(){
            document.title='ShipShop: Search '

            let uri=window.location.search.substring(1)
            let params=new URLSearchParams(uri)

            console.log(params)

            if(params.get('q')){
                console.log(params.get('q'))
                this.query=params.get('q')

                this.perfomrSearch()
            }
        },
        methods:{
            async perfomrSearch(){
                
                this.$store.commit('setIsLoading',true)

                await axios
                    .post('/api/v1/products/search/',{query:this.query})
                    .then(response=>{
                        this.products=response.data
                    })
                    .catch(error=>{
                        console.log(error)
                        toast({
                            message:'An Error Occured !',
                            type:'error',
                            position:'bottom-right',
                            duration: 2000,
                            dismissible:true,
                            pauseOnHover:true
                        })
                    })

                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>