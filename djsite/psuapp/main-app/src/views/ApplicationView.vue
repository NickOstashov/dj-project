<template>
    <nav-bar/>
    <div class="container app-box">
        <div class = "col-10">
        <div class = 'title'>
            <h1>Заявки</h1>
        </div>   
        <table class="table table-hover ">
        <thead>
            <tr>
                <th> id </th>
                <th> ФИО </th>
                <th> номер телефона</th>
                <th> должность </th>
                <th> вид проблемы </th>
                <th> комметарии </th>
                <th> </th>
            </tr>
        </thead>
            <tbody >
                <tr v-for="(app,idx) in appList" :key="app.id" >
                    <td>{{app.id}}</td>
                    <td>{{app.user_name}}</td>
                    <td>{{app.tel? app.tel:'-'}}</td>
                    <td>{{app.position}}</td>
                    <td>{{app.kind_of_problem}}</td>
                    <td>{{app.comment? app.comment:'-'}}</td>
                    <td><button @click="deleteApplication(app,idx)" class = "btn-danger">удалить </button></td>
                </tr>
            </tbody>
        </table>
        </div>
    </div> 

    <contact-bar/>
</template>


<script>
import NavBar from '@/components/NavBar.vue'
import ContactBar from '@/components/ContactBar.vue'
import { Application } from '@/api'

export default {
  name: 'home-page',
    data(){
        return{
          appList:[],
        }
    },


    methods:{
        async deleteApplication(app,idx){
            await Application.objects.delete(app)
            this.appList.splice(idx,1)
        },

        async getApplication(){
            let params = {
                user_name__icontains:this.searchField,
                ...this.filters
            }
            let data = await Application.objects.filter(params)
            this.appList = data 
        }

    },

    mounted(){
        this.getApplication()
    },

    components: {
      NavBar,
      ContactBar
    }
}

</script>

<style>
.title{
    display:flex;
    justify-content: center;
    margin-bottom: 50px;
}

.app-box{
    min-height: 800px;
}

</style>