<template>
    <nav-bar/>
    <div class = "container">
    <h2>Заявки</h2>
    <table class="table table-hover ">
    <thead>
        <tr>
            <th> id </th>
            <th> ФИО </th>
            <th> номер телефона</th>
            <th> должность </th>
            <th> вид проблемы </th>
            <th> статус </th>
            <th> комметарии </th>
        </tr>
    </thead>
        <tbody >
            <tr v-for="app in appList" :key="app.id" >
                <td>{{app.id}}</td>
                <td>{{app.user_name}}</td>
                <td>{{app.tel? app.tel:'-'}}</td>
                <td>{{app.position}}</td>
                <td>{{app.kind_of_problem.naming}}</td>
                <td>{{app.get_status_display}}</td>
                <td>{{app.comment? app.comment:'-'}}</td>
            </tr>
        </tbody>
    </table>
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
        async getApplication(){
            let params = {}
            let data = await Application.objects.filter(params)
            this.appList = data 
        }

    },

    mounted(){
        this.getApplication()
    },

    components: {
      NavBar,
      ContactBar,
    }
}

</script>

<style>

</style>