<template>
    <div>
        <nav-bar/>
        <div class = "detail">
            <div class = "detail-title__box">
                <h1 class = "detail-title">{{title}}</h1>
            </div>
            <div class ="container detail-contant">
                <h2>Часто задаваемые вопросы</h2>
                <div v-for="i in faq" :key="i.id">
                    <div class = "cl-ct" @click="collapse">
                        <button class = "collapse-bt">
                            <div class = 'question'>
                            <img src="@/assets/img/close.svg" class='close'>
                            <img src="@/assets/img/open.svg" class='open'>
                            <h3>{{i.question}}</h3>
                            </div>
                        </button>
                        <div class = "collapse-contant">
                            <p>{{i.answer}}</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class = "container application">
                <p class = "application-text">
                    Если вы не нашли ответ на свой вопрос или не можете решить вашу проблему 
                    самостоятельно, оставьте заявку
                </p>
                <button @click = "toCreate" type="button" class="btn btn-danger application-btn">Оставить заявку</button>
            </div>
        </div>
        <contact-bar/>
    </div>
</template>


<script>
import {Faq} from "@/api"
import NavBar from "@/components/NavBar.vue"
import ContactBar from "@/components/ContactBar.vue"

export default {
    name:"problem-detail",
    data(){
        return {
            faq:[],
            title:""
        }
    },
    methods:{
        toCreate(){
            this.$router.push({name:'create-app',params:{}})
        },

        async getFaq(){
        let params ={
            problem:this.$route.params.id
        }
        this.faq = await Faq.objects.filter(params)
        let title = this.faq[0].problem.naming
        this.title = title
        },

        collapse(){
            let coll = document.getElementsByClassName("collapse-bt")
            for (let i =0; i<coll.length;i++){
                coll[i].addEventListener('click',function(){
                    this.classList.toggle('active');
                    let contant = this.nextElementSibling;
                    if (contant.style.maxHeight){
                        contant.style.maxHeight = null;
                    } else {
                        contant.style.maxHeight = contant.scrollHeight + "px"
                    }
                })
            }
        }
    },
    mounted(){
        this.getFaq()
    },
    components:{
        NavBar,
        ContactBar,
    }
}
</script>

<style>

:root{
    --major-background: #CE1532;
    --minor-background: #FFC7C7;
    --minor-background-opacity:rgba(255, 189, 189,0.5);
    --hover-card-color: rgba(255, 219, 219, 0.8);
    --description-text-color: rgb(0,0,0);
    --search-bacground: rgb(255,255,255);
}

.detail{
    min-height: 800px;
}

.detail-title__box{
    background-color: var(--minor-background);
    display: flex;
    padding: 20px 20px;
    justify-content: center;
    margin-bottom:50px;
}

.detail-contant{
    margin-bottom:100px;
}


/* Cворачиваемый раздел */

.collapse-bt{
    cursor: pointer;
    padding: 18px 0;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
}

.question{
    display: flex;
    align-items: center;
}

.question h3{
    margin: 0 0;
}

.close,
.open{
    height: 25px;
    width: 25px;
    order: -1;
    margin-right: 15px;
}

.open{
    display: none;
}

.active .close{
    display: none;
}

.active .open{
    display: inline;
}

.collapse-contant{
    padding: 0 18px;
    max-height: 0px;
    overflow: hidden;
    transition: max-height 0.2s ease-out;
    font-size: 20px;
}


/* Заявка */

.application-text{
    font-size: 18px;
}

.application-btn{
    font-size: 20px;
    color: var(--major-background);
    background-color: var(--minor-background);
    border-radius: 10px;
    border: none;
}

.application-btn:hover{
    color: var(--major-background);
    background-color: var(--minor-background-opacity)
}

</style>