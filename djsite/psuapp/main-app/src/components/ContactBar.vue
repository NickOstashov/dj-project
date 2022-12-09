<template>
    <div class = "contact">
        <div class = "container">
            <div class= "row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                <div class = "col" v-for="cont in contactList" :key="cont.id">
                    <div class = "card h-60 contact-card">
                        <div class = "card-body">
                            <p class = "contact-text">
                                {{cont.surname}}<br>
                                {{cont.name}}<br>
                            </p>
                            <p class = "contact-text">
                                {{cont.email}}<br>
                                {{cont.tel}}<br>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
//import axios from 'axios'
import {Contact} from '@/api'

export default{
    name:'contact-bar',

    data(){
        return {
          contactList:[]
        }
    },

    methods:{
        async getContact(){
            let params = {}
            let data = await Contact.objects.filter(params)
            this.contactList = data 
        }
    },

    mounted(){
        this.getContact()
    }
}
</script>

<style>
.contact{
    display: flex;
    width: 100%;
    margin-top: 100px;
    flex: 0 0 auto;
    background-color: #C0C0C0;
    padding-bottom: 20 px;
}

.contact-card{
    background: rgba(0, 0, 0, 0) !important;
    border: none !important;
}

.contact-text{
    font-size: 12px;
}

</style>