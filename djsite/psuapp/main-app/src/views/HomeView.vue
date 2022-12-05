<template>
    <nav-bar></nav-bar>
    <div class = "container">
        <div class = "problem">
            <h2 class = "problem-title">Возможные проблемы</h2>
            <div class= "row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">              
                <div class= "col" v-for="problem in problemList" :key="problem.id">
                    <div class = "card h-100 problem-card">
                        <div class = "problem-img">
                            <img :src="problem.icon" style = 'max-width: 80px'>
                        </div>
                        <div class = "card-body">
                            <h5 class = "card-title problem-naming">{{problem.naming}}</h5>
                            <p class= "problem-description">{{problem.description}}</p>
                        </div>
                    </div>
                </div>        
            </div>
        </div>
    </div>
    <contact-bar></contact-bar>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import ContactBar from './src/components/ContactBar.vue'

export default {
  name: 'home-page',
    data(){
        return {
            filters:{},
            searchFiedl:'',
            selectProblem:{},
            problemList:[
            ]
        }
    },
    methods:{
        async getProblem(){
            let params = {...this.filters}
            params['naming'] = this.filters.problem? this.filters.problem.id:undefined
            let response = await Article.objects.filter(params)
            this.problemList = response.results
      }
    },

    mounted(){
        this.getProblem()
    },
    components: {
      NavBar,
      ContactBar,
    }
}
</script>

<style>
.problem{
    margin: 100px 0;
}


.problem-naming{
    color: #CE1532;
}

.problem-description{
    color:black;
}

.problem-card{
    display: flex;
    align-items: center;
    padding: 10px;
    flex-direction: row !important;
    height: 100%;
}

.problem-card:hover{
    background-color: rgba(255, 219, 219, 0.8);
}

.card h-100 problem-card{
    flex-direction: row;
}


</style>
