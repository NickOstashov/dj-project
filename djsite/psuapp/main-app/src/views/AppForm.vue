<template>
    <div class="container">
        <h2> Создать статью </h2>
        <div>
            <div> ФИО </div>
            <input v-model="app.user_name" class="form-control"/>
        </div>

        <div>
            <div> Описание</div>
            <input v-model="app.comment" class="form-control"/>
        </div>

        <button class="btn btn-primary" @click="save"> Сохранить</button>
    </div>
</template>
<script>
import {Application} from "@/api"
export default{
    name:'app-form',
    data(){
        return {
            app:{},
        }
    },
    components:{
       
    },
    methods:{
        async save(){
            let app = this.app
            await Application.objects.save(app)
            this.$router.push('/')
        }

        // async save(){
        //     axios.post('/api/application/',this.app)
        // }
    }
}
</script>

