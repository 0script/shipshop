<template>
    <div class="page-category">

        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    {{ category.name }}
                </h2>
            </div>
            <products-list
                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product"
            >
            </products-list>

        </div>
    </div>
</template>

<script>

    import axios from 'axios'
    import {toast} from 'bulma-toast'
    import ProductsList from '@/components/ProductsList.vue'

    export default{
        name:'CategoryView',
        components:{
            ProductsList
        },
        data(){
            return{
                category:{
                    products:[]
                }
            }
        },
        mounted(){
            this.getCategory()
        },
        watch:{
            $route(to,from){
                if(to.name==='category'){
                    this.getCategory()
                }
            }
        },
        methods:{
            async getCategory(){
                const categorySlug=this.$route.params.category_slug

                this.$store.commit('setIsLoading',true)

                await axios(`/api/v1/products/${categorySlug}`)
                    .then(response=>{
                        this.category=response.data
                        this.category=this.category[0]
                        document.title='ShipShop: '+this.category.name
                    })
                    .catch(error=>{
                        console.log(error)

                        toast({
                            message:'Something went wrong please try again',
                            type:'is-danger',
                            dismissible:true,
                            pauseOnHover:true,
                            duration:2000,
                            position:'bottom-right'
                        })
                    })

                    this.$store.commit('setIsLoading',false)
                    
            }
        }
    }
</script>