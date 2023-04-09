<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form @submit.prevent="submitForm">
                    
                    <div class="field">
                        <label for="">UserName</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" />

                        </div>
                    </div>
                    <div class="fields">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notificatino is-danger" v-if="errors.length">
                        <p 
                            v-for="error in errors"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark mt-3">Log In</button>
                        </div>
                    </div>

                    <hr />
                        <p class="bd-footer-tsp">
                            You don't have an account <router-link to="/sign-up">Sign Up</router-link> 
                        </p>
                         
                </form>
            </div>
        </div>
    </div>
</template>

<script>

    import axios from 'axios'
    import { toast } from 'bulma-toast'


    export default{
        name:'LogInView',
        data(){
            return{
                username:'',
                password:'',
                errors:[]
            }
        },
        mounted(){
            document.title='ShipShop: Log In'
        },
        methods:{
            async submitForm(){
                
                console.log('form submission')
                
                axios.defaults.headers.common['Authorization']=''

                localStorage.removeItem('token')

                const formData={
                    username:this.username,
                    password:this.password
                }

                console.log('axios query')

                await axios
                    .post('/api/v1/token/login/',formData)
                    .then(response=>{
                        const token=response.data.auth_token

                        this.$store.commit('setToken',token)

                        axios.defaults.headers.common['Authorization']='Token '+token

                        localStorage.setItem('token',token)

                        const toPath=this.$route.query.to || '/cart'

                        this.$router.push(toPath)
                    })
                    .catch(error=>{
                        if(error.response){

                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        }else if(error.message){
                            this.errors.push('Something went wrong . Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })

                    console.log('axios query is done ')

            }
        }

    }
</script>