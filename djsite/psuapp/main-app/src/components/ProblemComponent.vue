<template>
        <div class = "problem">
            <div class = "problem-search">
                <div class = "container problem-searchh__item">
                    <h2 class = "problem-title">Возможные проблемы</h2>
                    <div class = "col-6 problem-search__field">
                        <img src="@/assets/img/search.svg" alt="#" class = "problem-search__field__icon">
                        <input v-model="filters.naming__icontains" class="problem-search__field__input" placeholder="Введите запрос"/>
                    </div>
                </div>
            </div>
            <div class = "container">  
                <div class= "row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">              
                    <div class= "col" v-for="pr in problem_list" :key="pr.id" @click="toDetail(pr)">
                        <div class = "card h-100 problem-card">
                            <div class = "problem-img">
                                <img :src="pr.icon" style = "max-width:80px">
                            </div>
                            <div class = "card-body">
                                <h5 class = "card-title problem-naming">{{pr.naming}}</h5>
                                <p class= "problem-description">{{pr.description}}</p>
                            </div>
                        </div>
                    </div>        
                </div>
            </div>  
        </div>
</template>

<script>
import {Problem} from '@/api'


export default{
    name:'problem-component',

    data(){
        return {
            filters:{},
            searchField:'',
            selectProblem:{},
            problem_list:[]
        }
    },

    watch:{
        searchFiedl(){
            this.getProblem()
        },
        filters:{
            deep:true,
            handler(){
                this.getProblem()
            },
        },
    },

    methods:{
        toDetail(pr){
            this.$router.push({name:'problem-detail',params:{id:pr.id}})
        },

        async getProblem(){
            let params = {
                naming__icontainns:this.searchField,
                ...this.filters
            }
            let data = await Problem.objects.filter(params)
            this.problem_list = data 
        }
    },

    mounted(){
        this.getProblem()
    },

}
</script>

<style>

:root{
    --major-background: #CE1532;
    --minor-background: #FFC7C7;
    --hover-card-color: rgba(255, 219, 219, 0.8);
    --description-text-color: rgb(0,0,0);
    --search-bacground: rgb(255,255,255);
}

.problem{
    margin-bottom: 100px;
    width: 100%;
    min-height: 800px;
}

.problem-search{
    background-color: var(--minor-background);
    width: 100%;
    padding: 20px 0px;
    margin-bottom: 20px;
}

.problem-searchh__item{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.problem-search__field{
    display: flex;
    align-items: center;
    background-color: var(--search-bacground);
    padding: 5px 5px;
    border-radius: 10px;
}

.problem-search__field__icon{
    width: 20px;
    height: 20px;
    padding-right: 5px;
}

.problem-search__field__input{
    border: none;
    width: 80%;
}

.problem-search__field__input:focus{
    outline:none;
}

.problem-naming{
    color: var(--major-background)
}

.problem-description{
    color:var(--description-text-color)
}

.problem-card{
    display: flex;
    align-items: center;
    padding: 10px;
    flex-direction: row !important;
    height: 100%;
}

.problem-card:hover{
    background-color: var(--hover-card-color)
}

.card h-100 problem-card{
    flex-direction: row;
}

</style>