<template>
    <div>
        <v-select @search="getProblem" :options="problem_list" label="naming" @update:modelValue="$emit('update:modelValue',$event)"/>
    </div>
</template>


<script>
import vSelect from 'vue-select'
import {Problem} from '@/api'

    export default{
        name:"select-problem",
        props:['modelValue'],

        data(){
            return{
                problem_list:[],
            }
        },
        methods:{
            async getProblem(search){
                let params = {
                    naming__icontains:search
                }
                let data = await Problem.objects.filter(params)
                this.problem_list = data 
            }
        },
        components:{
            vSelect,
        }
    }
</script>

<style>
</style>