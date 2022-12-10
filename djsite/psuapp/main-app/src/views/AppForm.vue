<template>
    <nav-bar/>
    <div class="container">
        <div class = "application col-8">
            <h2> Создать заявку </h2>
            <div class = 'col-8'>
                <div class = "app-field">
                    <div> ФИО </div>
                    <input v-model="app.user_name" class="form-control app-form" placeholder="Иванов Иван Иванович"/>
                </div>

                <div class = "app-field">
                    <div> Должность</div>
                    <input v-model="app.position" class="form-control app-form" placeholder="Преподаватель"/>
                </div>

                <div class = "app-field">
                    <div>Вид проблемы</div>
                    <input v-model="app.kind_of_problem" class="form-control app-form" placeholder="Компьютер"/>
                </div>

                <div class = "app-field">
                    <div> Номер телефона </div>
                    <input v-model="app.tel" class="form-control app-form" placeholder="+7 (999) 999-99-99" pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"/>
                </div>

                <div class = "app-field">
                    <div> Комметарии </div>
                    <textarea v-model="app.comment" class="form-control app-form" id="exampleFormControlTextarea1" rows="3" placeholder="памагити"/>
                </div>

                <button class="btn btn-primary send-btn" @click="save"> Оставить заявку</button>
            </div>
        </div>
    </div>
    <contact-bar/>
</template>
<script>
import {Application} from "@/api"
import NavBar from "@/components/NavBar.vue"
import ContactBar from "@/components/ContactBar.vue"


export default{
    name:'app-form',
    data(){
        return {
            app:{},
        }
    },
    components:{
       NavBar,
       ContactBar,
    },
    methods:{
        async save(){
            let app = this.app     
            await Application.objects.save(app)
            this.$router.push('/applications/')
        }
    }
}
</script>


<style>

:root{
    --border-color:#C9C9C9;
    --form-color:white;
}

.application{
    margin: 0 auto;
    border: 2px solid var(--border-color);
    border-radius: 20px;
    padding: 20px 30px;
    margin-top: 50px;
    background-color: var(--form-color);
}

.app-field{
    margin: 10px 0px;
}

.app-form{
    border: 2px solid var(--border-color);
    border-radius: 10px;
}


.send-btn{
    margin-top: 30px;
    color: #ce1532;
    padding: 5px 10px;
    background-color: #FFBDBD;
    border:none;
    border-radius: 10px;
}

.send-btn:hover{
    background-color: rgba(255, 189, 189,0.5)
}

</style>
