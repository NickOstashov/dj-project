<template>
    <div class = "container">
        <h2 class = "problem-title">Возможные проблемы</h2>
        <div class= "row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
            <a class = "problem-link" href ="#" v-for="pr in poblem_list" :key="pr.id">
                <div class= "col">
                    <div class = "card h-100 my-card">
                        <img src="{{pr.icon? pr.icon:''}}" style = 'max-width:80px'>
                        <div class = "card-body">
                            <h5 class = "card-title problem-naming">{{pr.naming}}</h5>
                             <p class= "problem-description">{{pr.description}}</p>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <button @click="getProblem">получить</button>
    </div>
</template>

<script>
import axios from 'axios'

export default{
    name:'problem-component',

    data(){
        return {
          problem_list:[]
        }
    },

    methods:{
        async getProblem(){
            let params = {}
            let data = (await axios.get('/api/problem/', {params})).data
            this.problem_list = data 
        }
    },
}
</script>

<style>
.container{
    margin-top: 200px;
    margin-bottom: 200px;
}

</style>