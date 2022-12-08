<template>
    <div class = "contact">
        <div class = "container">
            <div class= "row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                <div class = "col" v-for="cont in contact_list" :key="cont.id">
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
import axios from 'axios'

export default{
    name:'contact-bdr',

    data(){
        return {
          contact_list:[]
        }
    },

    methods:{
        async getContact(){
            let params = {}
            let data = (await axios.get('/api/contact/', {params})).data
            this.contact_list = data 
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